import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
from plotly import graph_objs as go


data = pd.read_csv('Data/Salary_Data.csv')

st.title('Salary Predictor App')

nav = st.sidebar.radio('Navigation', ('Home', 'Prediction', 'Contribute'))

if nav == 'Home':
    st.image('Data//salary.png', width=500)

if st.checkbox('Show Table'):
    st.table(data)

graph = st.selectbox('What kind of graph?', ['Non-interactive', 'Interactive'])

if graph == 'Non-interactive':
    plt.figure(figsize=(10, 5))
    plt.scatter(data['YearsExperience'], data['Salary'])
    plt.ylim(0)
    plt.xlabel('Years of Experience')
    plt.ylabel('Salary')
    plt.tight_layout()
    st.pyplot()

if graph == 'Interactive':


if nav == 'Prediction':
    st.write('Pred')

if nav == 'Contribute':
    st.write('Contri')



