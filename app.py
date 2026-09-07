import streamlit as st

st.set_page_config(
    page_title="2306历史纪念馆",
    page_icon="😂",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.doubao.com/chat',
        'Report a bug': "https://www.doubao.com/chat",
        'About': "这只是一个供人回忆的地方(有事自己问豆包)"
    }
)

st.title('2306历史纪念馆')
st.logo('resource/logo.png',size="large")

st.header('成员一览(排名不分前后)')

st.subheader('雷金龙')
st.image('resource/ljl.jpg',width=400)

st.subheader('杨炜潼')
st.image('resource/ywt.jpg',width=400)

st.subheader('谭浩杰')
st.image('resource/thj.jpg',width=400)

st.subheader('秦均豪')
st.image('resource/qjh.jpg',width=400)

st.subheader('钟浩')
st.image('resource/zh.jpg',width=400)

st.subheader('吴彦祖')
st.image('resource/hhh.jpg',width=400)