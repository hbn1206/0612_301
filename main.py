import streamlit as st

st.set_page_config(page_title="화폐의 현재가치 실습", layout="wide")

st.markdown("""
<div style='background-color:#e0d1eb; padding: 10px; border-radius: 10px; text-align:center; font-size:30px; font-weight:bold;'>
    화폐의 현재가치 실습 해보기
</div>
""", unsafe_allow_html=True)

st.markdown("## 화폐의 현재가치 계산")

col1, col2 = st.columns([1, 1.5])

with col1:
    st.markdown("### 입력변수")
    future_value = st.number_input("미래가치", value=10000000, step=100000, format="%d")
    years = st.number_input("기간(년)", value=4, step=1, format="%d")
    rate = st.number_input("이자율(%)", value=5.00, step=0.1, format="%.2f")

    # 현재가치 계산
    present_value = future_value / ((1 + rate / 100) ** years)

    st.markdown("### 출력변수")
    st.markdown(f"""
    <div style='background-color:#e0d1eb; padding:15px; border-radius:8px; font-size:28px; font-weight:bold;'>
        현재가치: <span style='color:#2123aa;'>{present_value:,.0f} 원</span>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <br>
    <ul>
        <li>미래가치: 미래 특정 시점의 일정 금액 (단위: 원)</li>
        <li>기간: 현재 시점과 미래 시점 사이의 기간 (단위: 년)</li>
        <li>이자율: 연 이자율 (단위: %)</li>
        <br>
        <li style='color:#be1e1e;'>현재가치: 미래 특정 시점의 일정금액을 현재 시점의 가치로 환산한 금액 (단위: 원)</li>
    </ul>
    """, unsafe_allow_html=True)

    st.markdown(f"<span style='color:#be1e1e;'>{present_value:,.0f}</span> : 미래 특정 시점의 일정금액을 현재 시점의 가치로 환산한 금액 (단위: 원)", unsafe_allow_html=True)
