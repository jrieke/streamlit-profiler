# streamlit-profiler &nbsp;🏄🏼

[![PyPi](https://img.shields.io/pypi/v/streamlit-profiler)](https://pypi.org/project/streamlit-profiler/)

**Runtime profiler for Streamlit, powered by [pyinstrument](https://github.com/joerick/pyinstrument).**

streamlit-profiler is a [Streamlit component](https://streamlit.io/components) that
helps you find out which parts of your app are slow. It profiles the code via
[pyinstrument](https://github.com/joerick/pyinstrument) and shows the results right
within your Streamlit app.

<sup>Alpha version, use with care.</sup>

---

<h3 align="center">
  ⏱️ <a href="https://share.streamlit.io/jrieke/streamlit-profiler/main/examples/basic.py">Live demo</a> ⏱️
</h3>

---

<p align="center">
    <a href="https://share.streamlit.io/jrieke/streamlit-profiler/main/examples/basic.py"><img src="images/demo.png" width=600></a>
</p>

## Installation

```bash
pip install streamlit-profiler
```

## Usage

```python
import streamlit as st
from streamlit_profiler import Profiler

with Profiler():
    st.title("My app")
    # ... other code

# Or:
# p = Profiler()
# p.start()
# ...
# p.stop()
```

Then start your app as usual: `streamlit run my_app.py`

The `Profiler` class is an extension of `pyinstrument.Profiler`, so you can use
[all of its functions](https://pyinstrument.readthedocs.io/en/latest/reference.html#pyinstrument.Profiler).
