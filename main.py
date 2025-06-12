import streamlit as st

st.set_page_config(page_title="100세 시대를 대비한 재무설계", layout="wide")

# CSS로 상단 배너, 표 스타일, 폰트 지정
st.markdown("""
    <style>
    body {
        background-color: #ece6f6;
    }
    .top-banner {
        background: linear-gradient(120deg, #a086be 90%, #ede4f5 100%);
        padding: 12px 0 0 0;
        margin-bottom: 12px;
        border-radius: 0 0 32px 32px;
        text-align: left;
        position: relative;
    }
    .main-title {
        font-family: 'Pretendard', sans-serif;
        font-size: 48px;
        font-weight: 900;
        color: #2b2232;
        padding-left: 32px;
        letter-spacing: 1px;
        margin-bottom: 0;
        display: inline-block;
        vertical-align: middle;
    }
    .piggy-img {
        position: absolute;
        right: 50px;
        top: 12px;
        width: 70px;
    }
    .subtitle-box {
        background: #f6f6fa;
        border: 3px solid #bbb;
        padding: 16px;
        border-radius: 8px;
        margin-top: 16px;
        margin-bottom: 16px;
        text-align: center;
        font-size: 32px;
        font-weight: 600;
        color: #222;
        letter-spacing: 4px;
    }
    .main-table {
        background: #f2daf9;
        border-radius: 7px;
        border: 2.5px solid #bca7cc;
        font-size: 22px;
        width: 98%;
        margin: 0;
    }
    .main-table th {
        background: #e5c5ec;
        color: #1d132b;
        font-size: 26px;
        font-weight: 900;
        border-bottom: 2.5px solid #8c659c;
        text-align: center;
    }
    .main-table td {
        border-bottom: 1.5px solid #e0c2eb;
        padding: 6px 8px 6px 18px;
        background: #fff0ff;
        font-size: 22px;
        color: #171222;
        font-weight: 700;
    }
    .input-label {
        color: #000;
        font-weight: 900;
        font-size: 23px;
        padding-right: 4px;
    }
    .input-value {
        color: #e40000;
        font-weight: 900;
        font-size: 27px;
        padding-left: 10px;
        letter-spacing: 2px;
    }
    .output-label {
        color: #222;
        font-weight: 900;
        font-size: 23px;
        padding-right: 4px;
    }
    .output-value {
        color: #2a106a;
        font-weight: 900;
        font-size: 30px;
        padding-left: 10px;
        letter-spacing: 2px;
        background: #f6e0fa;
        border-radius: 7px;
        display: inline-block;
    }
    </style>
""", unsafe_allow_html=True)

# 상단 배너
st.markdown("""
<div class="top-banner">
    <span class="main-title">100세 시대를 대비한 재무설계</span>
    <img src="https://em-content.zobj.net/source/microsoft-teams/363/piggy-bank_1f4b3.png" class="piggy-img">
</div>
""", unsafe_allow_html=True)

# 중간 제목 박스
st.markdown("""
<div class="subtitle-box">
    화폐의 현재가치 실습 해보기
</div>
""", unsafe_allow_html=True)

# 표 입력 및 계산
col1, col2 = st.columns([1.1, 1.3])

with col1:
    st.markdown("""
    <table class="main-table">
        <tr>
            <th colspan="2">화폐의 현재가치 계산</th>
        </tr>
        <tr><td colspan="2" style="background:#f6e9fa; font-size:19px; color:#333; font-weight:700;">입력변수</td></tr>
        <tr>
            <td class="input-label">미래가치</td>
            <td>
    """, unsafe_allow_html=True)
    future_value = st.number_input("", value=10000000, step=100000, format="%d", key="future_value")
    st.markdown(f'<span class="input-value">{future_value:,.0f}</span>', unsafe_allow_html=True)
    st.markdown("""
            </td>
        </tr>
        <tr>
            <td class="input-label">기간</td>
            <td>
    """, unsafe_allow_html=True)
    years = st.number_input("", value=7, step=1, format="%d", key="years")
    st.markdown(f'<span class="input-value">{years}</span>', unsafe_allow_html=True)
    st.markdown("""
            </td>
        </tr>
        <tr>
            <td class="input-label">이자율</td>
            <td>
    """, unsafe_allow_html=True)
    rate = st.number_input("", value=5.00, step=0.1, format="%.2f", key="rate")
    st.markdown(f'<span class="input-value">{rate:.2f}%</span>', unsafe_allow_html=True)
    st.markdown("""
            </td>
        </tr>
        <tr><td colspan="2" style="background:#f6e9fa; font-size:19px; color:#333; font-weight:700;">출력변수</td></tr>
        <tr>
            <td class="output-label">현재가치</td>
            <td>
    """, unsafe_allow_html=True)
    present_value = future_value / ((1 + rate / 100) ** years)
    st.markdown(f'<span class="output-value">{present_value:,.0f}</span>', unsafe_allow_html=True)
    st.markdown("""
            </td>
        </tr>
    </table>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <br>
    <div style="font-size:20px; line-height:2.1; font-weight:600;">
      <span>💸 <b>미래가치</b>: 미래 특정 시점의 일정 금액<br>
      <span>⏳ <b>기간</b>: 현재 시점과 미래 시점 사이의 기간 (년)<br>
      <span>💹 <b>이자율</b>: 연 이자율 (%)<br>
      <span style="color:#9e1c2c; font-size:22px;">🏦 <b>현재가치</b>: 미래 일정금액을 현재 시점 가치로 환산한 금액 (원)</span>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"""
    <span style='color:#be1e1e; font-size:17px; font-weight:900;'>{present_value:,.0f}</span> : 미래 특정 시점의 일정금액을 현재 시점의 가치로 환산한 금액 (단위: 원)
    """, unsafe_allow_html=True)

# 하단 보라색 배경
st.markdown("""
    <div style="height:22px; background: linear-gradient(120deg, #a086be 90%, #ede4f5 100%); border-radius: 0 0 20px 20px; margin-top:32px;"></div>
""", unsafe_allow_html=True)
