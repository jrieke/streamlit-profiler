"""
Runs some functions and shows the profiler.

Install the package and start with `streamlit run examples/basic.py`.
"""

import time
import streamlit as st
from streamlit_profiler import Profiler


with Profiler():
    st.title(
        "Demo for [streamlit-profiler](https://github.com/jrieke/streamlit-profiler)"
    )
    st.write(
        """
        Simulates a few long-running functions (using `time.sleep`) and profiles them. 
        See code [here](https://github.com/jrieke/streamlit-profiler/blob/main/examples/basic.py).
        """
    )

    name = st.text_input("Enter your name")

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

    st.write("Profiler is shown below 👇")
