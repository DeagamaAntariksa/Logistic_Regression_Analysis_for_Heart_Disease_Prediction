import streamlit as st
import numpy as np
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_option_menu import option_menu

model = pickle.load(open('heart_disease_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))
coefficients = pickle.load(open('coefficients.pkl', 'rb'))

with st.sidebar:
    selected = option_menu(
        "Menu Utama",
        ["Deteksi Penyakit Jantung", "Analisis Koefisien Regresi"],
        icons=['heartbeat', 'bar-chart'],
        menu_icon="cast",
        default_index=0)

if selected == "Deteksi Penyakit Jantung":
    st.title('Prediksi Penyakit Jantung')

    st.sidebar.header('Masukkan Data Pasien')

    age = st.sidebar.number_input('Umur', 0, 120)
    sex = st.sidebar.selectbox('Jenis Kelamin', [0, 1], format_func=lambda x: 'Pria' if x == 1 else 'Wanita')
    cp_options = ['ASY', 'NAP', 'ATA', 'TA']
    cp = st.sidebar.selectbox('Tipe Nyeri Dada', cp_options)
    cp = cp_options.index(cp)

    restingbp = st.sidebar.number_input('Tekanan Darah Saat Istirahat', 0, 300)
    cholesterol = st.sidebar.number_input('Kolesterol', 0, 500)
    fastingbs = st.sidebar.selectbox('Gula Darah Puasa > 120 mg/dl', [0, 1], format_func=lambda x: 'Ya' if x == 1 else 'Tidak')
    restecg_options = ['Normal', 'LVH', 'ST']
    restecg = st.sidebar.selectbox('Hasil EKG Istirahat', restecg_options)
    restecg = restecg_options.index(restecg)

    maxhr = st.sidebar.number_input('Detak Jantung Maksimum yang Dicapai', 0, 250)
    exerciseangina = st.sidebar.selectbox('Angina Induksi Olahraga', [0, 1], format_func=lambda x: 'Ya' if x == 1 else 'Tidak')
    oldpeak = st.sidebar.number_input('Depresi ST yang Diinduksi oleh Olahraga', 0.0, 10.0)
    st_slope_options = ['Flat', 'Up', 'Down']
    st_slope = st.sidebar.selectbox('Slope Segmen ST', st_slope_options)
    st_slope = st_slope_options.index(st_slope)

    input_data = pd.DataFrame({
        'Age': [age],
        'Sex': [sex],
        'ChestPainType': [cp],
        'RestingBP': [restingbp],
        'Cholesterol': [cholesterol],
        'FastingBS': [fastingbs],
        'RestingECG': [restecg],
        'MaxHR': [maxhr],
        'ExerciseAngina': [exerciseangina],
        'Oldpeak': [oldpeak],
        'ST_Slope': [st_slope]
    })

    input_data_scaled = scaler.transform(input_data)

    if st.sidebar.button('Prediksi'):
        prediction = model.predict(input_data_scaled)
        prediction_proba = model.predict_proba(input_data_scaled)

        st.write(f"### Prediksi: {'Ada Penyakit Jantung' if prediction[0] == 1 else 'Tidak Ada Penyakit Jantung'}")
        st.write(f"### Probabilitas: {prediction_proba[0][1]:.2f}")

        labels = ['Tidak Ada Penyakit Jantung', 'Ada Penyakit Jantung']
        sizes = [prediction_proba[0][0], prediction_proba[0][1]]
        colors = ['#ff9999','#66b3ff']
        explode = (0.1, 0)

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')
        st.pyplot(fig1)

elif selected == "Analisis Koefisien Regresi":
    st.title("Analisis Koefisien Model Regresi Logistik")

    feature_names = ["Age", "Sex", "ChestPainType", "RestingBP", "Cholesterol", "FastingBS", "RestingECG", "MaxHR", "ExerciseAngina", "Oldpeak", "ST_Slope"]
    coef_df = pd.DataFrame(coefficients[0], index=feature_names, columns=['Koefisien'])
    st.write(coef_df)

    fig2, ax2 = plt.subplots()
    sns.barplot(x=coef_df['Koefisien'], y=coef_df.index, palette='coolwarm', ax=ax2)
    ax2.set_title('Analisis Koefisien Model')
    st.pyplot(fig2)
