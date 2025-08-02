# list_functions.py
import os

def main(request):
    # 取得 functions 目錄絕對路徑
    functions_dir='./functions'
    # 取得所有 .py 檔案（但排除 __init__.py）
    try:
        files=os.listdir(functions_dir)
        py_files=[f[:-3] for f in files if f.endswith('.py') and f != '__init__.py']
        py_files.sort()  # 按字母順序排序
    except FileNotFoundError:
        return '<p>directory ./functions not found!</p>'
    # 產生 HTML 碼
    html = '<h2>函式列表</h2>'
    html += '<table border="1" cellspacing="0" cellpadding="6" style="border-collapse: collapse;">'
    html += '<tr><th>函式名稱</th><th>執行</th><th>編輯</th><th>刪除</th></tr>'
    PROTECTED_FUNCTIONS=['list_functions',
                     'add_function',
                     'save_function',
                     'edit_function',
                     'update_function',
                     'delete_function']
    for func in py_files:
        if func in PROTECTED_FUNCTIONS:
            continue
        html += f'<tr>'
        html += f'<td>{func}</td>'
        html += f'<td><a href="/function/{func}">執行</a></td>'
        html += f'<td><a href="/function/edit_function?module_name={func}">編輯</a></td>'
        html += f'<td><a href="/function/delete_function?module_name={func}">刪除</a></td>'
        html += f'</tr>'
    html += '</table>'
    html += '<br><a href="/function/add_function">新增函式</a> '
    html += '<a href="/logout">登出</a>'
    return html