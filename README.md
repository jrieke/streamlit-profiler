# streamlit-profiler &nbsp;🏄🏼

[![PyPi](https://img.shields.io/pypi/v/streamlit-profiler)](https://pypi.org/project/streamlit-profiler/)

**Runtime profiler for Streamlit, powered by [pyinstrument](https://github.com/joerick/pyinstrument).**

streamlit-profiler is a Streamlit component that helps you find out which parts of your
code are slow. It profiles code via [pyinstrument](https://github.com/joerick/pyinstrument)
and shows the results right within the Streamlit app.

<sup>Alpha version, use with care.</sup>

<!--

<h3 align="center">
  🎉 <a href="https://github.com/jrieke/streamlit-profiler">Try it out</a> 🎉
</h3>

---

<p align="center">
    <a href="https://github.com/jrieke/readme-template"><img src="demo.gif" width=600></a>
</p>
-->

## Installation

```bash
pip install streamlit-profiler
```

## How to use it

```python
import streamlit as st
from streamlit_profiler import Profiler

with Profiler():
    st.title("My app")
    # ... and any other code
```

## TODOs

PRs are welcome! If you want to work on any of these things, please open an issue to coordinate.

- [ ] TBD
