# add_function.py
def main(request):
    html='''
    <h2>新增函式模組</h2>
    <form action="/function/save_function" method="post">
        <label>模組名稱（請用英數字，不含副檔名 .py）:</label><br>
        <input type="text" name="module_name" size="50" required><br><br>
        <label>模組內容（請輸入合語法的 Python 程式碼）:</label><br>
        <textarea id="code" name="code" rows="20" cols="100" required></textarea><br><br>
        <button onclick="location.href='/function/list_functions'">取消</button>
        <button type="button" onclick="document.getElementById('code').value = '';">清除</button>
        <input type="submit" value="存檔">
    </form>
    '''
    return html
