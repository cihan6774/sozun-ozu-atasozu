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
    "Balık baştan kokar": "Bir topluluktaki bozulma, önce yöneticilerden veya üst mevkidekilerden başlar.",
    "Tatlı dil yılanı deliğinden çıkarır": "ert ve kırıcı olmayan, nazik ve yumuşak konuşmalar en inatçı kişileri bile ikna edebilir.",
    "Aba altında er yatar": "Kişilerin dış görünüşüne bakarak onların değerini veya yeteneğini küçümsememek gerekir..",
    "Ateş düştüğü yeri yakar": "Bir felaketin acısını gerçek anlamda sadece o felakete uğrayanlar hisseder.",
    "Dereyi görmeden paçaları sıvama": "Bir işin sonucunu kesin olarak görmeden hazırlıklara girişmek yanlıştır.",
    "Gülü seven dikenine katlanır": "Sevdiği bir işi veya kişiyi seçen, onun getireceği zorluklara da razı olmalıdır.",
    "Keskin sirke küpüne zarar": "Öfkeli ve asabi kimseler, bu tavırlarıyla en çok kendilerine zarar verirler.",
    "Minareyi çalan kılıfını hazırlar": "Hukuka aykırı veya gizli bir iş yapan kişi, yakalanmamak için önceden her türlü önlemi alır.",
    "Rüzgâr eken fırtına biçer": "Başkalarına kötülük yapanlar, yaptıklarının karşılığında çok daha büyük zararlar görürler..",
    "Üzüm üzüme baka baka kararır": "Birbirine yakın olan insanlar, zamanla birbirlerinin huyunu ve alışkanlıklarını kaparlar..",
    "Yalancının mumu yatsıya kadar yanar": "Söylenen yalanlar uzun süre gizli kalamaz, çok geçmeden ortaya çıkar..",
    "Demir tavında dövülür": "Bir işten istenilen sonucun alınabilmesi için o işin en uygun zamanda yapılması gerekir..",
    "Paça ıslanmadan balık tutulmaz": "Bir başarıya ulaşmak veya kazanç elde etmek için bazı zorlukları göze almak gerekir.",
    "Besle kargayı oysun gözünü": "Kıymet bilmeyen birine yapılan iyilik, gün gelir size zarar olarak dönebilir.",
    "Boş çuval dik durmaz": "Bilgisi veya yeteneği olmayan, içi boş bir insan toplumda tutunamaz..",
    "Sütten ağzı yanan yoğurdu üfleyerek yer": "Bir olaydan büyük zarar gören kişi, benzer durumlarda aşırı tedbirli davranır.",
    "Meyve veren ağacı taşlarlar": "Başarılı ve yetenekli kimselere karşı kıskançlık ve saldırılar eksik olmaz..",
    "Denize düşen yılana sarılır": "Çok çaresiz bir duruma düşen kişi, kurtulmak için hiç güvenmediği şeylerden bile yardım umar..",
    "Taş yerinde ağırdır": " İnsan, bulunduğu çevrede ve kendi makamında daha saygın ve etkili olur. .",
    "Yavru kuş yuvada gördüğünü yapar": "Çocuklar, ailelerinden gördükleri davranışları örnek alarak büyürler.",
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
    {
        "soru": "Ağaç yaş iken ...",
        "secenekler": ["kurur", "eğilir", "meyve verir"],
        "dogru": "eğilir"
    },
    {
        "soru": "Balık baştan ...",
        "secenekler": ["kokar", "yüzür", "avlanır"],
        "dogru": "kokar"
    },
    {
        "soru": "Tatlı dil yılanı ... çıkarır.",
        "secenekler": ["yuvasından", "deliğinden", "topraktan"],
        "dogru": "deliğinden"
    },
    {
        "soru": "Aba altında ... yatar.",
        "secenekler": ["er", "dev", "kuzu"],
        "dogru": "er"
    },
    {
        "soru": "Ateş düştüğü yeri ...",
        "secenekler": ["ısıtır", "yakar", "aydınlatır"],
        "dogru": "yakar"
    },
    {
        "soru": "Damlaya damlaya ... olur.",
        "secenekler": ["taş", "göl", "sel"],
        "dogru": "göl"
    },
    {
        "soru": "Dereyi görmeden ... sıvama.",
        "secenekler": ["kolları", "paçaları", "etekleri"],
        "dogru": "paçaları"
    },
    {
        "soru": "Gülü seven ... katlanır.",
        "secenekler": ["kokusuna", "dikenine", "rengine"],
        "dogru": "dikenine"
    },
    {
        "soru": "Keskin sirke ... zarar.",
        "secenekler": ["şişesine", "küpüne", "tadına"],
        "dogru": "küpüne"
    },
    {
        "soru": "Minareyi çalan ... hazırlar.",
        "secenekler": ["yerini", "kılıfını", "parasını"],
        "dogru": "kılıfını"
    },
    {
        "soru": "Rüzgâr eken ... biçer.",
        "secenekler": ["buğday", "fırtına", "yağmur"],
        "dogru": "fırtına"
    },
    {
        "soru": "Üzüm üzüme baka baka ...",
        "secenekler": ["sararır", "kararır", "tatlanır"],
        "dogru": "kararır"
    },
    {
        "soru": "Yalancının mumu ... kadar yanar.",
        "secenekler": ["akşama", "yatsıya", "sabaha"],
        "dogru": "yatsıya"
    },
    {
        "soru": "Demir ... dövülür.",
        "secenekler": ["ateşte", "tavında", "örste"],
        "dogru": "tavında"
    },
    {
        "soru": "Paça ıslanmadan ... tutulmaz.",
        "secenekler": ["balık", "tavşan", "ördek"],
        "dogru": "balık"
    },
    {
        "soru": "Besle kargayı oysun ...",
        "secenekler": ["elini", "gözünü", "yemini"],
        "dogru": "gözünü"
    },
    {
        "soru": "Boş çuval ... durmaz.",
        "secenekler": ["dik", "yan", "düz"],
        "dogru": "dik"
    },
    {
        "soru": "Sütten ağzı yanan yoğurdu ... yer.",
        "secenekler": ["soğuk", "üfleyerek", "kaşıkla"],
        "dogru": "üfleyerek"
    },
    {
        "soru": "Meyve veren ağacı ...",
        "secenekler": ["sularlar", "taşlarlar", "budarlar"],
        "dogru": "taşlarlar"
    },
    {
        "soru": "Denize düşen ... sarılır.",
        "secenekler": ["yılana", "osuna", "salına"],
        "dogru": "yılana"
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
