import streamlit as st
from pyinstrument import Profiler as OriginalProfiler


class Profiler(OriginalProfiler):
    def stop(self):
        session = super().stop()
        st.components.v1.html(self.output_html(), height=600, scrolling=True)
        return session
