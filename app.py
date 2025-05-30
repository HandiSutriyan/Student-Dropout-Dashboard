import os
import io
import streamlit as st

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

def categorize_risk(score, high_threshold, medium_threshold):
    if score >= high_threshold: 
        return "HIGH"
    elif score >= medium_threshold:
        return "MEDIUM"
    else:
        return "LOW"

MODEL = joblib.load("./model/model_xgb.pkl")
COURSE_LIST = {0:'- Pilih Kelas -', 33:'Biofuel Production Technologies', 171:'Animation and Multimedia Design', 8014:'Social Service (evening attendance)', 9003:'Agronomy', 9070:'Communication Design',
                   9085:'Veterinary Nursing', 9119:'Informatics Engineering', 9130:'Equinculture', 9147:'Management', 9238:'Social Service', 9254:'Tourism', 9500:'Nursing', 
                   9556: 'Oral Hygiene',  9670:'Advertising and Marketing Management', 9773:'Journalism and Communication', 9853:'Basic Education', 9991:'Management (evening attendance)'}
GENDER = {"Pria":1, "Wanita": 0}
BOOL = {'Ya':True,'Tidak':False}

st.set_page_config(page_title="Jaya Jaya Institut", layout="wide")
st.title("🧮 Prediksi Dropout Jaya Jaya Institut")
st.markdown("""Masukkan data-data siswa yang diminta pada form di bawah ini untuk melakukan prediksi potensi dropoutnya""")

st.divider()
col1, col2 = st.columns(2)
col1.subheader("👤 Biodata Siswa")
name = col1.text_input("Nama Siswa")
gender = col1.radio("Jenis Kelamin", list(GENDER.keys()), key='Gender')
course = col1.selectbox("Kelas yang diikuti", list(COURSE_LIST.values()))
if course == '- Pilih Kelas -':
    col1.error('Pilih Kelas terlebih dahulu')
course_id = [key for key, value in COURSE_LIST.items() if value == course][0]
age = col1.number_input("Usia saat mendaftar", key='Age_at_enrollment', min_value=5, max_value=100, step=1, format='%d')

col2.subheader("💵 Finansial Siswa")
tuition = col2.radio("Apakah siswa sudah melunasi biaya pendidikan terakhir?", list(BOOL.keys()), key='Tuition_fees_up_to_date')
scholarship = col2.radio("Apakah siswa merupakan penerima beasiswa?", list(BOOL.keys()), key='Scholarship_holder')
debtor = col2.radio("Apakah siswa merupakan debitur (penerima kredit)?", list(BOOL.keys()),key='Debtor')

col3,col4 = st.columns(2)


col3.subheader("🎓 Akademik Semester I")
Curricular_units_1st_sem_enrolled = col3.number_input('Jumlah mata kuliah yang diregistrasi',key='Curricular_units_1st_sem_enrolled', min_value=0, max_value=100, step=1, format='%d')                
Curricular_units_1st_sem_approved = col3.number_input("Jumlah Mata Kuliah yang lulus",key='Curricular_units_1st_sem_approved', min_value=0, max_value=100, step=1, format='%d')

col4.subheader("🎓 Akademik Semester II")
Curricular_units_2nd_sem_approved = col4.number_input("Jumlah Mata Kuliah yang lulus", key = 'Curricular_units_2nd_sem_approved', min_value=0, max_value=100, step=1, format='%d')
Curricular_units_2nd_sem_credited = col4.number_input("Jumlah Mata kuliah yang diikuti", key='Curricular_units_2nd_sem_credited', min_value=0, max_value=100, step=1, format='%d')               
Curricular_units_2nd_sem_without_evaluations = col4.number_input("Jumlah mata kuliah yang tidak dievaluasi", key='Curricular_units_2nd_sem_without_evaluations', min_value=0, max_value=100, step=1, format='%d')
Curricular_units_2nd_sem_grade = col4.number_input("Nilai akhir", key='Curricular_units_2nd_sem_grade')

input_data = {
    '﻿Marital_status': 1, 
    'Application_mode': 18, 
    'Application_order': 1, 
    'Course': course_id,
    'Daytime_evening_attendance': 1, 
    'Previous_qualification': 1,
    'Previous_qualification_grade': 132.6, 
    'Nacionality': 1, 
    'Mothers_qualification':19,
    'Fathers_qualification':22, 
    'Mothers_occupation': 10, 
    'Fathers_occupation': 10,
    'Admission_grade':126.97,
    'Displaced': True, 
    'Educational_special_needs': False, 
    'Debtor': BOOL[debtor],
    'Tuition_fees_up_to_date': BOOL[tuition], 
    'Gender': GENDER[gender], 
    'Scholarship_holder': BOOL[scholarship],
    'Age_at_enrollment': int(age), 
    'International': False,
    'Curricular_units_1st_sem_credited': 0,
    'Curricular_units_1st_sem_enrolled': int(Curricular_units_1st_sem_enrolled),
    'Curricular_units_1st_sem_evaluations':8,
    'Curricular_units_1st_sem_approved': int(Curricular_units_1st_sem_approved), 
    'Curricular_units_1st_sem_grade': 10.64,
    'Curricular_units_1st_sem_without_evaluations': 0,
    'Curricular_units_2nd_sem_credited': int(Curricular_units_2nd_sem_credited),
    'Curricular_units_2nd_sem_enrolled': 6,
    'Curricular_units_2nd_sem_evaluations': 8,
    'Curricular_units_2nd_sem_approved': int(Curricular_units_2nd_sem_approved), 
    'Curricular_units_2nd_sem_grade': Curricular_units_2nd_sem_grade,
    'Curricular_units_2nd_sem_without_evaluations': int(Curricular_units_2nd_sem_without_evaluations), 
    'Unemployment_rate':11.56,
    'Inflation_rate': 1.2, 
    'GDP': 0.0019
}
input_df = pd.DataFrame([input_data])

st.divider()
if st.button("✨ **JALANKAN PREDIKSI SEKARANG**"):
        
    dropout_predict = MODEL.predict(input_df)[0]
    dropout_prob = MODEL.predict_proba(input_df)[0][1]
    risk_level = categorize_risk(dropout_prob,0.6,0.2084) 

    st.markdown("""## 🧠 Hasil Prediksi""")
    st.write(f"Nama: {name} | Kelas: {course} | Usia saat mendaftar: {int(age)}")
    col1, col2, col3 = st.columns(3)
    col1.metric("Diprediksi Dropout?", [key for key, value in BOOL.items() if value == bool(dropout_predict)][0])
    col2.metric("Probabilitas",f'{dropout_prob:.2f}')
    col3.metric("Tingkat Risiko", risk_level)
