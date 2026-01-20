import streamlit as st

st.set_page_config(page_title="중국어 번역기", page_icon="🇨🇳")

st.title("🇨🇳 식당 전용 중국어 번역기")
st.write("입력하신 주소를 중국인 손님이 보는 화면으로 변환합니다.")

# 주소 입력창
url = st.text_input("👇 매장 주소(네이버 플레이스 등)를 붙여넣으세요", placeholder="https://naver.me/xxx")

if url:
    url = url.strip()
    if not url.startswith("http"):
        url = "https://" + url

    # 방식 1: 구글 번역 (가장 대중적)
    google_link = f"https://translate.google.com/translate?sl=auto&tl=zh-CN&u={url}"
    
    # 방식 2: 빙(Bing/MS) 번역 (구글이 안 될 때 대안)
    bing_link = f"https://www.bing.com/translator/?to=zh-Hans&url={url}"

    st.divider()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("방법 A (추천)")
        st.markdown(f"""
            <a href="{google_link}" target="_blank" style="
                display: block; text-align: center; padding: 15px;
                background-color: #4285F4; color: white;
                text-decoration: none; border-radius: 10px; font-weight: bold;
            ">구글 엔진으로 열기</a>
        """, unsafe_allow_html=True)
        st.caption("가장 일반적으로 사용되는 번역 방식입니다.")

    with col2:
        st.subheader("방법 B (대안)")
        st.markdown(f"""
            <a href="{bing_link}" target="_blank" style="
                display: block; text-align: center; padding: 15px;
                background-color: #00897B; color: white;
                text-decoration: none; border-radius: 10px; font-weight: bold;
            ">빙(Bing) 엔진으로 열기</a>
        """, unsafe_allow_html=True)
        st.caption("구글에서 '이용 불가'가 뜰 때 사용하세요.")

    st.info("💡 **꿀팁:** 만약 위 버튼들이 모두 안 된다면, 스마트폰 브라우저(크롬/사파리) 설정에서 '번역' 기능을 켜는 것이 가장 정확합니다.")
