# Analisis Data Prediksi Sakit Jantung menggunakan Regresi Logistik

## Pendahuluan
Proyek ini bertujuan untuk memprediksi kemungkinan seseorang menderita penyakit jantung berdasarkan berbagai faktor risiko menggunakan model regresi logistik. Analisis ini dilakukan menggunakan dataset yang berisi data medis dari pasien.

## Dataset
Dataset yang digunakan dalam proyek ini dapat ditemukan di [Kaggle: Heart Failure Prediction](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction). Dataset ini mencakup atribut berikut:
- Age: Usia pasien
- Sex: Jenis kelamin pasien (1 = Pria, 0 = Wanita)
- ChestPainType: Tipe nyeri dada (0 = Typical Angina, 1 = Atypical Angina, 2 = Non-anginal Pain, 3 = Asymptomatic)
- RestingBP: Tekanan darah saat istirahat
- Cholesterol: Kolesterol dalam mg/dl
- FastingBS: Gula darah puasa > 120 mg/dl (1 = True, 0 = False)
- RestingECG: Hasil elektrokardiografi saat istirahat (0 = Normal, 1 = Memiliki kelainan ST-T, 2 = Menunjukkan kemungkinan atau pasti hipertrofi ventrikel kiri)
- MaxHR: Denyut jantung maksimum
- ExerciseAngina: Angina yang diinduksi oleh latihan (1 = Yes, 0 = No)
- Oldpeak: Depresi ST diinduksi oleh latihan relatif terhadap istirahat
- ST_Slope: Kemiringan puncak segmen ST latihan (0 = Upsloping, 1 = Flat, 2 = Downsloping)
- HeartDisease: Diagnosis penyakit jantung (1 = Ya, 0 = Tidak)

## Prasyarat
Untuk menjalankan analisis ini, pastikan Anda telah menginstal paket-paket berikut:
- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn
- streamlit

Anda dapat menginstal semua prasyarat menggunakan perintah berikut:
```bash
pip install pandas numpy scikit-learn matplotlib seaborn streamlit
