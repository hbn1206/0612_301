import streamlit as st

st.set_page_config(page_title="민감도 분석 실습: 적립금 산출", layout="centered")

# --------- 입력 ---------
annuity = st.number_input("연금", value=40000000, step=100000, format="%d")
save_period = st.number_input("적립기간", value=30, step=1, format="%d")
pay_period = st.number_input("지급기간", value=30, step=1, format="%d")
rate = st.number_input("이자율", value=5.00, step=0.1, format="%.2f")

# --------- 계산 ---------
# 은퇴시점의 연금 현재가치(적립금 미래가치)
if rate != 0:
    fv = annuity * (1 - (1 + rate / 100) ** (-pay_period)) / (rate / 100)
else:
    fv = annuity * pay_period

# 적립금 = 미래가치 × r / ((1+r)^n - 1)
if rate != 0 and save_period != 0:
    deposit = fv * (rate / 100) / ((1 + rate / 100) ** save_period - 1)
else:
    deposit = 0

# --------- 표 스타일 ---------
st.markdown("""
<style>
.sense-header {
    width: 870px;
    margin: 0 auto 0.7em auto;
    background: #efefef;
    border: 3px solid #000;
    border-radius: 2px;
    text-align: center;
    font-size: 2.3em;
    font-weight: bold;
    letter-spacing: 2px;
    padding: 13px 0 10px 0;
}
.sense-table {
    width: 770px;
    border-collapse: collapse;
    margin-top: 22px;
    font-size: 25px;
    font-family: "Pretendard", "Malgun Gothic", "맑은 고딕", Arial, sans-serif;
    box-shadow: 0 4px 16px #e9e9e950;
}
.sense-table th, .sense-table td {
    border: 2.2px solid #000;
    padding: 8px 18px;
    text-align: left;
    height: 40px;
}
.sense-table .top-title {
    background: #ffd6ba;
    color: #23132b;
    text-align: center;
    font-size: 1.14em;
    font-weight: bold;
    letter-spacing: 1px;
}
.sense-table .input-title, .sense-table .output-title {
    background: #f6f6f6;
    color: #222;
    font-size: 19px;
    font-weight: bold;
    border-right: none;
    text-align: left;
}
.sense-table .output-title {
    border-top: 2.2px solid #000;
}
.sense-table .input-label {
    font-size: 22px;
    font-weight: bold;
    background: #fff;
    width: 230px;
}
.sense-table .input-value {
    color: #e30000;
    font-weight: bold;
    font-size: 25px;
    text-align: right;
    background: #fff;
    width: 210px;
}
.sense-table .output-value {
    color: #c15412;
    font-weight: bold;
    font-size: 28px;
    text-align: right;
    background: #ffd6ba;
}
.sense-table .unit {
    color: #444;
    font-size: 17px;
    font-weight: normal;
    padding-left: 3px;
}
.sense-table .note-row {
    background: #ffede0;
    font-size: 21px;
    font-weight: bold;
    color: #111;
    text-align: center;
}
.sense-table .note-value {
    font-size: 23px;
    color: #222;
    font-weight: bold;
    text-align: right;
    background: #fff;
}
</style>
""", unsafe_allow_html=True)

# --------- 표 출력 ---------
st.markdown('<div class="sense-header">민감도 분석 실습 해보기</div>', unsafe_allow_html=True)
st.markdown(f"""
<table class="sense-table">
    <tr>
        <th class="top-title" colspan="3">입력변수 변화에 따른 적립금 계산</th>
    </tr>
    <tr>
        <td class="input-title" colspan="3">입력변수</td>
    </tr>
    <tr>
        <td class="input-label">연금</td>
        <td class="input-value">{annuity:,.0f}</td>
        <td class="unit">원</td>
    </tr>
    <tr>
        <td class="input-label">적립기간</td>
        <td class="input-value">{save_period}</td>
        <td class="unit"></td>
    </tr>
    <tr>
        <td class="input-label">지급기간</td>
        <td class="input-value">{pay_period}</td>
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
        <td class="input-label">적립금</td>
        <td class="output-value">{deposit:,.0f}</td>
        <td class="unit">원</td>
    </tr>
    <tr>
        <td class="note-row" colspan="1">참고</td>
        <td class="note-value" colspan="2">
            적립금 미래가치(은퇴시점) = 연금 현재가치(은퇴시점)
            <span style='font-size:25px;font-weight:bold'> {fv:,.0f} </span>
        </td>
    </tr>
</table>
""", unsafe_allow_html=True)

# --------- 변수 설명(맨 아래) ---------
st.markdown("""
<br>
<hr style="margin-top:36px; margin-bottom:16px; border:1px solid #eee;">
<h3 style="font-size: 23px;">📝 변수 설명</h3>
<ul style="font-size: 19px;">
  <li>💸 <b>연금</b>: 은퇴 이후 매년 정기적으로 수령하는 연금액 (단위: 원)</li>
  <li>📅 <b>적립기간</b>: 정기 적립금 불입 기간 (단위: 년)</li>
  <li>⏳ <b>지급기간</b>: 은퇴 이후 연금 수령 기간 (단위: 년)</li>
  <li>🟢 <b>이자율</b>: 연 이자율 (단위: %)</li>
  <li>💰 <b>적립금</b>: 매년말 정기적으로 불입해야 하는 금액 (단위: 원)</li>
  <li>💎 <b>적립금 미래가치</b>: 정기적으로 불입한 적립금 현금흐름의 은퇴시점의 가치(=연금 현재가치, 단위: 원)</li>
</ul>
""", unsafe_allow_html=True)
