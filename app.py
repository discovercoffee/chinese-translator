import streamlit as st
import urllib.parse

st.set_page_config(page_title="중국어 자동 번역기", page_icon="🇨🇳")

# 화면 디자인
st.title("🇨🇳 중국어(간체) 자동 번역기")
st.success("식당 사장님을 위한 간편 번역 도구입니다.")

st.markdown("""
우리 가게 네이버 플레이스 주소나, 궁금한 웹사이트 주소를 넣으시면
중국인 손님들이 보는 **중국어 화면**으로 자동 번역해 드립니다.
""")

# 주소 입력 받기
url = st.text_input("👇 여기에 웹사이트 주소를 붙여넣으세요", placeholder="예: https://map.naver.com/...")

if url:
    try:
        if not url.startswith("http"):
            url = "https://" + url

        # 인코딩 및 번역 링크 생성
        encoded_url = urllib.parse.quote(url, safe='')
        translate_link = f"https://translate.google.com/translate?sl=auto&tl=zh-CN&u={url}"

        st.divider()
        
        # 버튼 만들기
        st.markdown(f"""
        <a href="{translate_link}" target="_blank" style="
            display: block;
            text-align: center;
            padding: 15px;
            background-color: #d93025; 
            color: white;
            text-decoration: none;
            border-radius: 10px;
            font-size: 18px;
            font-weight: bold;
        ">🇨🇳 번역된 화면 보러가기 (클릭)</a>
        """, unsafe_allow_html=True)
        
        st.info("👆 위 붉은 버튼을 누르면 중국어 페이지가 열립니다.")

    except Exception as e:
        st.error("주소가 올바르지 않습니다. 다시 확인해주세요.")
