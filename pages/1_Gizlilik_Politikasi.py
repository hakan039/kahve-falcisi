import streamlit as st


st.set_page_config(page_title="Gizlilik Politikası", page_icon="🔒", layout="centered")

st.title("🔒 Gizlilik Politikası")
st.caption("Son güncelleme: 4 Eylül 2026")

st.markdown(
    """
Bu politika, Yapay Zeka Kahve Falcısı uygulamasının kişisel bilgileri ve
yüklenen görselleri nasıl işlediğini açıklar.

## 1. İşlenen bilgiler

Fal oluşturmak için aşağıdaki bilgiler uygulamaya girilebilir:

- Adınız, yaşınız ve ilişki durumunuz
- Merak ettiğiniz konu
- Yüklediğiniz kahve fincanı görseli

Bu bilgiler fal yorumunu kişiselleştirmek amacıyla kullanılır. Uygulama bu
bilgileri kendi bünyesinde kalıcı bir kullanıcı hesabına veya veritabanına
kaydetmez.

## 2. Üçüncü taraf hizmetler

Fal yorumunu oluşturmak için Google Gemini API kullanılır. Girdiğiniz bilgiler
ve fincan görseli, yalnızca bu hizmetten yanıt alınması amacıyla Google'a
aktarılır. Google'ın verileri nasıl işlediği, Google'ın güncel gizlilik
politikası ve Gemini API kullanım şartlarına tabidir.

## 3. Görsellerin saklanması

Yüklenen görseller uygulama tarafından kalıcı olarak saklanmaz. Görsel, analiz
tamamlandıktan sonra uygulamanın çalışma belleğinden çıkarılır. İnternet
üzerinden gönderilen verilerin üçüncü taraf hizmetlerdeki saklama süresi,
ilgili hizmetin kendi politikalarına göre belirlenir.

## 4. Güvenlik ve sorumluluk

Uygulamayı kullanırken kimlik, iletişim, finans, sağlık veya başka hassas
kişisel bilgileri fincan görseline ya da metin alanlarına eklemeyin. Kahve
falı eğlence amaçlıdır ve sağlık, hukuk veya finansal kararlar için tavsiye
olarak değerlendirilmemelidir.

## 5. İletişim

Bu politika hakkında sorularınız veya talepleriniz için uygulamanın
yayınlandığı platformdaki iletişim kanalını kullanabilirsiniz.
"""
)
