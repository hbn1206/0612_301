import streamlit as st

st.set_page_config(page_title="연금의 현재가치 실습 해보기", layout="wide")

# ---- 입력 ----
annuity = st.number_input("연금", value=40000000, step=100000, format="%d")
n_years = st.number_input("지급기간", value=30, step=1, format="%d")
rate = st.number_input("이자율", value=5.00, step=0.1, format="%.2f")

# ---- 계산 ----
annuity_sum = annuity * n_years
if rate != 0:
    pv = annuity * (1 - (1 + rate / 100) ** (-n_years)) / (rate / 100)
else:
    pv = annuity_sum

# ---- 표 및 스타일 ----
st.markdown("""
<style>
.npv-header {
    width: 880px;
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
.npv-table {
    width: 670px;
    border-collapse: collapse;
    font-size: 25px;
    font-family: "Pretendard", "Malgun Gothic", "맑은 고딕", Arial, sans-serif;
}
.npv-table th, .npv-table td {
    border: 2.2px solid #000;
    padding: 8px 18px;
    text-align: left;
    height: 40px;
}
.npv-table th {
    background: #fad2d6;
    color: #23132b;
    text-align: center;
    font-size: 27px;
    font-weight: bold;
    letter-spacing: 1px;
}
.npv-table .input-title, .npv-table .output-title {
    background: #f6f6f6;
    color: #222;
    font-size: 19px;
    font-weight: bold;
    border-right: none;
    text-align: left;
}
.npv-table .output-title {
    border-top: 2.2px solid #000;
}
.npv-table .input-label {
    font-size: 22px;
    font-weight: bold;
    background: #fff;
    width: 210px;
}
.npv-table .input-value {
    color: #e30000;
    font-weight: bold;
    font-size: 25px;
    text-align: right;
    background: #fff;
    width: 220px;
}
.npv-table .output-value {
    color: #23132b;
    font-weight: bold;
    font-size: 27px;
    text-align: right;
    background: #fad2d6;
}
.npv-table .output-sum {
    color: #23132b;
    font-weight: bold;
    font-size: 27px;
    text-align: right;
    background: #f6f6f6;
}
.npv-table .unit {
    color: #444;
    font-size: 17px;
    font-weight: normal;
    padding-left: 3px;
}
</style>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1.37,1.0])

with col1:
    st.markdown('<div class="npv-header">연금의 현재가치 실습 해보기</div>', unsafe_allow_html=True)
    st.markdown(f"""
    <table class="npv-table">
        <tr>
            <th colspan="3">연금의 현재가치 계산</th>
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
            <td class="input-label">연금 합계</td>
            <td class="output-sum">{annuity_sum:,.0f}</td>
            <td class="unit">원</td>
        </tr>
        <tr>
            <td class="input-label">연금 현재가치</td>
            <td class="output-value">{pv:,.0f}</td>
            <td class="unit">원</td>
        </tr>
    </table>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <br>
    <hr style="margin-top:16px; margin-bottom:12px; border:1px solid #eee;">
    <h3 style="font-size: 23px;">✨ 변수 설명</h3>
    <ul style="font-size: 19px;">
      <li>💸 <b>연금</b> : 은퇴 이후 매년 정기적으로 지급 받는 연금 금액<br><span style='color:#888;'>(단위: 원)</span></li>
      <li>📅 <b>지급기간</b> : 은퇴 이후 연금 지급 기간<br><span style='color:#888;'>(단위: 년)</span></li>
      <li>🟢 <b>이자율</b> : 연 이자율<br><span style='color:#888;'>(단위: %)</span></li>
      <li>🧮 <b>연금 합계</b> : 은퇴 이후 매년 정기적으로 지급 받는 연금 현금흐름의 합계<br><span style='color:#888;'>(단위: 원)</span></li>
      <li>💎 <b>연금 현재가치</b> : 은퇴 이후 매년 정기적으로 지급 받는 연금 현금흐름의 은퇴시점의 가치<br><span style='color:#888;'>(단위: 원)</span></li>
    </ul>
    """, unsafe_allow_html=True)
