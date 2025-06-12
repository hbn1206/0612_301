import streamlit as st

st.set_page_config(page_title="화폐의 미래가치 계산", layout="centered")

# 스타일 지정 (입력/출력 변수 블루, 결과값 진한 파랑)
st.markdown("""
<style>
.pv-table {
    width: 410px;
    border-collapse: collapse;
    font-size: 25px;
    font-family: "Pretendard", "Malgun Gothic", "맑은 고딕", Arial, sans-serif;
}
.pv-table th, .pv-table td {
    border: 2.2px solid #000;
    padding: 6px 16px;
    text-align: left;
    height: 38px;
}
.pv-table th {
    background: #91d0f5;
    color: #23132b;
    text-align: center;
    font-size: 28px;
    font-weight: bold;
}
.pv-table .input-title, .pv-table .output-title {
    background: #e6f4fa;
    color: #222;
    font-size: 19px;
    font-weight: bold;
    border-right: none;
}
.pv-table .output-title {
    border-top: 2.2px solid #000;
}
.pv-table .input-label {
    font-size: 25px;
    font-weight: bold;
    background: #f9f9f9;
    width: 120px;
}
.pv-table .input-value {
    color: #e30000;
    font-weight: bold;
    font-size: 26px;
    text-align: right;
    background: #fff;
    width: 170px;
}
.pv-table .output-value {
    color: #0866ad;
    font-weight: bold;
    font-size: 29px;
    text-align: right;
    background: #91d0f5;
}
.pv-table .unit {
    color: #444;
    font-size: 18px;
    font-weight: normal;
    padding-left: 3px;
}
</style>
""", unsafe_allow_html=True)

# 값 입력 및 계산 (미래가치 계산: 현재가치 × (1 + 이자율/100)^기간)
present_value = st.number_input('현재가치', value=10000000, step=100000, format="%d")
years = st.number_input('기간', value=4, step=1, format="%d")
rate = st.number_input('이자율', value=5.00, step=0.1, format="%.2f")
future_value = present_value * ((1 + rate / 100) ** years)

# 표 출력 (입력/출력 변수, 색상 및 레이블 이미지와 동일하게)
st.markdown(f"""
<table class="pv-table">
    <tr>
        <th colspan="2">화폐의 미래가치 계산</th>
    </tr>
    <tr>
        <td class="input-title" colspan="2">입력변수</td>
    </tr>
    <tr>
        <td class="input-label">현재가치</td>
        <td class="input-value">{present_value:,.0f} <span class="unit">원</span></td>
    </tr>
    <tr>
        <td class="input-label">기간</td>
        <td class="input-value">{years}</td>
    </tr>
    <tr>
        <td class="input-label">이자율</td>
        <td class="input-value">{rate:.2f}%</td>
    </tr>
    <tr>
        <td class="output-title" colspan="2">출력변수</td>
    </tr>
    <tr>
        <td class="input-label">미래가치</td>
        <td class="output-value">{future_value:,.0f} <span class="unit">원</span></td>
    </tr>
</table>
""", unsafe_allow_html=True)

# 변수 설명 (이미지와 동일)
st.markdown("""
---
### 🔎 변수 설명

- 💵 **현재가치**: 현재 시점의 일정 금액 (단위: 원)
- ⏳ **기간**: 현재 시점과 미래 시점 사이의 기간 (단위: 년)
- 💹 **이자율**: 연 이자율 (단위: %)

- 🔷 <b>미래가치</b>: 현재 시점의 일정 금액을 미래 특정 시점의 가치로 환산한 금액 (단위: 원)
""", unsafe_allow_html=True)
