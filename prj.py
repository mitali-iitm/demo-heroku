import streamlit as st
st.title('GA 8')
st.subheader('Dividing App')
placeholder_diviend = st.empty()
placeholder_divisor = st.empty()
n = placeholder_dividend.number_input('Enter Dividend')
d= placeholder_divisor.number_input('Enter Divisor ')
st.write(n/d)
