# serverless.py
from flask import Flask, request, jsonify, session  
import importlib.util
import os
import logging
from dotenv import dotenv_values  

def check_auth():  # 檢查使用者是否已登入
    return session.get('authenticated') == True  

app=Flask(__name__)
# 從 .env 讀取權杖 (密碼) 與金鑰
config=dotenv_values('.env')
SECRET_TOKEN=config.get('SECRET_TOKEN')  # 易記的令牌 (類似密碼)
SECRET_KEY=config.get('SECRET_KEY')  # 簽章加密用的金鑰
app.secret_key=SECRET_KEY  # 用來簽章與驗證 session cookie
# 指定函式模組所在的資料夾
FUNCTIONS_DIR=os.path.expanduser('./functions')
# 指定錯誤日誌檔 (在目前工作目錄下)
logging.basicConfig(filename='serverless_error.log', level=logging.ERROR)
# 需要驗證的函式列表
PROTECTED_FUNCTIONS=['list_functions',
                     'add_function',
                     'save_function',
                     'edit_function',
                     'update_function',
                     'delete_function'
                     ]
# 登入管理功能
@app.route('/login', methods=['GET', 'POST'])
def login():
    # GET 請求 : 顯示登入頁面
    if request.method == 'GET':  
        return '''
        <!DOCTYPE html>
        <html>
        <head><title>系統登入</title></head>
        <body>
            <h2>系統登入</h2>
            <form method="post">
                <input type="password" name="token" placeholder="請輸入密碼" required>
                <button type="submit">登入</button>
            </form>
        </body>
        </html>
        '''
    # POST 請求 : 處理登入請求
    if request.is_json:  # JSON 登入 
        token=request.json.get('token')
    else:   # 表單登入
        token=request.form.get('token')    
    if token == SECRET_TOKEN:  # 驗證登入密碼
        # 將登入狀態儲存在瀏覽器的 session cookie 中 (以明碼方式儲存)
        # Flask 會用金鑰對資料進行簽章 (非加密) 確保內容未被竄改
        session['authenticated']=True    
        # 回應登入成功
        if request.is_json:  
            return jsonify({'message': '登入成功'})
        else:
            return '<p>登入成功！<a href="/function/list_functions">查看函式列表</a></p>'
    else:  # 密碼錯誤 : 回應登入失敗訊息
        if request.is_json:
            return jsonify({'message': '登入失敗'}), 401
        else:
            return '<p>登入失敗！<a href="/login">重新登入</a></p>', 401

# 登出管理功能 
@app.route('/logout')
def logout():
    session.clear()  # 清除伺服端 Flask session 字典中的所有鍵值對
    return '<p>已登出！<a href="/login">重新登入</a></p>'

# 動態載入 & 執行函式模組 (支援 RESTful) 
@app.route('/function/<func_name>', defaults={'subpath': ''}, methods=['GET', 'POST'])
@app.route('/function/<func_name>/<path:subpath>', methods=['GET', 'POST'])
def handle_function(func_name, subpath):  # 傳入 subpath 支援 RESTful
    # 1. 檢查是否為保護的函式模組且使用者已登入
    if func_name in PROTECTED_FUNCTIONS and not check_auth():
        return jsonify({'error': 'Authentication required', 'login_url': '/login'}), 401    
    # 2. 取得檔案路徑
    func_path=os.path.join(FUNCTIONS_DIR, f'{func_name}.py')
    if not os.path.isfile(func_path):  # 模組檔案不存在 -> 回 404
        return jsonify({'error': f'Function "{func_name}" not found'}), 404
    try:
        # 3. 動態載入模組 (絕對路徑)
        spec=importlib.util.spec_from_file_location(func_name, func_path)
        module=importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        # 4. 檢查模組中有無 main() 函式 :
        if not hasattr(module, 'main'):  # 模組中無 main() 函式
            return jsonify({'error': f'Module "{func_name}" has no main()'}), 400
        # 5. 將 subpath 加入 request 中 (支援 RESTful)
        request.view_args['subpath']=subpath  
        # 6. 執行模組中的函式 :        
        result=module.main(request)  # 將 request 傳給被載入模組由其自行處理參數
        # 7. 傳回函式執行結果
        return result 
    except Exception as e:
        logging.exception(f'Error in function {func_name}\n{e}')  # 紀錄錯誤於日誌
        return jsonify({'error': 'Function execution failed'}), 500

if __name__ == '__main__':
    app.run(debug=True)
