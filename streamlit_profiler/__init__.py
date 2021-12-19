import streamlit as st
from pyinstrument import Profiler as OriginalProfiler


class Profiler(OriginalProfiler):
    def stop(self):
        session = super().stop()
        html = self.output_html()

        # Adapt style of html output to match streamlit design.
        # TODO: Use streamlit's theme colors.
        # Font color: white -> black (streamlit's font color)
        html = html.replace("#fff", "#31333f")
        # Background color: gray -> white
        html = html.replace("#303538", "#ffffff")
        # Normal line hover: gray -> light gray
        html = html.replace(
            "background-color:#354759;opacity:.5", "background-color:#f0f2f6"
        )
        # Header background: dark gray -> light gray (streamlit's widget color)
        html = html.replace("#292f32", "#f0f2f6")
        # Expander background: gray -> light gray (streamlit's widget color)
        html = html.replace("#3b4043", "#f0f2f6")
        # Expander hovered: dark gray -> gray (between streamlit's widget & caption color)
        html = html.replace("#4a4f54", "#c1c1c5")
        # Expander text + triangle: white -> gray (streamlit's caption color)
        html = html.replace("hsla(0,0%,100%,.58)", "#84858c")
        html = html.replace('fill:"#FFF"', 'fill:"#84858c"')
        # Vertical lines opacity
        html = html.replace("opacity:.08", "opacity:.3")
        # Details on right side: white -> gray (streamlit's caption color)
        html = html.replace("hsla(0,0%,100%,.5)", "#84858c")
        # Metrics top right: dark gray -> black (streamlit's font color)
        html = html.replace("#737779", "#31333f")
        # Metrics descriptions: gray -> gray (streamlit's caption color)
        html = html.replace("#a9abad", "#84858c")

        # Blue -> blue 80
        html = html.replace("#5db3ff", "#1c83e1")
        # Red -> red 80
        # html = html.replace("#FF4159", "#ff2b2b")
        # Yellow -> yellow 80
        # html = html.replace("#D8CB2A", "#faca2b")

        # Add border to body.
        html = html.replace(
            "body,html{",
            "body{border:1px solid #d6d6d8;border-radius:0.25rem;padding-bottom:20px !important;}body,html{",
        )
        # Make header content rounded to match border.
        html = html.replace(
            ".header[data-v-0183f483]{",
            ".header[data-v-0183f483]{border-radius:0.25rem;",
        )

        st.components.v1.html(html, height=600, scrolling=True)
        return session
