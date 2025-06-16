import streamlit as st

st.set_page_config(page_title="100세 시대를 대비한 재무설계", layout="centered")

# CSS 커버 스타일 적용
st.markdown("""
<style>
.cover-bg {
    min-height: 100vh;
    background: linear-gradient(135deg, #5e826a 0%, #6a9477 70%, #38604b 100%);
    position: relative;
    overflow: hidden;
    padding: 0;
}
.cover-header {
    position: absolute;
    top: 1.2vw;
    left: 2vw;
    color: #e0f5ea;
    font-size: 15px;
    font-family: 'Pretendard','Malgun Gothic',sans-serif;
    z-index: 10;
    opacity: 0.9;
}
.cover-header a {
    color: #e0f5ea;
    text-decoration: none;
}
.cover-big-circle {
    position: absolute;
    top: 4vw;
    left: 2vw;
    width: 350px;
    height: 350px;
    background: none;
    border-radius: 50%;
    border: 5px solid #6a9477;
    opacity: 0.13;
}
.cover-dots {
    position: absolute;
    right: 0vw;
    bottom: 5vw;
    width: 360px;
    height: 110px;
    opacity: 0.32;
}
.cover-dots svg {
    width: 100%;
    height: 100%;
}
.cover-title {
    position: relative;
    z-index: 2;
    color: white;
    text-align: left;
    margin-left: 80px;
    margin-top: 120px;
    font-family: 'Pretendard','Malgun Gothic',sans-serif;
}
.cover-number {
    font-size: 120px;
    font-weight: 900;
    line-height: 1.0;
    letter-spacing: -2px;
}
.cover-hr {
    border: none;
    border-top: 4px solid #fff;
    width: 220px;
    margin: 0.3em 0 1em 0;
    opacity: 0.9;
}
.cover-main-title {
    font-size: 44px;
    font-weight: 900;
    letter-spacing: -2px;
    line-height: 1.18;
    margin-top: 0.2em;
    margin-bottom: 0.2em;
    text-shadow: 0 2px 12px #42664955;
    word-break: keep-all;
}
.cover-shape1 {
    position: absolute;
    left: -8vw;
    top: 0vw;
    width: 62vw;
    height: 41vw;
    background: linear-gradient(110deg, #3b5847cc 0%, #5e826a00 100%);
    border-radius: 48vw 13vw 42vw 14vw;
    z-index: 1;
    opacity: 0.19;
    transform: rotate(-9deg);
}
.cover-triangle {
    position: absolute;
    right: 7vw;
    top: 3vw;
    width: 0; 
    height: 0; 
    border-left: 34px solid transparent;
    border-right: 34px solid transparent;
    border-bottom: 60px solid #c7e2cc33;
    opacity: 0.28;
    z-index: 2;
}
.cover-circle2 {
    position: absolute;
    left: 7vw;
    bottom: 4vw;
    width: 80px;
    height: 80px;
    background: none;
    border: 4px dotted #d9f4e3;
    border-radius: 50%;
    opacity: 0.37;
}
.cover-geos {
    position: absolute;
    right: 12vw;
    bottom: 11vw;
    font-size: 30px;
    color: #e9ffe3;
    opacity: 0.45;
    z-index: 3;
}
</style>
<div class="cover-bg">
    <div class="cover-header">
        💡 Made with ❤️ by 대원여고 HBN<br>
        📧 문의: <a href="mailto:hbn@dwg.sen.hs.kr">hbn@dwg.sen.hs.kr</a>
    </div>
    <div class="cover-shape1"></div>
    <div class="cover-big-circle"></div>
    <div class="cover-circle2"></div>
    <div class="cover-triangle"></div>
    <div class="cover-dots">
        <svg>
            <circle cx="22" cy="80" r="3" fill="#fff"/>
            <circle cx="42" cy="95" r="3" fill="#fff"/>
            <circle cx="62" cy="100" r="3" fill="#fff"/>
            <circle cx="80" cy="90" r="3" fill="#fff"/>
            <circle cx="100" cy="102" r="3" fill="#fff"/>
            <circle cx="120" cy="92" r="3" fill="#fff"/>
            <circle cx="140" cy="99" r="3" fill="#fff"/>
            <circle cx="160" cy="97" r="3" fill="#fff"/>
            <circle cx="180" cy="102" r="3" fill="#fff"/>
            <circle cx="200" cy="89" r="3" fill="#fff"/>
            <circle cx="220" cy="95" r="3" fill="#fff"/>
            <circle cx="240" cy="104" r="3" fill="#fff"/>
            <circle cx="260" cy="90" r="3" fill="#fff"/>
            <circle cx="280" cy="100" r="3" fill="#fff"/>
            <circle cx="300" cy="93" r="3" fill="#fff"/>
            <circle cx="320" cy="99" r="3" fill="#fff"/>
            <circle cx="340" cy="101" r="3" fill="#fff"/>
        </svg>
    </div>
    <div class="cover-title">
        <span class="cover-number">03</span><br>
        <hr class="cover-hr">
        <div class="cover-main-title">100세 시대를 대비한<br>재무설계</div>
    </div>
    <div class="cover-geos">
        &#9675; &nbsp; &#9651; &nbsp; + &nbsp; &#9675; &nbsp; &#9679; &nbsp; &#9651;
    </div>
</div>
""", unsafe_allow_html=True)

st.write("")
