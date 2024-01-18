import streamlit as st
import random

from numpy.random import rand


def click_button():
    st.write(str(random.randint(1, 10)))


st.button("Click Me!", on_click=click_button())
