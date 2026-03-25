import streamlit as st
import random
import gspread
from google.oauth2.service_account import Credentials

scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

creds_dict = dict(st.secrets["gcp_service_account"])
creds = Credentials.from_service_account_info(creds_dict, scopes=scope)
client = gspread.authorize(creds)

sheet = client.open("atasozu_veriler").sheet1

atasozleri = {
    "Ağaç yaşken eğilir": "İnsan küçük yaşta eğitilmelidir.",
    "Damlaya damlaya göl olur": "Küçük birikimler zamanla büyür.",
    "İşleyen demir ışıldar": "Çalışan insan dinç kalır.",
    "Komşu komşunun külüne muhtaçtır": "İnsanlar birbirine ihtiyaç duyar.",
    "Ne ekersen onu biçersin": "Yaptıklarının karşılığını görürsün."
}


# ---------------- AYARLAR ----------------
st.set_page_config(page_title="Sözün Özü, Atasözü", layout="centered")
st.title("📘 Sözün Özü, Atasözü")

# ---------------- OTURUM DEĞİŞKENLERİ ----------------
if "puan" not in st.session_state:
    st.session_state.puan = 0

if "soru_no" not in st.session_state:
    st.session_state.soru_no = 0

# ---------------- VERİLER ----------------

# Atasözü – anlam (sözlük)
atasozu_sozlugu = {
    "Ağaç yaşken eğilir": "İnsan küçük yaşta eğitilmelidir.",
    "Damlaya damlaya göl olur": "Küçük birikimler zamanla büyür.",
    "Sakla samanı, gelir zamanı": "Gereksiz görülen şeyler ileride işe yarar.",
    "İşleyen demir ışıldar": "Çalışan insan körelmez.",
    "Ne ekersen onu biçersin": "Yaptıklarının karşılığını görürsün."
}

# OYUN SORULARI (20 SORU)
oyun_sorulari = [
    ("Ağaç yaşken ...", ["eğilir", "kurur", "büyür"], "eğilir"),
    ("Damlaya damlaya ...", ["taş olur", "göl olur", "kum olur"], "göl olur"),
    ("Sakla samanı, ...", ["gerekmez", "yok olur", "gelir zamanı"], "gelir zamanı"),
    ("Ayağını yorganına göre ...", ["koş", "uzat", "sar"], "uzat"),
    ("İşleyen demir ...", ["pas tutmaz", "kırılır", "kararır"], "pas tutmaz"),
    ("Balık baştan ...", ["büyür", "kokar", "yüzer"], "kokar"),
    ("Ne ekersen onu ...", ["yersin", "biçersin", "bulursun"], "biçersin"),
    ("Dost kara günde ...", ["belli olur", "kaçır", "susar"], "belli olur"),
    ("Gülme komşuna, ...", ["ayıp olur", "gelir başına", "ayıp sayılır"], "gelir başına"),
    ("Taşıma suyla ...", ["iş yapılır", "değirmen dönmez", "yol alınmaz"], "değirmen dönmez"),
    ("Borç yiğidin ...", ["yüküdür", "kamçısıdır", "düşmanıdır"], "kamçısıdır"),
    ("Erken kalkan ...", ["yorulur", "yol alır", "yanılır"], "yol alır"),
    ("Acele işe ...", ["bereket girer", "şeytan karışır", "zaman yetmez"], "şeytan karışır"),
    ("Az veren candan, ...", ["çok veren maldan", "az alan yoldan", "çok alan kardan"], "çok veren maldan"),
    ("Keskin sirke ...", ["küpe zarar", "ağza zarar", "tadı bozar"], "küpe zarar"),
    ("Ev alma, ...", ["para al", "komşu al", "yol al"], "komşu al"),
    ("Bir elin nesi var, ...", ["çoktur", "iki elin sesi var", "gücü var"], "iki elin sesi var"),
    ("Söz gümüşse ...", ["altın olur", "susmak iyidir", "sükût altındır"], "sükût altındır"),
    ("İki cambaz bir ...", ["ipte oynamaz", "yolda kalmaz", "işte durmaz"], "ipte oynamaz"),
    ("Komşu komşunun ...", ["evine bakar", "külüne muhtaçtır", "sözünü dinler"], "külüne muhtaçtır")
]

# ---------------- MENÜ ----------------
menu = st.radio(
    "Menüden bir bölüm seç:",
    ("📖 Atasözü Sözlüğü", "🎮 Atasözünü Tamamla", "✍️ Hikâye Yaz", "📱 QR Kod", "ℹ️ Proje Hakkında")
)

# ---------------- SÖZLÜK ----------------
if menu == "📖 Atasözü Sözlüğü":
    st.subheader("📖 Atasözü Sözlüğü")
    for soz, anlam in atasozu_sozlugu.items():
        st.write(f"**{soz}**")
        st.write(anlam)
        st.write("---")

# ---------------- OYUN ----------------
elif menu == "🎮 Atasözünü Tamamla":
    st.subheader("🎮 Atasözünü Tamamla (Çoktan Seçmeli)")

    soru, secenekler, dogru = oyun_sorulari[st.session_state.soru_no]

    st.write(f"**Soru {st.session_state.soru_no + 1}/20:** {soru}")
    secim = st.radio("Doğru seçeneği işaretle:", secenekler, key=st.session_state.soru_no)

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Cevabı Kontrol Et"):
            if secim == dogru:
                st.success("Doğru ✔")
                st.session_state.puan += 1
            else:
                st.error(f"Yanlış ❌ Doğru cevap: {dogru}")

    with col2:
        if st.button("⬅️ Önceki") and st.session_state.soru_no > 0:
            st.session_state.soru_no -= 1

    with col3:
        if st.button("Sonraki ➡️") and st.session_state.soru_no < len(oyun_sorulari) - 1:
            st.session_state.soru_no += 1

    st.markdown(f"### 🧮 Puanın: **{st.session_state.puan}**")

    if st.button("🔄 Oyunu Sıfırla"):
        st.session_state.puan = 0
        st.session_state.soru_no = 0

# ---------------- HİKÂYE ----------------
elif menu == "✍️ Hikâye Yaz":
    st.subheader("✍️ Atasözü ile Hikâye Yazma")

    secilen = st.selectbox(
        "Bir atasözü seç:",
        list(atasozu_sozlugu.keys())
    )

    hikaye = st.text_area(
        "Bu atasözünün anlamını yansıtan kısa bir hikâye yaz:",
        height=200
    )

    if st.button("Hikâyeyi Kaydet"):
        if hikaye.strip() == "":
            st.warning("Lütfen bir hikâye yaz.")
        else:
            sheet.append_row([secilen, hikaye])
            st.success("Hikâye başarıyla kaydedildi! ✨")
            
# ---------------- QR Kod ----------------

elif menu == "📱 QR Kod":
    st.subheader("📱 Atasözleri için QR Kod")

    st.write("Bir atasözü seç, QR kodunu oluştur ve telefonla okut.")

    atasozleri_listesi = list(atasozleri.keys())

    secilen = st.selectbox("Atasözü seç:", atasozleri_listesi)

    # QR kodun yönleneceği adres (uygulama linkin)
    url = "http://localhost:8501"

    qr = qrcode.make(url)
    buf = BytesIO()
    qr.save(buf)

    st.image(buf, caption=secilen)


# ---------------- PROJE ----------------
elif menu == "ℹ️ Proje Hakkında":
    st.subheader("ℹ️ Proje Hakkında")
    st.write("""
    **Sözün Özü, Atasözü** projesi; atasözlerini dijital ortamda,
    oyunlaştırma ve yaratıcı yazma yöntemleriyle öğretmeyi amaçlamaktadır.

    Uygulama, Python ve Streamlit kullanılarak geliştirilmiştir.
    """)
