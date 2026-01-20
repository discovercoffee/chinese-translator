import streamlit as st

st.set_page_config(page_title="중국어 자동 번역기", page_icon="🇨🇳")

st.title("🇨🇳 중국어(간체) 자동 번역기")
st.info("식당 주소(네이버/카카오 등)를 입력하면 중국어로 번역합니다.")

# 주소 입력창
url = st.text_input("👇 웹사이트 주소를 붙여넣으세요", placeholder="https://naver.me/xxx")

if url:
    # 1. 주소 정제 (앞뒤 공백 제거)
    clean_url = url.strip()
    
    if not clean_url.startswith("http"):
        clean_url = "https://" + clean_url

    # 2. 구글 번역 URL 생성 (가장 표준적인 방식)
    # sl=auto(언어자동감지), tl=zh-CN(중국어간체), u=주소
    translate_link = f"https://translate.google.com/translate?sl=auto&tl=zh-CN&u={clean_url}"

    st.divider()
    
    # 3. 결과 안내
    st.subheader("✅ 번역 링크 생성 완료")
    st.write("아래 버튼을 누르면 구글 번역 엔진이 해당 사이트를 중국어로 보여줍니다.")
    
    # 사장님들이 누르기 편한 큰 버튼
    st.markdown(f"""
        <a href="{translate_link}" target="_blank" style="
            display: block;
            text-align: center;
            padding: 20px;
            background-color: #00C73C; /* 네이버 느낌의 초록색 */
            color: white;
            text-decoration: none;
            border-radius: 12px;
            font-size: 20px;
            font-weight: bold;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        ">🇨🇳 중국어로 번역해서 보기</a>
    """, unsafe_allow_html=True)
    
    st.warning("⚠️ 참고: 네이버 지도 앱 주소(naver.me)는 구글 번역기 내에서 보안상 바로 안 열릴 수 있습니다. 그럴 땐 매장의 '실제 전체 주소'를 입력하는 것이 좋습니다.")
