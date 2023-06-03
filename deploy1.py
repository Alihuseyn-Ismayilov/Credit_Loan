#import pickle as pkl
import warnings
import streamlit as st
import joblib

warnings.filterwarnings('ignore')

#st.markdown("<h1 style='margin-top: 0.25rem;'>My Title</h1>", unsafe_allow_html=True)
st.markdown(
    """
    <style>
    .css-1y4p8pa {
        padding: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.title('Credit prediction based on historical')

import os

current_dir = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(current_dir, 'model.joblib')

model = joblib.load(model_path)



#st.title('Credict loan prediction model')

#revolvingutilizationofunsecuredlines	age	numberoftime30_59dayspastduenotworse	debtratio	#monthlyincome	numberofopencreditlinesandloans	numberrealestateloansorlines	numberofdependents	islate
#124339	0.031530	59.0	0	0.003737	9900.0	3.0	0.0	0.0	0


with st.form('my_form'):
    col1, col2 = st.columns(2)
    with col1:
        v1 = st.number_input(label='revolvingutilizationofunsecuredlines',value=0.031530,format='%4f')
        v2 = st.number_input(label='age',value=59,format='%d')
        v3 = st.number_input(label='numberoftime30_59dayspastduenotworse',value=0,format='%d')
        v4 = st.number_input(label='debtratio',value=0.003737,format='%6f')
    with col2:
        v5 = st.number_input(label='monthlyincome',value=9900.0,format='%1f')
        v6 = st.number_input(label='numberofopencreditlinesandloans',value=3,format='%d')
        v7 = st.number_input(label='numberrealestateloansorlines',value=0,format='%d')
        v8 = st.number_input(label='numberofdependents',value=0,format='%d')
    v9 = st.radio("Have late payments?",("Yes","No"))
    v = 0
    if(v9 == "Yes"):
        v = 1
    submit = st.form_submit_button('submit')
predictors = [[v1,v2,v3,v4,v5,v6,v7,v8,v]]

#st.write(predictors)
if(model.predict(predictors)[0] == 0):
    st.write('No')
else:
    st.write('Yes')

