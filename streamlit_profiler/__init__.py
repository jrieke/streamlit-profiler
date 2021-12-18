import streamlit as st
from pyinstrument import Profiler as OriginalProfiler


class Profiler(OriginalProfiler):
    def __exit__(self, type, value, traceback):
        result = super().__exit__(type, value, traceback)
        st.components.v1.html(self.output_html(), height=400, scrolling=True)
        return result
