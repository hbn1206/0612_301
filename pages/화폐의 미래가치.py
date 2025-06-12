import streamlit as st

st.set_page_config(page_title="화폐의 미래가치 실습", layout="wide")

# ---- 스타일 ----
st.markdown("""
<style>
.mv-header {
    width: 780px;
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
.mv-table {
    width: 540px;
    border-collapse: collapse;
    font-size: 25px;
    font-family: "Pretendard", "Malgun Gothic", "맑은 고딕", Arial, sans-serif;
}
.mv-table th, .mv-table td {
    border: 2.2px solid #000;
    padding: 6px 16px;
    text-align: left;
    height: 38px;
}
.mv-table th {
    background: #91d0f5;
    color: #23132b;
    text-align: center;
    font-size: 28px;
    font-weight: bold;
}
.mv-table .input-title, .mv-table .output-title {
    background: #e6f4fa;
    color: #222;
    font-size: 19px;
    font-weight: bold;
    border-right: none;
}
.mv-table .output-title {
    border-top: 2.2px solid #000;
}
.mv-table .input-label {
    font-size: 25px;
    font-weight: bold;
    background: #f9f9f9;
    width: 120px;
}
.mv-table .input-value {
    color: #e30000;
    font-weight: bold;
    font-size: 26px;
    text-align: right;
    background: #fff;
    width: 170px;
}
.mv-table .output-value {
    color: #0866ad;
    font-weight: bold;
    font-size: 29px;
    text-align: right;
    background: #91d0f5;
}
.mv-table .unit {
    color: #444;
    font-size: 18px;
    font-weight: normal;
    padding-left: 3px;
}
.mv-table td {
    vertical-align: middle;
}
</style>
""", unsafe_allow_html=True)

# ---- 양쪽으로 화면 분할 ----
col1, col2 = st.columns([1.15,1.2])

# ---- 표/입력 ----
with col1:
    st.markdown('<div class="mv-header">화폐의 미래가치 실습 해보기</div>', unsafe_allow_html=True)
    
    st.markdown('<table class="mv-table">'
        '<tr><th colspan="2">화폐의 미래가치 계산</th></tr>'
        '<tr><td class="input-title" colspan="2">입력변수</td></tr>', unsafe_allow_html=True)

    present_value = st.number_input('현재가치', value=10000000, step=100000, format="%d")
    years = st.number_input('기간', value=4, step=1, format="%d")
    rate = st.number_input('이자율', value=5.00, step=0.1, format="%.2f")
    future_value = present_value * ((1 + rate / 100) ** years)

    st.markdown(
        f"""
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
        <tr><td class="output-title" colspan="2">출력변수</td></tr>
        <tr>
            <td class="input-label">미래가치</td>
            <td class="output-value">{future_value:,.0f} <span class="unit">원</span></td>
        </tr>
        </table>
        """, unsafe_allow_html=True)

# ---- 우측 변수 설명 ----
with col2:
    st.write("")
    st.markdown("""
    <div style="font-size:19px; line-height:1.95;">
    <b>현재 시점의 일정 금액</b> (단위: 원)<br><br>
    현재 시점과 미래 시점 사이의 기간 (단위: 년)<br><br>
    연 이자율 (단위: %)<br><br><br>
    <span style="color:#c93025; font-size:18px;">{:,}</span> : 현재 시점의 일정 금액을 미래 특정 시점의 가치로 환산한 금액 (단위: 원)
    </div>
    """.format(int(future_value)), unsafe_allow_html=True)
