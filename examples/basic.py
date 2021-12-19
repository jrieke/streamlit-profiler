"""
Runs some functions and shows the profiler.

Install the package and start with `streamlit run examples/basic.py`.
"""

import time
import streamlit as st
from streamlit_profiler import Profiler


with Profiler():
    st.title(
        "Demo for [streamlit-profiler](https://github.com/jrieke/streamlit-profiler) 🏄🏼"
    )
    st.write("""Select which functions you want to run:""")

    def clear_sky():
        time.sleep(1)

    def inflate_balloons():
        time.sleep(2)

    def release_balloons():
        time.sleep(0.2)
        st.balloons()

    if st.checkbox("Clear sky"):
        clear_sky()
    if st.checkbox("Inflate balloons"):
        inflate_balloons()
    if st.checkbox("Release!"):
        release_balloons()

    st.write("...and see their runtime in the profiler:")


st.caption(
    "[View code for this demo](https://github.com/jrieke/streamlit-profiler/blob/main/examples/basic.py)"
)
