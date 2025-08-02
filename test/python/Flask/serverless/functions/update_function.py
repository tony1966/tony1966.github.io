# update_function.py
import os

def main(request):
    if request.method != 'POST':
        return '請使用 POST 方法'
    module_name=request.form.get('module_name', '').strip()
    code=request.form.get('code', '').strip()
    # 檢查檔案名稱合法性
    if not module_name.isidentifier():
        return '<p>錯誤：模組名稱須為合法的 Python 識別字</p>'
    if '/' in module_name or '\\' in module_name or '..' in module_name:
        return '錯誤：無效的函式名稱'  # 避免目錄穿越攻擊(只允許純檔名, 無 / 或 ..)      
    if not code:
        return '<p>錯誤：模組內容不得為空</p>'
    # 組成檔案路徑
    filename=f'./functions/{module_name}.py'
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(code)  # 若檔名一樣覆蓋原內容, 否則建立新模組
        return f'模組 {module_name} 已成功更新!<br><br><a href="/function/list_functions">返回函式列表</a>'
    except Exception as e:
        return f'更新失敗：{e}'
