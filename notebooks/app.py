import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('../vehicles_us.csv')
st.header('Vehicle Sales Data Analysis')
hist_button = st.button('Create Histogram') 
if hist_button: st.write('Creating a histogram for the vehicle mileage distribution')
    
fig = px.histogram( 
    car_data, 
    x='odometer', 
    nbins=50, 
    title='Distribution of Vehicle Mileage', 
    labels={ 'odometer': 'Mileage (miles)', 'count': 'Number of Vehicles' }, 
    color_discrete_sequence=['#0B1F3A'] 
    )
    
fig.update_traces( 
    marker_line_color='#061426', 
    marker_line_width=1, 
    opacity=0.95 
    )
    
fig.update_layout( 
    plot_bgcolor='white', 
    paper_bgcolor='white', 
    title={'text': 'Distribution of Vehicle Mileage', 'x': 0.5, 'xanchor': 'center', 'font': { 'size': 22, 'color': '#0B1F3A' } }, 
    font={ 'family': 'Arial', 'size': 13, 'color': '#1A1A1A' }, 
    xaxis={ 'showgrid': False, 'zeroline': False, 'title': 'Mileage (miles)' }, 
    yaxis={ 'showgrid': False, 'zeroline': False, 'title': 'Number of Vehicles' }, 
    bargap=0.12, 
    margin={ 'l': 70, 'r': 40, 't': 80, 'b': 60 } 
    )
    
st.plotly_chart(fig, use_container_width=True)
scatter_button = st.button('Create Scatter Plot') 
if scatter_button: st.write( 'Creating a scatter plot of vehicle price and mileage' )
    
fig = px.scatter( 
    car_data, 
    x='odometer', 
    y='price', 
    title='Vehicle Price vs. Mileage', 
    labels={ 'odometer': 'Mileage (miles)', 'price': 'Price (USD)' }, 
    color_discrete_sequence=['#0B1F3A'] 
    ) 
   
fig.update_traces(
    marker={ 'size': 7, 'opacity': 0.65, 'line': { 'width': 0.5, 'color': '#061426' } } 
    )
   
fig.update_layout(
    plot_bgcolor='white', 
    paper_bgcolor='white', 
    title={ 'text': 'Vehicle Price vs. Mileage', 'x': 0.5, 'xanchor': 'center', 'font': { 'size': 22, 'color': '#0B1F3A' } }, 
    font={ 'family': 'Arial', 'size': 13, 'color': '#1A1A1A' }, 
    xaxis={ 'showgrid': False, 'zeroline': False, 'title': 'Mileage (miles)' }, 
    yaxis={ 'showgrid': False, 'zeroline': False, 'title': 'Price (USD)' }, 
    margin={ 'l': 70, 'r': 40, 't': 80, 'b': 60 } )
    
st.plotly_chart(fig, use_container_width=True)