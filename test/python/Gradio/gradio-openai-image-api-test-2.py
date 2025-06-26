# gradio-image-api-test-2.py
import gradio as gr
from openai import OpenAI

# 圖片尺寸選項
size_options={
    'dall-e-2': ['256x256', '512x512', '1024x1024'],
    'dall-e-3': ['1024x1024', '1024x1792', '1792x1024']
    }

# 呼叫 OpenAI API 生圖
def generate_images(prompt, api_key, **kwargs):
    client=OpenAI(api_key=api_key)
    replies=client.images.generate(prompt=prompt, **kwargs)
    urls=[item.url for item in replies.data]
    return urls  # Gallery 只能接收串列

# 執行按鈕時處理函式
def handler(api_key, prompt, model_sel, size_sel, image_count):
    if not api_key.strip():   # 處理使用者未輸入金鑰問題
        return [], '請輸入 OpenAI API Key'
    if not prompt.strip():   # 處理使用者未輸入提示詞問題
        return [], '請輸入提示詞 (prompt)'
    if model_sel == 'dall-e-2':
        size=size_sel
        n=image_count   # dall-e-2 允許生 1~10 張圖
    else:
        size=size_sel
        n=1   # dall-e-3 只允許生 1 張圖
    urls=generate_images(prompt, api_key, model=model_sel, n=n, size=size)
    msg=f'模型: {model_sel}\n尺寸: {size}\n張數: {n}'   # 輸出設定值
    return urls, msg  # 傳回生圖之網址串列給 Gallery, 設定值給狀態訊息

# 模型選單連動圖片尺寸選單 : 動態更新圖片尺寸選單
def update_size_options(selected_model):
    return gr.update(
        choices=size_options[selected_model],
        value=size_options[selected_model][0]
        )

# 使用 Blocks 語法 (才有元件連動功能)
with gr.Blocks(title='OpenAI Image API 測試') as blocks:
    gr.Markdown('## 🎨 使用 DALL·E 2 / 3 生圖')
    api_key=gr.Textbox(label='請輸入金鑰 (API key)', type='password')
    prompt=gr.TextArea(label='請輸入提示詞 (Prompt)', max_lines=10)
    model_sel=gr.Radio(
        label='選擇模型',
        choices=['dall-e-2', 'dall-e-3'],
        value='dall-e-3'
        )
    size_sel=gr.Radio(
        label='選擇圖片尺寸',
        choices=size_options['dall-e-3'],
        value=size_options['dall-e-3'][0]
        )
    image_count=gr.Slider(
        label='圖片張數 (DALL·E 2 專用)',
        minimum=1,
        maximum=10,
        step=1,
        value=1
        )
    submit_btn=gr.Button('開始生成')
    gallery=gr.Gallery(label='生成的圖片')
    status=gr.Textbox(label='狀態訊息', interactive=False) # 僅輸出
    # 連動更新圖片尺寸選單
    model_sel.change(
        fn=update_size_options,  # 呼叫自訂函式更新尺寸選單內容
        inputs=model_sel,  # 模型選單值
        outputs=size_sel   # 尺寸選單值
        )
    # 點擊按鈕觸發 handler
    submit_btn.click(
        fn=handler,
        inputs=[api_key, prompt, model_sel, size_sel, image_count],
        outputs=[gallery, status]
        )
blocks.launch()
