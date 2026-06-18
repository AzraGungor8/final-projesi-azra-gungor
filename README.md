# final-projesi-azra-gungor
# 💸 SmartSpend

## Problem Tanımı

Birçok kişi gelir ve giderlerini düzenli analiz edemediği için bütçesini verimli yönetememektedir. Bu proje kullanıcıların harcamalarını analiz ederek karar desteği sunmayı amaçlamaktadır.

## Hedef Kullanıcı

* Üniversite öğrencileri
* Bireysel kullanıcılar
* Bütçesini takip etmek isteyen kişiler

## Çözümün Kısa Açıklaması

SmartSpend, Excel dosyalarından alınan gelir ve harcama verilerini analiz eden, grafikler oluşturan, akıllı öneriler sunan ve finansal rapor oluşturabilen etkileşimli bir veri panelidir.

## Kullanılan Teknolojiler

* Python
* Streamlit
* Pandas
* Plotly
* ReportLab

## Sistem Mimarisi

Excel Dosyaları → Veri Analizi → Grafikler → Akıllı Yorum Sistemi → PDF Raporu

## Kurulum

```bash
pip install streamlit pandas plotly openpyxl reportlab
python -m streamlit run app.py
```

## Kullanım

1. Harcama Excel dosyasını yükleyin.
2. Gelir bilgileri kullanılarak analizler oluşturulur.
3. Grafikler ve göstergeler görüntülenir.
4. Akıllı öneriler alınır.
5. PDF raporu indirilebilir.

## Özellikler

* Toplam gelir ve gider analizi
* Tasarruf oranı hesaplama
* Kategori filtreleme
* Pasta grafiği
* Sütun grafiği
* Gelir-gider karşılaştırması
* Günlük harcama eğilimi
* Akıllı yorum sistemi
* PDF raporu oluşturma

## Bilinen Sınırlılıklar

* Gelir verisi tek Excel dosyasından okunmaktadır.
* Gerçek zamanlı banka entegrasyonu bulunmamaktadır.

## Gelecekteki Geliştirmeler

* Yapay zekâ destekli gelişmiş öneriler
* Mobil uygulama desteği
* Çoklu kullanıcı sistemi
* Banka API entegrasyonu

## Yapay Zekâ Araçları

Kod geliştirme sürecinde ChatGPT'den destek alınmıştır.
## Tanıtım Videosu

Video bağlantısı:

https://youtu.be/ka7U2URiEF4
