import streamlit as st

st.set_page_config(page_title="민감도 분석 실습 해보기", layout="wide")

# 스타일 지정
st.markdown("""
<style>
.top-header {
    width: 870px;
    margin: 0 auto 0.7em auto;
    background: #efefef;
    border: 3px solid #000;
    border-radius: 2px;
    text-align: center;
    font-size: 2.3em;
    font-weight: bold;
    letter-spacing: 2px;
    padding: 12px 0 10px 0;
}
.pv-table {
    width: 610px;
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
    background: #c6efb3;
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
    background: #f9f9f9;
    width: 160px;
}
.pv-table .input-value {
    color: #e30000;
    font-weight: bold;
    font-size: 26px;
    text-align: right;
    background: #fff;
    width: 220px;
}
.pv-table .output-value {
    color: #22490b;
    font-weight: bold;
    font-size: 29px;
    text-align: right;
    background: #c6efb3;
}
.pv-table .unit {
    color: #444;
    font-size: 18px;
    font-weight: normal;
    padding-left: 3px;
}
.pv-table .note-row {
    background: #e2f0d9;
    font-size: 21px;
    font-weight: bold;
    color: #111;
    text-align: center;
}
.pv-table .note-value {
    font-size: 23px;
    color: #222;
    font-weight: bold;
    text-align: right;
    background: #fff;
}
</style>
""", unsafe_allow_html=True)

# 입력 및 계산
deposit = st.number_input('적립금', value=10000000, step=100000, format="%d")
save_period = st.number_input('적립기간', value=40, step=1, format="%d")
pay_period = st.number_input('지급기간', value=30, step=1, format="%d")
rate = st.number_input('이자율', value=4.00, step=0.1, format="%.2f")

# 적립금 미래가치 계산 (매년말 불입)
if rate != 0:
    future_value = deposit * (((1 + rate / 100) ** save_period - 1) / (rate / 100))
else:
    future_value = deposit * save_period

# 연금액 계산 (이미지와 같은 방식)
if rate != 0:
    pension = future_value * (rate / 100) / (1 - (1 + rate / 100) ** (-pay_period))
else:
    pension = future_value / pay_period

col1, col2 = st.columns([1.35,1.05])

with col1:
    st.markdown('<div class="top-header">민감도 분석 실습 해보기</div>', unsafe_allow_html=True)
    st.markdown(f"""
    <table class="pv-table">
        <tr>
            <th colspan="2">입력변수 변화에 따른 연금 변화 계산</th>
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
            <td class="input-value">{save_period}</td>
        </tr>
        <tr>
            <td class="input-label">지급기간</td>
            <td class="input-value">{pay_period}</td>
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
        <tr>
            <td class="note-row" colspan="1">참고</td>
            <td class="note-value">
                적립금 미래가치(은퇴시점) = 연금 현재가치(은퇴시점)<br>
                <span style='font-size:25px;font-weight:bold'>{future_value:,.0f}</span>
            </td>
        </tr>
    </table>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="font-size:18px; line-height:2.0; margin-top:30px;">
    은퇴 이전 매년 정기적으로 불입하는 적립금액 (단위: 원)<br><br>
    정기 적립금 불입 기간 (단위: 년)<br><br>
    은퇴 이후 연금 수령 기간 (단위: 년)<br><br>
    연 이자율 (단위: %)<br><br><br>
    은퇴 이후 매년 정기적으로 수령하는 연금금액 (단위: 원)
    </div>
    """, unsafe_allow_html=True)
