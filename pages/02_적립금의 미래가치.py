import streamlit as st

st.set_page_config(page_title="적립금의 미래가치 계산", layout="centered")

# 스타일 지정 (입력/출력 파트 파란색, 결과값 진한 파랑)
st.markdown("""
<style>
.pv-table {
    width: 520px;
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
    font-size: 27px;
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
    width: 150px;
}
.pv-table .input-value {
    color: #e30000;
    font-weight: bold;
    font-size: 26px;
    text-align: right;
    background: #fff;
    width: 200px;
}
.pv-table .output-value {
    color: #0866ad;
    font-weight: bold;
    font-size: 29px;
    text-align: right;
    background: #91d0f5;
}
.pv-table .output-sum {
    color: #222;
    font-weight: bold;
    font-size: 27px;
    text-align: right;
    background: #e6f4fa;
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
deposit = st.number_input('적립금', value=10000000, step=100000, format="%d")
period = st.number_input('적립기간', value=40, step=1, format="%d")
rate = st.number_input('이자율', value=4.00, step=0.1, format="%.2f")

# 적립금 합계 및 미래가치 계산 (매년말 정기불입, 연이율)
deposit_sum = deposit * period
if rate != 0:
    fv = deposit * (((1 + rate / 100) ** period - 1) / (rate / 100))
else:
    fv = deposit_sum

# 표 출력 (입력/출력 변수명, 색상, 순서 이미지와 동일)
st.markdown(f"""
<table class="pv-table">
    <tr>
        <th colspan="2">적립금의 미래가치(은퇴 시점 적립금의 원리금 합계) 계산</th>
    </tr>
    <tr>
        <td class="input-title" colspan="2">입력변수</td>
    </tr>
    <tr>
        <td class="input-label">적립금</td>
        <td class="input-value">{deposit:,.0f} <span class="unit">원</span></td>
    </tr>
    <tr>
        <td class="input-label">적립기간</td>
        <td class="input-value">{period}</td>
    </tr>
    <tr>
        <td class="input-label">이자율</td>
        <td class="input-value">{rate:.2f}%</td>
    </tr>
    <tr>
        <td class="output-title" colspan="2">출력변수</td>
    </tr>
    <tr>
        <td class="input-label">적립금 합계</td>
        <td class="output-sum">{deposit_sum:,.0f} <span class="unit">원</span></td>
    </tr>
    <tr>
        <td class="input-label">적립금 미래가치</td>
        <td class="output-value">{fv:,.0f} <span class="unit">원</span></td>
    </tr>
</table>
""", unsafe_allow_html=True)

# 변수 설명 (이미지와 동일하게)
st.markdown(f"""
---
### 🔎 변수 설명

- 💰 **적립금**: 매년말 정기적으로 불입하는 금액 (단위: 원)
- ⏳ **적립기간**: 적립 기간 (단위: 년)
- 💹 **이자율**: 연 이자율 (단위: %)

- 🔲 <b>적립금 합계</b>: 정기적으로 불입한 적립금 현금흐름의 합계 (단위: 원)
- 🔷 <b>적립금 미래가치</b>: 정기적으로 불입한 적립금 현금흐름의 은퇴시점의 가치 (단위: 원)
""", unsafe_allow_html=True)
