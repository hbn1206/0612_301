import streamlit as st

st.set_page_config(page_title="연금액 산출 실습", layout="centered")

# 스타일 지정 (연분홍 강조, 결과값은 진한 분홍)
st.markdown("""
<style>
.pv-table {
    width: 570px;
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
    background: #fad2d6;
    color: #23132b;
    text-align: center;
    font-size: 27px;
    font-weight: bold;
}
.pv-table .input-title, .pv-table .output-title {
    background: #f6f6f6;
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
    background: #fff4f6;
    width: 180px;
}
.pv-table .input-value {
    color: #e30000;
    font-weight: bold;
    font-size: 26px;
    text-align: right;
    background: #fff;
    width: 210px;
}
.pv-table .output-value {
    color: #c72e4b;
    font-weight: bold;
    font-size: 29px;
    text-align: right;
    background: #fad2d6;
}
.pv-table .unit {
    color: #444;
    font-size: 18px;
    font-weight: normal;
    padding-left: 3px;
}
</style>
""", unsafe_allow_html=True)

# 값 입력 및 계산
pv = st.number_input('연금 현가치', value=950255157, step=1000000, format="%d")
n_years = st.number_input('지급기간', value=30, step=1, format="%d")
rate = st.number_input('이자율', value=4.00, step=0.1, format="%.2f")

# 연금 지급액 계산 (연금 PV 공식)
if rate != 0:
    pension = pv * (rate / 100) / (1 - (1 + rate / 100) ** (-n_years))
else:
    pension = pv / n_years

# 표 출력 (입력/출력 변수, 색상, 순서 이미지와 동일)
st.markdown(f"""
<table class="pv-table">
    <tr>
        <th colspan="2">연금의 현재가치(=적립금 미래가치)를 사용하여 연금 계산</th>
    </tr>
    <tr>
        <td class="input-title" colspan="2">입력변수</td>
    </tr>
    <tr>
        <td class="input-label">연금 현재가치</td>
        <td class="input-value">{pv:,.0f} <span class="unit">원</span></td>
    </tr>
    <tr>
        <td class="input-label">지급기간</td>
        <td class="input-value">{n_years}</td>
    </tr>
    <tr>
        <td class="input-label">이자율</td>
        <td class="input-value">{rate:.2f}%</td>
    </tr>
    <tr>
        <td class="output-title" colspan="2">출력변수</td>
    </tr>
    <tr>
        <td class="input-label">연금</td>
        <td class="output-value">{pension:,.0f} <span class="unit">원</span></td>
    </tr>
</table>
""", unsafe_allow_html=True)

# 변수 설명 (이미지와 동일)
st.markdown(f"""
---
### 🔎 변수 설명

- 🏦 **연금 현재가치**: 은퇴 이후 매년 정기적으로 지급 받는 연금 현금흐름의 은퇴시점의 가치 (단위: 원)
- ⏳ **지급기간**: 은퇴 이후 연금 수령 기간 (단위: 년)
- 💹 **이자율**: 연 이자율 (단위: %)

- 💴 <b>연금</b>: 은퇴 이후 매년 정기적으로 수령하는 연금액 (단위: 원)
""", unsafe_allow_html=True)
