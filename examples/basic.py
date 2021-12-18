import time
import streamlit as st
from streamlit_profiler import Profiler


with Profiler():
    st.title("Streamlit App")

    name = st.text_input("Your name")

    def long_computation():
        time.sleep(1)
        return 42

    if name:
        st.write(f"Hey {name} 👋 Your lucky number is:", long_computation())

        clicked = st.button("Show something cool")
        if clicked:

            def countdown():
                for i in range(3, 0, -1):
                    st.write(f"{i}...")
                    time.sleep(1)

            countdown()
            st.write("Balloons! 🎈")
            st.balloons()
