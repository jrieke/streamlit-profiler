import streamlit as st
from pyinstrument import Profiler as OriginalProfiler


class Profiler(OriginalProfiler):
    def stop(self):
        session = super().stop()
        
        # Create HTML report of profiling results.
        html = self.output_html()

        # Adapt style of html report to match Streamlit's design.
        
        # Default colors for Streamlit's white theme.
        # TODO: Use streamlit's theme colors instead of hardcoding colors. Doesn't work 
        #   currently, see https://github.com/streamlit/streamlit/issues/4198.
        text_color = "#31333f"
        background_color = "#ffffff"
        secondary_background_color = "#f0f2f6"
        caption_color = "#84858c"

        # Default font color
        html = html.replace("#fff", text_color)
        # Background color
        html = html.replace("#303538", background_color)
        # Line background when hovered
        html = html.replace(
            "background-color:#354759;opacity:.5",
            f"background-color:{secondary_background_color}",
        )
        # Header background
        html = html.replace("#292f32", secondary_background_color)
        # Expander background
        html = html.replace("#3b4043", secondary_background_color)
        # Expander background when hovered
        html = html.replace("#4a4f54", "#c1c1c5")
        # Expander text + triangle
        html = html.replace("hsla(0,0%,100%,.58)", caption_color)
        html = html.replace('fill:"#FFF"', f'fill:"{caption_color}"')
        html = html.replace('"fill-opacity":".582"', f'"fill-opacity":"1"')
        # Vertical guiding lines
        html = html.replace("opacity:.08", "opacity:.4")
        # File name and line (right side)
        html = html.replace("hsla(0,0%,100%,.5)", caption_color)
        # Metrics top right
        html = html.replace("#737779", text_color)
        # Metrics top right labels
        html = html.replace("#a9abad", caption_color)

        # Blue -> blue 80
        html = html.replace("#5db3ff", "#1c83e1")
        # Red -> red 80
        html = html.replace("#FF4159", "#ff2b2b")
        # Yellow -> yellow 80
        # html = html.replace("#D8CB2A", "#faca2b")
        # Green -> green 70
        html = html.replace("#7ED321", "#21c354")
        # Font weight of green color from 500 to 600 (to match other colors).
        # html = html.replace("e=500", "e=600")

        # Add border around body. Make it stick to the component iframe. 
        html = html.replace(
            "body,html{",
            "body{position:absolute;top:0;right:0;bottom:0;left:0;border:1px solid #d6d6d8;border-radius:0.25rem}body,html{",  # padding-bottom: 20px !important
        )

        # Make header top corners rounded to match border.
        html = html.replace(
            ".header[data-v-0183f483]{",
            ".header[data-v-0183f483]{border-radius:0.25rem 0.25rem 0 0;",
        )

        # Make timeline content scrollable, but keep header fixed. Adapt padding.
        html = html.replace("#app{", "#app{display:flex;flex-flow:column;height:100%;")
        html = html.replace(
            "#app{", "#app > div:nth-child(3){padding: 20px 30px;overflow:scroll}#app{"
        )
        html = html.replace('height:"20px"', 'height:"0"')  # remove spacer
        # html = html.replace(".margins{", ".margins{overflow:scroll;")

        # Display modified HTML report in iframe.
        st.components.v1.html(html, height=600)
        
        return session
