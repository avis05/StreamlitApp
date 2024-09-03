import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(layout="wide")

st.markdown(
    """
    <style>
    .lottie-wrapper {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100%;
        height: auto; 
        margin: 50px 0; /* Add margin if needed */
        padding-left: 200px;
    }
    .title-text {
        font-size: 36px;
        font-weight: bold;
        margin-bottom: 20px;
        text-align: center;
    }
    .subheader-text {
        font-size: 30px;
        font-weight: bold;
        margin-top: 10px;
        text-align: center;
    }
    .centered-text {
        text-align: center;
        font-size: 18px;
        width: 80%; 
        max-width: 800px; 
        margin: 0 auto;
        line-height: 1.6;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coder = load_lottie_url("https://lottie.host/cb3fd299-254c-4afa-9e45-e2e9d7b57a9e/fx3PTuqlgh.json")


st.markdown('<div class="lottie-wrapper">', unsafe_allow_html=True)
st_lottie(lottie_coder)
st.markdown('</div>', unsafe_allow_html=True)


st.markdown('<div class="title-text">Hi! I am Andrhey T. Visbal</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader-text">FULL STACK DEVELOPER</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader-text">About Me</div>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="centered-text">
    Hi there! I have a passion for creating dynamic and user-friendly web applications and I'm an aspiring full-stack developer. 
    My interest in the technical aspects of websites led me to pursue a career in web development. My proficiency with front-end and 
    back-end technologies has improved with time, enabling me to produce streamlined and effective online experiences.
    I'm dedicated to always honing my skill set, and I'm always excited to master new tools and technology. 
    I take pleasure in every stage of the process, be it creating strong server-side logic or user-friendly interfaces.
    I'm thrilled about the opportunities that lie ahead and am looking forward to helping out on important tech-related projects.
    </div>
    """,
    unsafe_allow_html=True,
)
