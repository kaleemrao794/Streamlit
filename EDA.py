import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# webapp ka title
st.markdown('''
# **Exploratory Data Analysis Web Application**
This app is developed by Kaleem Ullah called **EDA App**
   ''')

# how to upload a file from pc
with st.sidebar.header('Upload your Dataset(.csv)'):
   uploaded_file = st.sidebar.file_uploader("Upload your file", type=['csv'])
   df = sns.load_dataset('titanic')
   st.sidebar.markdown('[Example CSV file](https://www.kaggle.com/louise2001/quantum-physics-articles-on-arxiv-1994-to-2009)')

# profiling reports for pandas
if uploaded_file is not None:
   @st.cache
   def load_csv():
      csv = pd.read_csv(uploaded_file)
      return csv
   df = load_csv()
   pr = ProfileReport(df, explorative=True)
   st.header('**Input DF**')
   st.write(df)
   st.write('---')
   st.header('**Profiling Report with Pandas**')
   st_profile_report(pr)
else:
   st.info('Awaiting for CSV file.')
   if st.button('Press to use example data'):
      # example dataset
      @st.cache
      def load_data():
         a = pd.DataFrame(np.random.randn(100,6),
                           columns=['J','U','N',"A",'I','D'])
         return a
         df = load_data()
         pr = ProfileReport(df, explorative=True)
         st.header('**Input DF**')
         st.write(df)
         st.write('---')
         st.header('**Profiling Report with Pandas**')
         st_profile_report(pr)

