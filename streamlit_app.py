from collections import namedtuple
import altair as alt
import math
import pandas as pd
import numpy as np
import altair as alt
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

st.write('Hello world!')
st.header('st.choice')

if st.button('Say hello touch it'):
     st.write('Why hello there')
else:
     st.write('Goodbye')



st.header('st.write')
st.write('Hello,*World!* :sunglasses:')
st.markdown('Hello wrold')

st.write(1234)

df=pd.DataFrame({'first_column':[1,2,3],'second_colum':[4,5,6]})
st.write(df)

st.write('below is a dataframe',df,'Above is a dataframe')

df2=pd.DataFrame(np.random.randn(200,3),columns=['a','b','c'])
c=alt.chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)
