import pandas as pd
import streamlit as st

from streamlit_pandas_profiling import st_profile_report
df=pd.read_csv('diamonds.csv')
st.title('data analysis of diamond dataset')
st.selectbox('select dataset',['diamonds'])
option=st.selectbox('Data Analysis',['Data Info','Data Analysis'])

if True:
    if option== 'Data Analysis':
        submit=st.button('report')
    elif option == 'Data Info':
        submit = st.button('Submit')

    if submit:
        if option == 'Data Analysis':
            pr = df.profile_report()
            st_profile_report(pr)
        elif option =='Data Info':
            st.write('Data Description')
            des = 'description.txt'
            with open('description.txt') as input:
                st.text(input.read())