# edit_function.py
# 模組名稱也可更改 -> 相當於新增模組
from flask import render_template_string
import os

def main(request):
    module_name=request.args.get('module_name', '')  # 取得模組名稱
    if not module_name:  # 檢查有無傳入模組名稱
        return '請指定要編輯的模組名稱，格式 ?module_name=hello'
    filename=f'./functions/{module_name}.py'
    if not os.path.isfile(filename):
        return f'找不到函式檔案：{module_name}'
    with open(filename, 'r', encoding='utf-8') as f: 
        content=f.read()  # 讀取模組內容
    html=f'''
    <h2>編輯函式模組：/functions/{module_name}.py</h2>
    <form method="POST" action="/function/update_function">
        <label>模組名稱（請用英數字，不含副檔名 .py）:</label><br>    
        <input type="text" name="module_name" size="50" value="{module_name}"><br><br>
        <label>模組內容（請輸入合語法的 Python 程式碼）:</label><br>        
        <textarea id="code" name="code" rows="20" cols="100" style="font-family:monospace;">{content}</textarea><br><br>
        <button type="button" onclick="location.href='/function/list_functions'">取消</button>
        <button type="button" onclick="document.getElementById('code').value = '';">清除</button>
        <button type="submit">更新</button>
    </form>
    '''
    return render_template_string(html)
