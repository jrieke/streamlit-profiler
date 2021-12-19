import streamlit as st
from pyinstrument import Profiler as OriginalProfiler


class Profiler(OriginalProfiler):
    def stop(self):
        session = super().stop()
        html = self.output_html()

        # Adapt style of html output to match streamlit design.
        # TODO: Use streamlit's theme colors. Doesn't work if using var(...) in here.
        #   Also doesn't work if using
        #   st.components.v1.html('<div style="background-color: var(--primary-color);">foo</div>')
        #   so I'd expect it's not an issue of the specific html template here.

        text_color = "#31333f"
        background_color = "#ffffff"
        secondary_background_color = "#f0f2f6"
        caption_color = "#84858c"

        # Font color: white -> black (streamlit's font color)
        html = html.replace("#fff", text_color)
        # Background color: gray -> white
        html = html.replace("#303538", background_color)
        # Normal line hover: gray -> light gray
        html = html.replace(
            "background-color:#354759;opacity:.5",
            f"background-color:{secondary_background_color}",
        )
        # Header background: dark gray -> light gray (streamlit's widget color)
        html = html.replace("#292f32", secondary_background_color)
        # Expander background: gray -> light gray (streamlit's widget color)
        html = html.replace("#3b4043", secondary_background_color)
        # Expander hovered: dark gray -> gray (between streamlit's widget & caption color)
        html = html.replace("#4a4f54", "#c1c1c5")
        # Expander text + triangle: white -> gray (streamlit's caption color)
        html = html.replace("hsla(0,0%,100%,.58)", caption_color)
        html = html.replace('fill:"#FFF"', f'fill:"{caption_color}"')
        html = html.replace('"fill-opacity":".582"', f'"fill-opacity":"1"')
        # Vertical lines opacity
        html = html.replace("opacity:.08", "opacity:.4")
        # Details on right side: white -> gray (streamlit's caption color)
        html = html.replace("hsla(0,0%,100%,.5)", caption_color)
        # Metrics top right: dark gray -> black (streamlit's font color)
        html = html.replace("#737779", text_color)
        # Metrics descriptions: gray -> gray (streamlit's caption color)
        html = html.replace("#a9abad", caption_color)

        # Blue -> blue 80
        html = html.replace("#5db3ff", "#1c83e1")
        # Red -> red 80
        html = html.replace("#FF4159", "#ff2b2b")
        # Yellow -> yellow 80
        # html = html.replace("#D8CB2A", "#faca2b")
        # Green -> green 70
        html = html.replace("#7ED321", "#21c354")

        # Add border to body.
        html = html.replace(
            "body,html{",
            "body{position:absolute;top:0;right:0;bottom:0;left:0;border:1px solid #d6d6d8;border-radius:0.25rem;padding-bottom: 20px !important}body,html{",
        )

        # Make header content rounded to match border.
        html = html.replace(
            ".header[data-v-0183f483]{",
            ".header[data-v-0183f483]{border-radius:0.25rem 0.25rem 0 0;",
        )

        # Make timeline content scrollable, but keep header fixed.
        html = html.replace("#app{", "#app{display:flex;flex-flow:column;height:100%;")
        html = html.replace(".margins{", ".margins{overflow:scroll;")

        st.components.v1.html(html, height=600)
        return session
