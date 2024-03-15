import datetime

import pandas as pd
import streamlit as st
from snowflake.snowpark.context import get_active_session
from streamlit import (
    code,
    dataframe,
    markdown,
    multiselect,
    select_slider,
    tabs,
    vega_lite_chart,
)

st.set_page_config(layout="wide")

st.title("Cybersyn: Financial Package Preview")