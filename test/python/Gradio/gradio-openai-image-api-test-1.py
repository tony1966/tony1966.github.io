# gradio-image-api-test-1.py
import gradio as gr
from openai import OpenAI

def generate_images(prompt, api_key, **kwargs):
    client=OpenAI(api_key=api_key)
    replies=client.images.generate(prompt=prompt, **kwargs)
    urls=[item.url for item in replies.data]
    return urls

def handler(api_key, prompt, model_sel, size_sel, image_count):
    if not api_key.strip():  # 處理使用者未輸入金鑰問題
        return [], '請輸入 OpenAI API Key'
    elif not prompt.strip():  # 處理使用者未輸入提示詞問題
        return [], '請輸入提示詞 (prompt)'
    if model_sel == 'dall-e-2':  
        n=image_count  # dall-e-2 允許生 1~10 張圖
        if size_sel == 'dall-e-2:256x256|dall-e-3:1024x1024':
            size='256x256'
        elif size_sel == 'dall-e-2:512x512|dall-e-3:1024x1792':
            size='512x512'
        else:
            size='1024x1024'
    else:  # model_sel='dall-e-3'
        n=1  # dall-e-3 只允許生 1 張圖
        if size_sel == 'dall-e-2:256x256|dall-e-3:1024x1024':
            size='1024x1024'
        elif size_sel == 'dall-e-2:512x512|dall-e-3:1024x1792':
            size='1024x1792'
        else:
            size='1792x1024'
    urls=generate_images(prompt, api_key, model=model_sel, n=n, size=size)
    msg=f'model:{model_sel}\nsize:{size}\nn:{n}'  # 輸出設定值
    return urls, msg  # 傳回生圖之網址給 Gallery, 設定值給狀態訊息

api_key=gr.Textbox(label='請輸入金鑰 (API key)', type='password')
prompt=gr.TextArea(label='請輸入提示詞 (Prompt)', max_lines=10)
model_sel=gr.Radio(
    label='選擇模型',
    choices=['dall-e-2', 'dall-e-3'],
    value='dall-e-3'
    )
size_sel=gr.Radio(
    label='選擇圖片尺寸',
    choices=[
        'dall-e-2:256x256|dall-e-3:1024x1024',
        'dall-e-2:512x512|dall-e-3:1024x1792',
        'dall-e-2:1024x1024|dall-e-3:1792x1024'
        ],
    value='dall-e-2:256x256|dall-e-3:1024x1024'
    )
image_count=gr.Slider(
    label='圖片張數',
    minimum=1,
    maximum=10,
    step=1,
    value=1
    )
iface=gr.Interface(
    fn=handler,
    inputs=[api_key, prompt, model_sel, size_sel, image_count],  
    outputs=[
        gr.Gallery(label='生成的圖片'),
        gr.Textbox(label='狀態訊息', interactive=False)
        ],
    title='OpenAI Image API 測試',
    flagging_mode='never'
    )
iface.launch()