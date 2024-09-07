import streamlit as st
import numpy as np
import pickle

# Muat model
with open("model_numpy.pkl", "rb") as model_file:
    model = pickle.load(model_file)

def main():
    st.title("Weather Prediction")
    st.sidebar.title("Weather Type")
    st.sidebar.write('1. Rainy')
    st.sidebar.write('2. Cloudy')
    st.sidebar.write('3. Sunny')
    st.sidebar.write('4. Snowy')

    # Mengambil input dari pengguna
    col1, col2 = st.columns(2)

    with col1:
        temperature = st.text_input('Temperature/Temperatur', '0.0')
    with col2:
        humidity = st.text_input('Humidity/Kelembaban', '0')
    with col1:
        wind_speed = st.text_input('Wind Speed/Kecepatan Angin', '0.0')
    with col2:
        precipitation = st.text_input('Precipitation/Curah Hujan', '0.0')
    with col1:
        cloud_cover = st.text_input('Cloud Cover/Tutupan Awan', '0')
    with col2:
        atmospheric_pressure = st.text_input('Atmospheric Pressure/Tekanan Atmosfer', '0.0')
    with col1:
        uv_index = st.text_input('UV Index/Indeks UV', '0')
    with col2:
        season = st.text_input('Season/Musim', '0')
    with col1:
        visibility = st.text_input('Visibility/Visibilitas (km)', '0.0')
    with col2:
        location = st.text_input('Location/Lokasi', '0')

    # Variabel default untuk hasil prediksi
    weather_type_label = None

    # Tombol prediksi
    if st.button("Weather Prediction"):
        try:
            # Mengonversi input ke tipe numerik
            user_input = np.array([
                float(temperature), float(humidity), float(wind_speed),
                float(precipitation), float(cloud_cover), float(atmospheric_pressure),
                float(uv_index), float(season), float(visibility), float(location)
            ])

            # Memastikan user_input adalah array 2D
            user_input = np.expand_dims(user_input, axis=0)

            # Debug: Menampilkan data input untuk verifikasi
            st.write("User Input Array:", user_input)

            # Prediksi
            prediction = model.predict(user_input)

            # Menentukan label cuaca berdasarkan prediksi
            if prediction[0] == 1:
                weather_type_label = 'Rainy'
            elif prediction[0] == 2:
                weather_type_label = 'Cloudy'
            elif prediction[0] == 3:
                weather_type_label = 'Sunny'
            else:
                weather_type_label = 'Snowy'

        except ValueError as e:
            st.error(f"Error in input values: {e}")
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")
        
        # Menggunakan try dan except untuk menangani kemungkinan kesalahan konversi dan memberi tahu jika ada input yang tidak valid.

    # Menampilkan hasil prediksi setelah tombol diklik
    if weather_type_label:
        st.write(f"Predicted Weather Type: {weather_type_label}")

if __name__ == "__main__":
    main()
