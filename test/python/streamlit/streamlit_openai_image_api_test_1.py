# streamlit_openai_image_api_test_1.py
import streamlit as st
from openai import OpenAI

# 生圖主函式
def generate_images(prompt, api_key, **kwargs):
    client=OpenAI(api_key=api_key)
    replies=client.images.generate(prompt=prompt, **kwargs)
    return [item.url for item in replies.data]

# UI 開始
st.set_page_config(page_title='OpenAI Image API 測試', layout='wide')
st.markdown('## 🎨 使用 DALL·E 2 / 3 生圖')
# 輸入金鑰與提示詞
api_key=st.text_input('請輸入金鑰 (API key)', type='password')
prompt=st.text_area('請輸入提示詞 (Prompt)', height=100)
# 圖片尺寸選項
size_options={
    'dall-e-2': ['256x256', '512x512', '1024x1024'],
    'dall-e-3': ['1024x1024', '1024x1792', '1792x1024']
    }
# 初始化 session 狀態
if 'model_sel' not in st.session_state:
    st.session_state.model_sel='dall-e-3'
if 'size_sel' not in st.session_state:
    st.session_state.size_sel=size_options['dall-e-3'][0]
# 模型選單（更新尺寸選單）
model=st.radio(
    '選擇模型',
    ['dall-e-2', 'dall-e-3'],
    index=['dall-e-2', 'dall-e-3'].index(st.session_state.model_sel)
    )
if model != st.session_state.model_sel:
    st.session_state.model_sel=model
    st.session_state.size_sel=size_options[model][0]
# 尺寸選單（依模型變化）
size_sel=st.radio(
    '選擇圖片尺寸',
    size_options[st.session_state.model_sel],
    index=size_options[st.session_state.model_sel].index(st.session_state.size_sel)
    )
st.session_state.size_sel=size_sel
# 圖片張數（僅限 dall-e-2）
image_count=1
if st.session_state.model_sel == 'dall-e-2':
    image_count=st.slider('圖片張數 (DALL·E 2 專用)', 1, 10, value=1)
sel_msg=f'模型: {st.session_state.model_sel} 尺寸: {st.session_state.size_sel}'
st.write(sel_msg)
# 按送出按鈕開始生成圖片
if st.button('開始生成', type='primary'):
    if not api_key.strip():  # 提醒必須輸入金鑰
        st.warning('⚠ 請輸入 OpenAI API Key')
    elif not prompt.strip():  # 提醒必須輸入提示詞
        st.warning('⚠️ 請輸入提示詞 (Prompt)')
    else:
        n=image_count if st.session_state.model_sel == 'dall-e-2' else 1
        with st.spinner('生成圖片中...'):
            try:
                urls=generate_images(prompt, api_key, model=st.session_state.model_sel, size=st.session_state.size_sel, n=n)
                st.success(f'✅ 成功產生 {len(urls)} 張圖片。')
                st.markdown(f'**模型**: {st.session_state.model_sel} **尺寸**: {st.session_state.size_sel} **張數**: {n}')
                cols=st.columns(min(len(urls), 3))
                for i, url in enumerate(urls):
                    with cols[i % len(cols)]:
                        st.image(url)
            except Exception as e:
                st.error(f'❌ 發生錯誤：{e}')
