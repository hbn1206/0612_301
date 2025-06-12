import streamlit as st

st.set_page_config(page_title="연금 계산 실습", layout="centered")

# ---- 값 입력 (기본 number_input 사용) ----
pv = st.number_input("연금 현가치", value=560849378, step=1000000, format="%d")
n_years = st.number_input("지급기간", value=30, step=1, format="%d")
rate = st.number_input("이자율", value=4.00, step=0.1, format="%.2f")

# ---- 연금액 계산 ----
if rate != 0:
    pension = pv * (rate / 100) / (1 - (1 + rate / 100) ** (-n_years))
else:
    pension = pv / n_years

# ---- 표 스타일 지정 ----
st.markdown("""
<style>
.annuity-table {
    width: 700px;
    border-collapse: collapse;
    margin-top: 18px;
    font-size: 22px;
    font-family: "Pretendard", "Malgun Gothic", "맑은 고딕", Arial, sans-serif;
    box-shadow: 0 4px 16px #e9e9e960;
}
.annuity-table th, .annuity-table td {
    border: 2.2px solid #000;
    padding: 8px 18px;
    text-align: left;
    height: 40px;
}
.annuity-table .top-title {
    background: #fad2d6;
    color: #23132b;
    text-align: center;
    font-size: 27px;
    font-weight: bold;
    letter-spacing: 0.5px;
}
.annuity-table .input-title, .annuity-table .output-title {
    background: #f6f6f6;
    color: #222;
    font-size: 18px;
    font-weight: bold;
    border-right: none;
    text-align: left;
}
.annuity-table .output-title {
    border-top: 2.2px solid #000;
}
.annuity-table .input-label {
    font-size: 22px;
    font-weight: bold;
    background: #fff;
    width: 230px;
}
.annuity-table .input-value {
    color: #e30000;
    font-weight: bold;
    font-size: 25px;
    text-align: right;
    background: #fff;
    width: 210px;
}
.annuity-table .output-value {
    color: #c72e4b;
    font-weight: bold;
    font-size: 28px;
    text-align: right;
    background: #fad2d6;
}
.annuity-table .unit {
    color: #444;
    font-size: 17px;
    font-weight: normal;
    padding-left: 3px;
}
</style>
""", unsafe_allow_html=True)

# ---- 표 출력 ----
st.markdown(f"""
<table class="annuity-table">
    <tr>
        <th class="top-title" colspan="3">
            연금의 현재가치(=적립금 미래가치)를 사용하여 연금 계산
        </th>
    </tr>
    <tr>
        <td class="input-title" colspan="3">입력변수</td>
    </tr>
    <tr>
        <td class="input-label">연금 현재가치</td>
        <td class="input-value">{pv:,.0f}</td>
        <td class="unit">원</td>
    </tr>
    <tr>
        <td class="input-label">지급기간</td>
        <td class="input-value">{n_years}</td>
        <td class="unit"></td>
    </tr>
    <tr>
        <td class="input-label">이자율</td>
        <td class="input-value">{rate:.2f}%</td>
        <td class="unit"></td>
    </tr>
    <tr>
        <td class="output-title" colspan="3">출력변수</td>
    </tr>
    <tr>
        <td class="input-label">연금</td>
        <td class="output-value">{pension:,.0f}</td>
        <td class="unit">원</td>
    </tr>
</table>
""", unsafe_allow_html=True)

# ---- 변수설명 (이모지 포함) ----
st.markdown("""
<br>
<hr style="margin-top:40px; margin-bottom:16px; border:1px solid #eee;">
<h3 style="font-size: 23px;">🔍 변수 설명</h3>
<ul style="font-size: 19px;">
  <li>🏠 <b>연금 현재가치</b>: 은퇴 이후 매년 정기적으로 지급 받는 연금 현금흐름의 은퇴시점의 가치 (단위: 원)</li>
  <li>⏳ <b>지급기간</b>: 은퇴 이후 연금 수령 기간 (단위: 년)</li>
  <li>🟩 <b>이자율</b>: 연 이자율 (단위: %)</li>
  <li>💵 <b>연금</b>: 은퇴 이후 매년 정기적으로 수령하는 연금액 (단위: 원)</li>
</ul>
""", unsafe_allow_html=True)
