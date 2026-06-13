import joblib
import pandas as pd

# 1. Yerel modeli İNTERNETSİZ olarak okuyor
yuklenen_model = joblib.load('sinerji_offline_model.pkl')

print("=" * 50)
print("SİNERJİ - İNTERAKTİF KARAR DESTEK SİSTEMİNE HOŞ GELDİNİZ")
print("=" * 50)

# 2. SİSTEM ARTIK SİZE SORU SORUYOR (İnteraktif Kısım)
sicaklik = float(input("🌡️ Hava sıcaklığı kaç derece? (Örn: 15.5): "))
yagmur = float(input("🌧️ Yağış miktarı nedir? (mm cinsinden, yağmur yoksa 0 yazın): "))
saat = int(input("⏰ Saat kaç? (0-23 arası bir saat girin): "))
haftasonu = int(input("📅 Bugün hafta sonu mu? (Evet için 1, Hayır için 0 yazın): "))

# 3. Verdiğin cevapları modele gönderiyoruz
yeni_durum = pd.DataFrame({
    'temperature_2m (°C)': [sicaklik],
    'rain (mm)': [yagmur],
    'Saat': [saat],
    'Haftasonu': [haftasonu]
})

# 4. Model anlık tahmin yapıyor
tahmin_edilen_hiz = yuklenen_model.predict(yeni_durum)[0]

print("\n" + "-" * 50)
print("📦 Lojistik Filosu Karar Destek Çıktısı - Fatih Bölgesi")
print(f"Tahmini Ortalama Trafik Hızı: {tahmin_edilen_hiz:.2f} km/s")
print("-" * 50)

# 5. Aksiyon Kararı
if tahmin_edilen_hiz < 25:
    print("🚨 SİSTEM ÖNERİSİ: KRİTİK YOĞUNLUK!")
    print("Maliyet Analizi: %40 ekstra rölanti yakıtı riski.")
    print("Aksiyon: Sevkiyatları erteleyin veya alternatif rota kullanın.")
elif tahmin_edilen_hiz < 40:
    print("⚠️ SİSTEM ÖNERİSİ: ORTA YOĞUNLUK!")
    print("Aksiyon: Teslimat sürelerine +15 dakika opsiyon ekleyin.")
else:
    print("✅ SİSTEM ÖNERİSİ: AKICI TRAFİK!")
    print("Aksiyon: Rota açık, standart operasyona devam edebilirsiniz.")