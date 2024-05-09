import subprocess
import sys
subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])

import pickle as pkl
import streamlit as st
import pandas as pd
from tabulate import tabulate

# Import model and related information

with open('./DATA/model_mean.pkl', 'rb') as f:
    model = pkl.load(f)

model_features = pd.read_csv('./DATA/model_features_mean.csv')

# Setup Streamlit layout

st.set_page_config(layout = "wide")

st.title('**Machine Learning-Based Prediction of Cardiovascular Disease Risk Using Lifestyle Factors**')

# DataFrame of features that impact the possibility of having a cardiovascular disease

st.write('Features that impact the possibility of having a cardiovascular disease are shown below:')
st.dataframe(model_features)

# Data input

st.write('**Please enter the following information to get the prediction. More information will return a more accurate prediction. Otherwise, the prediction will be based on the average values of the dataset:**')

# Widget values

select_cols = {
                'CDQ001': [0, 1],
                'MCQ160D': [0, 1],
                'CDQ010': [0, 1],
                'BPQ020': [1, 0],
                'BPQ090D': [1, 0],
                'MCQ300A': [0, 1],
                'RIAGENDR': [0, 1],
                'CDQ002': [1, 2, 3],
                'BPQ030': [1, 0],
                'MCQ160A': [1, 0],
                'CDQ008': [0, 1],
                'MCQ365C': [1, 0],
                'DMDEDUC2': [1, 2, 3, 4, 5],
              }

int_cols = {
                'INDFMIN2': [0, 100, 11],
                'RIDAGEYR': [0, 100, 57],
                'LBXTC': [0, 500, 185],
                'LBXSTR': [0, 500, 149],
                'BPXSY3': [0, 500, 125],
                'BPXDI1': [0, 200, 70],
                'LBXSCH': [0, 1000, 186],
                'LBXSIR': [0, 500, 83]
           }

float_cols = {
                'LBDSCRSI': [0.0, 300.0, 88.1504],
                'LBDHDDSI': [0.0, 10.0, 1.3617],
                'BMXWT': [0.0, 300.0, 83.6709],
                'LBDSUASI': [0.0, 1000.0, 334.5337],
                'BMXBMI': [0.0, 100.0, 30.0379],
                'LBDTCSI': [0.0, 50.0, 4.7434],
                'LBDSPHSI': [0.0, 10.0, 1.1783],
                'LBDSBUSI': [0.0, 20.0, 5.7012],
                'LBDSCHSI': [0.0, 50.0, 4.8053],
             }

meanings = {model_features['Feature'][i]: model_features['Variable Description'][i] for i in range(len(model_features))}


user_inputs = {}

# Select boxes

keys = list(select_cols.keys())

for i in range(len(keys)):
    if i % 2 == 0:
        pos = st.columns([0.75, 1.25])
    
    pos[i % 2].write(f"- {meanings[keys[i]]}:")
    user_inputs[keys[i]] =  pos[i % 2].selectbox(keys[i], select_cols[keys[i]], key = keys[i])

# Integer number inputs

keys = list(int_cols.keys())

for i in range(len(keys)):
    if i % 2 == 0:
        pos = st.columns([0.75, 1.25])
    
    pos[i % 2].write(f"- {meanings[keys[i]]}:")
    user_inputs[keys[i]] =  pos[i % 2].number_input(keys[i], value = int_cols[keys[i]][2], min_value = int_cols[keys[i]][0], max_value = int_cols[keys[i]][1], key = keys[i], step = 1)

# Float number inputs

st.write("**Examination Questions:**")

keys = list(float_cols.keys())

for i in range(len(keys)):
    if i % 2 == 0:
        pos = st.columns([0.75, 1.25])
    
    pos[i % 2].write(f"- {meanings[keys[i]]}:")
    user_inputs[keys[i]] =  pos[i % 2].number_input(keys[i], value = float_cols[keys[i]][2], min_value = float_cols[keys[i]][0], max_value = float_cols[keys[i]][1], key = keys[i], step = 1.0)

# Prediction

cols = ['RIDAGEYR', 'CDQ001', 'LBDSCRSI', 'MCQ160D', 'CDQ010', 'DMDEDUC2',
       'BPQ020', 'BPQ090D', 'LBDHDDSI', 'BMXWT', 'LBDSUASI', 'BMXBMI',
       'MCQ300A', 'MCQ160A', 'INDFMIN2', 'LBDTCSI', 'CDQ002', 'BPQ030',
       'LBDSPHSI', 'RIAGENDR', 'LBXTC', 'LBXSIR', 'CDQ008', 'LBXSTR',
       'LBDSBUSI', 'LBDSCHSI', 'BPXSY3', 'MCQ365C', 'BPXDI1', 'LBXSCH']

input = pd.DataFrame()

for key in user_inputs.keys():
    input[key] = [user_inputs[key]]
input = input[cols]

st.write(user_inputs)
st.dataframe(input)

st.write("**Prediction result:**")

if st.button('Predict'):
    if model.predict(input)[0] == 1:
        st.write(":red[**You have a high possibility to have cardiovascular disease. Please contact to your doctor for deep examination.**]")
    else:
        st.write(":green[**You have a low possibility to have cardiovascular disease. But please take examination every 6 months for your better health.**]")