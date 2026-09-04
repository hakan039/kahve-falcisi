import os
import streamlit as st
from PIL import Image
from google import genai

# Sayfa ayarları
st.set_page_config(page_title="Yapay Zeka Kahve Falcısı", page_icon="🔮", layout="centered")

st.title("🔮 Yapay Zeka Kahve Falcısı ☕")
st.write("Fincanınızın fotoğrafını yükleyin, bilgilerinizi girin ve falınızı öğrenin!")
st.page_link("pages/1_Gizlilik_Politikasi.py", label="Gizlilik Politikası", icon="🔒")

# Yan Panel - Kişisel Bilgiler
st.sidebar.header("📜 Kişisel Bilgileriniz")
kullanici_adi = st.sidebar.text_input("Adınız:", placeholder="Örn: Hakan")
kullanici_yasi = st.sidebar.number_input("Yaşınız:", min_value=1, max_value=120, value=25)
kullanici_iliski = st.sidebar.selectbox("İlişki Durumunuz:", ["Bekar", "Evli", "İlişkisi Var", "Platonik", "Kafası Karışık"])
kullanici_odak = st.sidebar.text_input("Özellikle merak ettiğiniz bir konu var mı?", placeholder="Örn: Kariyer, Aşk, Para")

# Ana Ekran - Resim Yükleme
st.subheader("📸 Fincan Fotoğrafı")
yuklenen_resim = st.file_uploader("Kahve fincanının içini gösteren bir fotoğraf seçin...", type=["jpg", "jpeg", "png"])

if yuklenen_resim is not None:
    resim = Image.open(yuklenen_resim)
    st.image(resim, caption="Yüklenen Kahve Fincanı", use_container_width=True)

    # FAL BAKMA BUTONU
    if st.button("🔮 Falıma Bak!"):
        if not kullanici_adi:
            st.warning("Lütfen fal bakabilmem için adınızı girin.")
        elif not os.environ.get("GEMINI_API_KEY"):
            st.error("Hata: GEMINI_API_KEY bulunamadı. Lütfen terminalden API anahtarınızı tanımlayın.")
        else:
            with st.spinner("☕ Telveler süzülüyor... Lütfen bekleyin..."):
                try:
                    client = genai.Client()
                    
                    falci_komutu = (
                        f"Sen geleneksel, sezgileri çok güçlü bir Türk kahvesi falcısısın. "
                        f"Fal baktıran kişinin adı {kullanici_adi}, yaşı {kullanici_yasi}, ilişki durumu '{kullanici_iliski}'. "
                        f"Özellikle merak ettiği konu: '{kullanici_odak}'.\n\n"
                        f"Fotoğraftaki telveleri analiz et ve tamamen bu kişiye özel, samimi bir dille kahve falı bak. "
                        f"Yorumunu şu başlıklarla yaz:\n"
                        f"1. Genel Ruh Hali ve Semboller\n"
                        f"2. Aşk ve İlişkiler\n"
                        f"3. İş, Kariyer ve Para\n"
                        f"4. Merak Edilen Konu ({kullanici_odak})\n"
                        f"Güzel bir dilekle falı bitir."
                    )

                    response = client.models.generate_content(
                        model='gemini-3.5-flash',
                        contents=[resim, falci_komutu]
                    )
                    
                    st.success(f"✨ İşte Sana Özel Kahve Falın, {kullanici_adi}! ✨")
                    st.write(response.text)
                    
                except Exception as e:
                    st.error(f"Fal bakılırken teknik bir hata oluştu: {e}")
else:
    st.info("Falı başlatmak için lütfen yukarıdaki alandan bir fincan fotoğrafı yükleyin.")