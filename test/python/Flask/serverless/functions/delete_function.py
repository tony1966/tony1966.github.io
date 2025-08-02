# delete_function.py
import os

def main(request):
    module_name=request.args.get('module_name', '').strip()
    # 過濾模組名稱
    if not module_name:
        return '<p>錯誤：未提供模組名稱</p>'
    if not module_name.isidentifier():
        return '<p>錯誤：模組名稱須為合法的 Python 識別字</p>'    
    if '/' in module_name or '\\' in module_name or '..' in module_name:
        return '錯誤：無效的函式名稱'  # 避免目錄穿越攻擊(只允許純檔名, 無 / 或 ..)  
    filename=f'./functions/{module_name}.py'
    if not os.path.exists(filename):
        return f'<p>錯誤：模組 {module_name} 不存在</p>'
    try:
        os.remove(filename)  # 刪除檔案
        return f'''
        <p>已成功刪除模組：{module_name}</p>
        <a href="/function/list_functions">返回函式列表</a>
        '''
    except Exception as e:
        return f'<p>刪除失敗：{e}</p>'