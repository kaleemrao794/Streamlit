# import libraries
import streamlit as st
import plotly.express as px
import pandas as pd 

# import dataset
st.title('Plotly and Streamlit ko mila ka app bnana')
df = px.data.gapminder()
st.write(df)
st.write(df.columns)
# Summary stats
st.write(df.describe())

# Data Management
year_option = df['year'].unique().tolist()  # make a list
# year = st.selectbox('Which year should we plot?', year_option, 0) # make a box      # 0 is for index
# df = df[df['year']==year]       # modification of origional column

# Plotting with Plotly
fig = px.scatter(df, x= 'gdpPercap', y= 'lifeExp', size='pop', color='country', hover_name='country',
                log_x=True, size_max=55, range_x=[100,100000], range_y=[20,90],
                animation_frame='year', animation_group='country')
fig.update_layout(width=800, height=600)
st.write(fig)