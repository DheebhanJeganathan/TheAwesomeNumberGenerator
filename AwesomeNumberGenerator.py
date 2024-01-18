import streamlit as st
import random

from numpy.random import rand


def click_button():
    st.session_state.clicked = True
    random_int = rand.range(1, 10)
    st.write(str(random_int))

