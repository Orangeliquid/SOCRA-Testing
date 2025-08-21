import streamlit as st

from ui.start import run_start
from app.utils.style import custom_css


st.set_page_config(page_title="SOCRA Testing", page_icon="assets/orange_alien.ico")

# Inject custom_css at the start of streamlit_app run
st.markdown(custom_css, unsafe_allow_html=True)


def main():
    st.markdown(
        "<h1 style='color:#FFA500; text-align: center; '>Orangeliquid's</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<h2 style='color:#FF10F0; text-align: center; text-style: italic; '><i>SOCRA Testing Extraordinaire</i></h2>",
        unsafe_allow_html=True
    )

    st.write("---")
    run_start()


if __name__ == '__main__':
    main()
