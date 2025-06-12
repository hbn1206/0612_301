import streamlit as st

st.set_page_config(page_title="100세 시대를 대비한 재무설계", layout="centered")

# 배경 이미지 CSS
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("https://raw.githubusercontent.com/yourrepo/yourpath/yourimg.png");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    .block-container {{
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        margin: 0 auto !important;
        max-width: 100vw !important;
    }}
    header, footer {{visibility: hidden;}}
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit 화면에는 빈 공간만 출력
st.write("")
