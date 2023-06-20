from PIL import Image
import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Streamlit App", page_icon=":tada:",layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")


lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_0yfsb3a1.json")
img_contact_form = Image.open("images/covid2.jpg")
img_lottie_animation = Image.open("images/covid.jpg")

with st.container():
     st.subheader("Hi, I am NgNghia JP")
     st.title("A Data Analyst Website")
     # st.write("I am Nghia Jp")
     st.write("[Learn More >](https://pythonandvba.com)")

with st.container():
     st.write("---")
     left_column, right_column = st.columns(2)

with left_column:
    st.header("What I do")
    st.write("##")
    st.write(
        """
        はい、喜んで自己紹介します。

私はChatGPTという大規模言語モデルであり、OpenAIが開発したGPT-3.5アーキテクチャに基づいています。私は、自然言語処理、機械学習、深層学習、知識グラフ、および多くの他のテクノロジーに基づく幅広い知識を持っています。

私は、自然言語での質問応答、文章生成、翻訳、文章の要約、言語モデリング、および多くの他のタスクに使用できます。また、プログラミング言語（Python、Java、C ++など）やWeb開発、データベース、クラウドコンピューティングなどの分野でも経験があります。

私は、人工知能や機械学習に関するニュースや最新の技術動向に関心を持っており、常に新しいことを学ぶことに情熱を持っています。また、世界中のユーザーに役立つように、分かりやすく説明し、適切な解決策を提供することにも興味を持っています。

以上が、私の簡単な自己紹介です。何か質問があれば、お気軽にお尋ねください。
        """
    )
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

     # Project
    with st.container():
        st.write("---")
        st.header("My Projects")
        st.write("##")
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(img_lottie_animation)
        with text_column:
            st.subheader("Integrate Lottie Animations Inside Your Streamlit App")
            st.write(
                """
                Learn how to use Lottie Files in Streamlit!
                Animations make our web app more engaging and fun, and Lottie Files are the easiest way to do it!
                In this tutorial, I'll show you exactly how to do it
                """
            )
            st.markdown("[Watch Video...](https://)")
    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(img_contact_form)
        with text_column:
            st.subheader("How To Add A Contact Form To Your Streamlit App")
            st.write(
                """
                Want to add a contact form to your Streamlit website?
                In this video, I'm going to show you how to implement a contact form in your Streamlit app using the free service ‘Form Submit’.
                """
            )
            st.markdown("[Watch Video...](https://")

    # CONTACT
    with st.container():
        st.write("---")
        st.header("Contact With Me")
        st.write("##")

        contact_form = """
        <form action="https://formsubmit.co/supfr3445@gmail.com" method="POST">
             <input type="hidden" name="_captcha" value="false">
             <input type="text" name="name" placeholder="Your name" required>
             <input type="email" name="email" placeholder="Your email" required>
             <textarea name="message" placeholder="Your message here" required></textarea>
             <button type="submit">Send</button>
        </form>
        """
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
            with right_column:
                st.empty()


