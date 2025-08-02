# save_function.py
import os

def main(request):
    # 僅接受 POST 請求
    if request.method != 'POST':
        return '<p>只接受 POST 請求</p>'
    module_name=request.form.get('module_name', '').strip()
    code=request.form.get('code', '').strip()
    # 檢查輸入合法性
    if not module_name.isidentifier():
        return '<p>錯誤：模組名稱須為合法的 Python 識別字</p>'
    if '/' in module_name or '\\' in module_name or '..' in module_name:
        return '錯誤：無效的函式名稱'  # 避免目錄穿越攻擊(只允許純檔名, 無 / 或 ..)      
    if not code:
        return '<p>錯誤：模組內容不得為空</p>'
    # 組成檔案路徑
    filename=f'./functions/{module_name}.py'
    if os.path.exists(filename):
        return f'<p>錯誤：模組 <b>{module_name}.py</b> 已存在</p>'
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(code)
    except Exception as e:
        return f'<p>儲存失敗：{e}</p>'
    return f'''
    <p>模組 <b>{module_name}.py</b> 已成功建立</p>
    <a href="/function/list_functions">返回函式列表</a>
    '''

