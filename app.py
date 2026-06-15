import streamlit as st
import pandas as pd
import plotly.express as px
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from io import BytesIO

st.title("💸 SmartSpend")

uploaded_file = st.file_uploader(
    "📂 Harcama Excel dosyanızı yükleyin",
    type=["xlsx"]
)

if uploaded_file is not None:
    veri = pd.read_excel(uploaded_file)
else:
    st.warning("Lütfen bir Excel dosyası yükleyin.")
    st.stop()
veri["Tarih"] = pd.to_datetime(veri["Tarih"])

gelir_dosya = "data/gelir.xlsx"
gelir_veri = pd.read_excel(gelir_dosya)

st.write("Harcama verileri:")
st.dataframe(veri)

toplam_harcama = veri["Tutar"].sum()
toplam_gelir = gelir_veri["Gelir"].sum()
kalan_para = toplam_gelir - toplam_harcama
gunluk_ortalama = veri["Tutar"].mean()
tasarruf_orani = (kalan_para / toplam_gelir) * 100
en_yuksek_kategori = veri.groupby("Kategori")["Tutar"].sum().idxmax()

st.subheader("📊 Özet Bilgiler")
st.metric("Toplam Harcama", f"{toplam_harcama} TL")
st.metric("En Çok Harcanan Kategori", en_yuksek_kategori)
st.metric("Toplam Gelir", f"{toplam_gelir} TL")
st.metric("Kalan Para", f"{kalan_para} TL")
st.metric("Günlük Ortalama Harcama", f"{gunluk_ortalama:.2f} TL")
st.metric("Tasarruf Oranı", f"%{tasarruf_orani:.2f}")

st.subheader("🔍 Kategori Filtresi")

kategori_secimi = st.selectbox(
    "Bir kategori seç:",
    ["Tümü"] + list(veri["Kategori"].unique())
)

if kategori_secimi != "Tümü":
    filtreli_veri = veri[veri["Kategori"] == kategori_secimi]
else:
    filtreli_veri = veri

st.dataframe(filtreli_veri)

st.subheader("📊 Kategoriye Göre Harcama Grafiği")

kategori_toplam = veri.groupby("Kategori")["Tutar"].sum().reset_index()

grafik = px.bar(
    kategori_toplam,
    x="Kategori",
    y="Tutar",
    title="Kategori Bazında Toplam Harcama"
)

st.plotly_chart(grafik)

st.subheader("🥧 Harcama Dağılımı")

pasta = px.pie(
    kategori_toplam,
    names="Kategori",
    values="Tutar",
    title="Harcama Kategorilerinin Dağılımı"
)

st.plotly_chart(pasta)
st.subheader("💰 Gelir - Gider Karşılaştırması")

gelir_gider = pd.DataFrame({
    "Tür": ["Gelir", "Gider", "Kalan Para"],
    "Tutar": [toplam_gelir, toplam_harcama, kalan_para]
})

gelir_gider_grafik = px.bar(
    gelir_gider,
    x="Tür",
    y="Tutar",
    title="Gelir, Gider ve Kalan Para Karşılaştırması"
)

st.plotly_chart(gelir_gider_grafik)
st.subheader("📈 Günlük Harcama Eğilimi")

gunluk_harcama = veri.groupby("Tarih")["Tutar"].sum().reset_index()

cizgi_grafik = px.line(
    gunluk_harcama,
    x="Tarih",
    y="Tutar",
    markers=True,
    title="Günlük Harcama Değişimi"
)

st.plotly_chart(cizgi_grafik)
st.subheader("🤖 Akıllı Harcama Yorumu")

if st.button("Harcamalarımı Yorumla"):

    st.write("## 📌 Akıllı Harcama Analizi")

    kategori_toplam = veri.groupby("Kategori")["Tutar"].sum()

    en_buyuk = kategori_toplam.idxmax()
    en_buyuk_tutar = kategori_toplam.max()

    oran = (en_buyuk_tutar / toplam_harcama) * 100

    st.write(
        f"Harcamalarınızın %{oran:.1f}'i "
        f"{en_buyuk} kategorisinde gerçekleşmiştir."
    )

    st.write(
        f"Toplam geliriniz {toplam_gelir} TL, "
        f"toplam harcamanız ise {toplam_harcama} TL'dir."
    )

    st.write(
        f"Mevcut tasarruf oranınız %{tasarruf_orani:.1f} seviyesindedir."
    )

    if tasarruf_orani >= 30:
        st.success(
            "Bütçe yönetiminiz oldukça başarılı görünüyor."
        )

    elif tasarruf_orani >= 10:
        st.warning(
            "Tasarruf oranınız orta seviyede."
        )

    else:
        st.error(
            "Tasarruf oranınız düşük görünüyor."
        )

    if oran > 40:
        st.warning(
            f"{en_buyuk} kategorisi toplam harcamaların "
            f"%{oran:.1f}'ini oluşturuyor."
        )

    st.write("### 💡 Öneri")

    st.write(
        f"{en_buyuk} kategorisindeki harcamalarınızı "
        "bir miktar azaltmanız tasarruf oranınızı artırabilir."
    )
    st.subheader("📄 Finansal Analiz Raporu")

def pdf_raporu_olustur():
    buffer = BytesIO()

    pdf = canvas.Canvas(buffer, pagesize=A4)
    pdf.setTitle("SmartSpend Finansal Analiz Raporu")

    pdf.drawString(100, 800, "SmartSpend Finansal Analiz Raporu")
    pdf.drawString(100, 760, f"Toplam Gelir: {toplam_gelir} TL")
    pdf.drawString(100, 735, f"Toplam Harcama: {toplam_harcama} TL")
    pdf.drawString(100, 710, f"Kalan Para: {kalan_para} TL")
    pdf.drawString(100, 685, f"Tasarruf Orani: %{tasarruf_orani:.2f}")
    pdf.drawString(100, 660, f"En Cok Harcama Yapilan Kategori: {en_yuksek_kategori}")

    pdf.drawString(100, 620, "Oneri:")
    pdf.drawString(
        100,
        595,
        f"{en_yuksek_kategori} kategorisindeki harcamalarinizi azaltmak tasarrufu artirabilir."
    )

    pdf.save()
    buffer.seek(0)

    return buffer

pdf_dosyasi = pdf_raporu_olustur()

st.download_button(
    label="📥 PDF Raporu İndir",
    data=pdf_dosyasi,
    file_name="SmartSpend_Rapor.pdf",
    mime="application/pdf"
)