import streamlit as st

st.set_page_config(page_title="화폐의 현재가치 계산", layout="centered")

# 스타일 지정
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
    background: #e9c8ef;
    color: #23132b;
    text-align: center;
    font-size: 28px;
    font-weight: bold;
}
.pv-table .input-title, .pv-table .output-title {
    background: #f4f4f4;
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
    color: #2e1760;
    font-weight: bold;
    font-size: 29px;
    text-align: right;
    background: #e9c8ef;
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
col1, col2 = st.columns([1,1.4])
with col1:
    future_value = st.number_input('미래가치', value=10000000, step=100000, format="%d", key="future_value_input")
with col2:
    st.markdown(f"<span style='font-size:22px; color:#e30000; font-weight:800'>{future_value:,.0f} 원</span>", unsafe_allow_html=True)

years = st.number_input('기간', value=7, step=1, format="%d")
rate = st.number_input('이자율', value=5.00, step=0.1, format="%.2f")
present_value = future_value / ((1 + rate / 100) ** years)

# 표 출력
st.markdown(f"""
<table class="pv-table">
    <tr>
        <th colspan="2">화폐의 현재가치 계산</th>
    </tr>
    <tr>
        <td class="input-title" colspan="2">입력변수</td>
    </tr>
    <tr>
        <td class="input-label">미래가치</td>
        <td class="input-value">{future_value:,.0f} <span class="unit">원</span></td>
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
        <td class="input-label">현재가치</td>
        <td class="output-value">{present_value:,.0f} <span class="unit">원</span></td>
    </tr>
</table>
""", unsafe_allow_html=True)
