import streamlit as st
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler

model = pickle.load(open('model.pkl', 'rb'))

def predict_disease(age, sex, chestPainType, restingBP, cholesterol, fastingBS, maxHR, exerciseAngina, oldPeak, st_Slope):
    input = {'Age': [age], 'Sex': [sex], 'ChestPainType': [chestPainType], 'RestingBP': [restingBP], 'Cholesterol': [cholesterol], 'FastingBS': [fastingBS], 'MaxHR': [maxHR], 'ExerciseAngina': [exerciseAngina], 'Oldpeak': [oldPeak], 'ST_Slope': [st_Slope]}
    
    input = pd.DataFrame(input)
    scaler = StandardScaler()
    input[['Age','RestingBP','Cholesterol','MaxHR','Oldpeak']] = scaler.fit_transform(input[['Age','RestingBP','Cholesterol','MaxHR','Oldpeak']])
    
    prediction = model.predict(input)
    print(type(prediction))
    return int(prediction)

def main():
    st.title("Heart Disease Prediction")
    html_temp = """
        <div>
        <h5 style="color: white;">
        Please input with Integer for the following attributes <br>
        </h5>
        
        <span style="color: #EF7C8E"> Gender </span> <br>
        F = 0 <br>
        M = 1 <br><br>
        <span style="color: #EF7C8E"> Chest Pain Type </span> <br>
        ASY = 0 <br>
        ATA = 1 <br>
        NAP = 2 <br><br>
        <span style="color: #EF7C8E"> Fasting Blood Sugar </span> <br>
        ASY = 0 <br>
        ATA = 1 <br>
        NAP = 2 <br><br>
        <span style="color: #EF7C8E"> Exercise Angina </span> <br>
        N = 0 <br>
        Y = 1 <br><br>
        <span style="color: #EF7C8E"> ST Slope </span> <br>
        Down = 0 <br>
        Flat = 1 <br>
        Up = 2
        </div>
    """

    st.markdown(html_temp, unsafe_allow_html=True)

    age = st.text_input("Age")
    sex = st.text_input("Gender (Female = 0, Male = 1)")
    chestPainType = st.text_input("Chest Pain Type (ASY = 0, ATA = 1, NAP = 2)")
    restingBP = st.text_input("Resting Blood Pressure")
    cholesterol = st.text_input("Cholesterol")
    fastingBS = st.text_input("Fasting Blood Sugar (FastingBS <= 120 mg/dl = 0, FastingBS > 120 mg/dl = 1)")
    maxHR = st.text_input("Max Heart Rate")
    exerciseAngina = st.text_input("Exercise Angina (No = 0, Yes = 1)")
    oldPeak = st.text_input("Old Peak")
    st_Slope = st.text_input("ST Slope (Down = 0, Flat = 1, Up = 2)")

    safe_html = """
        <div style="background-color: green; padding: 10px;">
        <h2 style="color: white; text-align: center;">You don't have heart disease</h2>
        </div>
    """

    danger_html = """
        <div style="background-color: red; padding: 10px;">
        <h2 style="color: white; text-align: center;">You have heart disease</h2>
        </div>
    """

    if st.button("Predict"):
        output = predict_disease(age, sex, chestPainType, restingBP, cholesterol, fastingBS, maxHR, exerciseAngina, oldPeak, st_Slope)

        if output == 1:
            st.markdown(danger_html, unsafe_allow_html=True)
        else:
            st.markdown(safe_html, unsafe_allow_html=True)

if __name__=='__main__':
    main()