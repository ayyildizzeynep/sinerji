import streamlit as st
import pandas as pd
import joblib

# Sayfa ayarları
st.set_page_config(page_title="Sinerji Karar Destek", page_icon="📦")

# 1. Modeli yükle
# Not: Yönerge gereği model lokalden offline çalışıyor
model = joblib.load('sinerji_offline_model.pkl')

st.title("SİNERJİ")
st.subheader("İnteraktif Lojistik Karar Destek Sistemi")
st.markdown("---")

# 2. Kullanıcıdan veri alma (Web Arayüzü Bileşenleri)
col1, col2 = st.columns(2)

with col1:
    sicaklik = st.number_input("🌡️ Hava sıcaklığı kaç derece?", value=15.0, step=0.5)
    yagmur = st.number_input("🌧️ Yağış miktarı nedir? (mm)", value=0.0, step=1.0)

with col2:
    saat = st.slider("⏰ Saat kaç?", min_value=0, max_value=23, value=12)
    haftasonu_secim = st.radio("📅 Bugün hafta sonu mu?", ["Hayır", "Evet"])
    # "Evet" ise 1, "Hayır" ise 0 yapıyoruz
    haftasonu = 1 if haftasonu_secim == "Evet" else 0

st.markdown("---")

# 3. Tahmin Butonu
if st.button("🚀 Trafik Durumunu Tahmin Et", use_container_width=True):
    # Verileri modelin beklediği formata (DataFrame) çeviriyoruz
    yeni_durum = pd.DataFrame({
        'temperature_2m (°C)': [sicaklik],
        'rain (mm)': [yagmur],
        'Saat': [saat],
        'Haftasonu': [haftasonu]
    })

    # Model tahmini yapıyor
    tahmin_edilen_hiz = model.predict(yeni_durum)[0]

    # Sonucu ekranda göster
    st.success(f"📦 Lojistik Filosu İçin Fatih Bölgesi Çıktısı")
    st.metric(label="Tahmini Ortalama Trafik Hızı", value=f"{tahmin_edilen_hiz:.2f} km/s")