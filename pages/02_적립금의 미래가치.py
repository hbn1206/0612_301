import streamlit as st

st.set_page_config(page_title="적립금의 미래가치 실습", layout="wide")

# --- 스타일 ---
st.markdown("""
<style>
.sv-header {
    width: 850px;
    margin: 0 auto 0.7em auto;
    background: #efefef;
    border: 3px solid #000;
    border-radius: 2px;
    text-align: center;
    font-size: 2.5em;
    font-weight: bold;
    letter-spacing: 2px;
    padding: 13px 0 10px 0;
}
.sv-table {
    width: 640px;
    border-collapse: collapse;
    font-size: 25px;
    font-family: "Pretendard", "Malgun Gothic", "맑은 고딕", Arial, sans-serif;
}
.sv-table th, .sv-table td {
    border: 2.2px solid #000;
    padding: 6px 16px;
    text-align: left;
    height: 38px;
}
.sv-table th {
    background: #91d0f5;
    color: #23132b;
    text-align: center;
    font-size: 27px;
    font-weight: bold;
}
.sv-table .input-title, .sv-table .output-title {
    background: #e6f4fa;
    color: #222;
    font-size: 19px;
    font-weight: bold;
    border-right: none;
}
.sv-table .output-title {
    border-top: 2.2px solid #000;
}
.sv-table .input-label {
    font-size: 25px;
    font-weight: bold;
    background: #f9f9f9;
    width: 170px;
}
.sv-table .input-value {
    color: #e30000;
    font-weight: bold;
    font-size: 26px;
    text-align: right;
    background: #fff;
    width: 250px;
}
.sv-table .output-value {
    color: #0866ad;
    font-weight: bold;
    font-size: 29px;
    text-align: right;
    background: #91d0f5;
}
.sv-table .output-sum {
    color: #222;
    font-weight: bold;
    font-size: 27px;
    text-align: right;
    background: #e6f4fa;
}
.sv-table .unit {
    color: #444;
    font-size: 18px;
    font-weight: normal;
    padding-left: 3px;
}
</style>
""", unsafe_allow_html=True)

# --- 레이아웃 분할 ---
col1, col2 = st.columns([1.18,1.2])

with col1:
    st.markdown('<div class="sv-header">적립금의 미래가치 실습 해보기</div>', unsafe_allow_html=True)
    
    st.markdown(
        '<table class="sv-table">'
        '<tr><th colspan="2">적립금의 미래가치(은퇴 시점 적립금의 원리금 합계) 계산</th></tr>'
        '<tr><td class="input-title" colspan="2">입력변수</td></tr>',
        unsafe_allow_html=True
    )

    # 값 입력 및 계산
    deposit = st.number_input('적립금', value=10000000, step=100000, format="%d")
    n_years = st.number_input('적립기간', value=40, step=1, format="%d")
    rate = st.number_input('이자율', value=4.00, step=0.1, format="%.2f")

    # 합계 및 미래가치 계산 (연단위, 매년말 불입)
    deposit_sum = deposit * n_years
    if rate != 0:
        fv = deposit * (((1 + rate / 100) ** n_years - 1) / (rate / 100))
    else:
        fv = deposit_sum

    st.markdown(
        f"""
        <tr>
            <td class="input-label">적립금</td>
            <td class="input-value">{deposit:,.0f} <span class="unit">원</span></td>
        </tr>
        <tr>
            <td class="input-label">적립기간</td>
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
            <td class="input-label">적립금 합계</td>
            <td class="output-sum">{deposit_sum:,.0f} <span class="unit">원</span></td>
        </tr>
        <tr>
            <td class="input-label">적립금 미래가치</td>
            <td class="output-value">{fv:,.0f} <span class="unit">원</span></td>
        </tr>
        </table>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.write("")
    st.markdown(f"""
    <div style="font-size:19px; line-height:2.0;">
    매년말 정기적으로 불입하는 금액(단위: 원)<br><br>
    적립 기간 (단위: 년)<br><br>
    연 이자율 (단위: %)<br><br><br>
    정기적으로 불입한 적립금 현금흐름의 합계 (단위: 원)<br><br>
    <span style="color:#c93025; font-size:18px;">{fv:,.0f}</span> : 정기적으로 불입한 적립금 현금흐름의 은퇴시점의 가치(단위: 원)
    </div>
    """, unsafe_allow_html=True)
