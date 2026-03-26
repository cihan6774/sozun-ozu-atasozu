import streamlit as st

# Sayfa ayarı
st.set_page_config(page_title="Sözün Özü, Atasözü", layout="centered")

st.title("📘 Sözün Özü, Atasözü")

# ---------------- OTURUM DEĞİŞKENLERİ ----------------
if "puan" not in st.session_state:
    st.session_state.puan = 0

if "soru_no" not in st.session_state:
    st.session_state.soru_no = 0

if "cevaplandi" not in st.session_state:
    st.session_state.cevaplandi = False

if "sonuc_mesaji" not in st.session_state:
    st.session_state.sonuc_mesaji = ""

if "sonuc_tipi" not in st.session_state:
    st.session_state.sonuc_tipi = ""

# ---------------- VERİLER ----------------
atasozu_sozlugu = {
    "Ağaç yaşken eğilir": "İnsan küçük yaşta eğitilmelidir.",
    "Damlaya damlaya göl olur": "Küçük birikimler zamanla büyür.",
    "Sakla samanı, gelir zamanı": "Gereksiz görülen şeyler ileride işe yarar.",
    "İşleyen demir ışıldar": "Çalışan insan körelmez.",
    "Ne ekersen onu biçersin": "Yapılan davranışların sonucu yaşanır."
}

oyun_sorulari = [
    {
        "soru": "Ağaç yaşken ...",
        "secenekler": ["eğilir", "kurur", "büyür"],
        "dogru": "eğilir"
    },
    {
        "soru": "Damlaya damlaya ...",
        "secenekler": ["taş olur", "göl olur", "sel olur"],
        "dogru": "göl olur"
    },
    {
        "soru": "Sakla samanı, ...",
        "secenekler": ["gelir zamanı", "olmaz zamanı", "biter zamanı"],
        "dogru": "gelir zamanı"
    },
    {
        "soru": "İşleyen demir ...",
        "secenekler": ["paslanır", "ışıldar", "kırılır"],
        "dogru": "ışıldar"
    },
    {
        "soru": "Ne ekersen onu ...",
        "secenekler": ["bulursun", "biçersin", "toplarsın"],
        "dogru": "biçersin"
    }
]

# ---------------- YARDIMCI FONKSİYONLAR ----------------
def sonraki_soru():
    if st.session_state.soru_no < len(oyun_sorulari) - 1:
        st.session_state.soru_no += 1
        st.session_state.cevaplandi = False
        st.session_state.sonuc_mesaji = ""
        st.session_state.sonuc_tipi = ""

def onceki_soru():
    if st.session_state.soru_no > 0:
        st.session_state.soru_no -= 1
        st.session_state.cevaplandi = False
        st.session_state.sonuc_mesaji = ""
        st.session_state.sonuc_tipi = ""

def oyunu_sifirla():
    st.session_state.puan = 0
    st.session_state.soru_no = 0
    st.session_state.cevaplandi = False
    st.session_state.sonuc_mesaji = ""
    st.session_state.sonuc_tipi = ""

# ---------------- MENÜ ----------------
menu = st.radio(
    "Menüden bir bölüm seç:",
    ("📖 Atasözü Sözlüğü", "🎮 Atasözünü Tamamla", "✍️ Hikâye Yaz", "ℹ️ Proje Hakkında")
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

    soru = oyun_sorulari[st.session_state.soru_no]

    st.write(f"**Soru {st.session_state.soru_no + 1}/{len(oyun_sorulari)}:** {soru['soru']}")

    secim = st.radio(
        "Doğru cevabı seç:",
        soru["secenekler"],
        key=f"secim_{st.session_state.soru_no}"
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Cevabı Kontrol Et"):
            if not st.session_state.cevaplandi:
                if secim == soru["dogru"]:
                    st.session_state.puan += 1
                    st.session_state.sonuc_mesaji = "Doğru ✔"
                    st.session_state.sonuc_tipi = "success"
                else:
                    st.session_state.sonuc_mesaji = f"Yanlış ❌ Doğru cevap: {soru['dogru']}"
                    st.session_state.sonuc_tipi = "error"

                st.session_state.cevaplandi = True
            else:
                st.session_state.sonuc_mesaji = "Bu soru zaten değerlendirildi. Sonraki soruya geçebilirsin."
                st.session_state.sonuc_tipi = "info"

    with col2:
        st.button("⬅️ Önceki", on_click=onceki_soru)

    with col3:
        st.button("Sonraki ➡️", on_click=sonraki_soru)

    if st.session_state.sonuc_mesaji:
        if st.session_state.sonuc_tipi == "success":
            st.success(st.session_state.sonuc_mesaji)
        elif st.session_state.sonuc_tipi == "error":
            st.error(st.session_state.sonuc_mesaji)
        else:
            st.info(st.session_state.sonuc_mesaji)

    st.markdown(f"### 🧮 Puanın: **{st.session_state.puan}**")

    if st.button("🔄 Oyunu Sıfırla"):
        oyunu_sifirla()
        st.rerun()

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

    if st.button("Hikâyeyi Göster"):
        if hikaye.strip() == "":
            st.warning("Lütfen bir hikâye yaz.")
        else:
            st.success("Hikâyen başarıyla oluşturuldu! ✨")
            st.write("### Yazdığın Hikâye")
            st.write(f"**Seçilen atasözü:** {secilen}")
            st.write(hikaye)

# ---------------- PROJE HAKKINDA ----------------
elif menu == "ℹ️ Proje Hakkında":
    st.subheader("ℹ️ Proje Hakkında")
    st.write("""
Bu uygulama, atasözlerini oyunlaştırma ve yaratıcı yazma etkinlikleriyle
öğretmek amacıyla hazırlanmıştır.

**Amaç:** Öğrencilerin atasözlerini anlamlandırma, günlük yaşamla ilişkilendirme
ve yaratıcı biçimde kullanma becerilerini geliştirmektir.
""")
