# TÜBİTAK 2209-A: Türk Kültürü Entegreli Beslenme Asistanı
## 6 Aylık (24 Hafta) 5 Kişilik Haftalık Görev Dağılımı ve İş Planı

### Proje Ekibi ve Rol Dağılımı

1. **Ahmet (`@AhmetElas-lab`) — ML / CV Lideri:** Bilgisayarlı Görü, Yemek Sınıflandırma, Porsiyon & Tabak Alanı Segmentasyonu, Model Eğitimi (YOLOv8-seg / MobileNetV3).
2. **Yağmur Sayın (`@yagmursayin`) — Proje Yürütücüsü & NLP/LLM Lideri:** Doğal Dil İşleme, Türk Kültürel Ölçü Dönüştürücüsü, RAG Tabanlı Akıllı Tarif Öneri Motoru, TÜBİTAK Süreç Yönetimi.
3. **ayss6502 (`@ayss6502`) — Veri Mühendisi & Domain Analisti:** TÜRKOMP Gıda Besin Değeri Veri Tabanı Entegrasyonu, Görsel Veri Toplama, Etiketleme & Veri Artırımı (Augmentation).
4. **hlnzmn (`@hlnzmn`) — Backend & MLOps Mühendisi:** FastAPI Sunucusu, REST API Uç Noktaları, Model Servisleme & Optimizasyon, Local PC Tünelleme (Ngrok/Cloudflare).
5. **zeynepkucuk23 (`@zeynepkucuk23`) — Mobil Geliştirici (Frontend / Flutter):** Flutter Mobil Uygulama, Kamera Entegrasyonu, Besin & Kalori Kartı UI, Kullanıcı Testleri.

---

## 1. AY: Altyapı, TÜRKOMP Veri Mimarisi ve İskelet Kurulumu

### 1. Hafta (Proje Başlangıcı & Ortam Senkronizasyonu)
- **Ahmet:** Açık kaynak yemek veri setlerinin incelenmesi (Food-101, Turkish Food Datasets); porsiyon kestirim mimarisinin teorik tasarımı.
- **Yağmur Sayın:** Türk mutfağına özgü ölçü birimleri ("kepçe", "avuç", "çimdik", "parmak", "tatlı kaşığı") sözlük yapısının belirlenmesi.
- **ayss6502:** TÜRKOMP veri tabanının taranması; ilk 100 popüler Türk yemeği listesinin çıkarılması.
- **hlnzmn:** FastAPI temel mimarisinin kurulması, Docker/sanal ortam konfigürasyonu ve Git branching kurallarının belirlenmesi.
- **zeynepkucuk23:** Flutter projesinin başlatılması, temel tema, fontlar ve sayfa navigasyon iskeletinin oluşturulması.

### 2. Hafta (Veri Tabanı Şeması & İlk UI Ekranları)
- **Ahmet:** U-Net ve YOLOv8-seg modellerinin karşılaştırmalı analizi; transfer learning için önceden eğitilmiş ağırlıkların seçimi.
- **Yağmur Sayın:** spaCy/HuggingFace tabanlı Türkçe metin işleme pipeline'ının taslağının hazırlanması.
- **ayss6502:** TÜRKOMP verilerinin standardize edilip JSON/SQLite formatına aktarılması (100 gramdaki kalori, protein, yağ, karbonhidrat).
- **hlnzmn:** `/health`, `/foods` temel CRUD API uç noktalarının yazılması ve Swagger dökümantasyonunun hazırlanması.
- **zeynepkucuk23:** Mobil uygulama Splash ve Ana Sayfa (Dashboard) ekran tasarımlarının kodlanması.

### 3. Hafta (Görsel Veri Arama & Ölçü Tablosu Kodlaması)
- **Ahmet:** Görsel veri toplama kriterlerinin (açı, ışık, tabak referansı) belirlenmesi ve etiketleme aracının (Roboflow) kurulması.
- **Yağmur Sayın:** Geleneksel ölçülerin gramaj eşleme tablosunun oluşturulması (`kepce -> 150ml/g`, `avuc -> 30-40g`).
- **ayss6502:** 100 Türk yemeği için açık kaynaklardan ve telifsiz kaynaklardan ilk görsel havuzunun (500+ fotoğraf) toplanması.
- **hlnzmn:** Pydantic veri modellerinin (`FoodItem`, `PortionRequest`, `NutritionalValue`) tanımlanması.
- **zeynepkucuk23:** Mobil uygulamada kamera izinlerinin ve kamera önizleme (preview) ekranının kodlanması.

### 4. Hafta (1. Ay Değerlendirmesi & Temel Entegrasyon)
- **Ahmet:** Roboflow üzerinde ilk 20 yemek sınıfının etiketleme şablonunun oluşturulması ve ekibe kılavuz hazırlanması.
- **Yağmur Sayın:** Kural tabanlı ölçü ayrıştırıcı Python modülünün yazılması ve ilk birim testlerinin (unit tests) yapılması.
- **ayss6502:** Toplanan görsellerin sınıflara göre klasörlenmesi ve veri temizleme (düşük çözünürlüklüleri ayıklama).
- **hlnzmn:** Ölçü dönüştürücü modülün API'ye `/api/v1/parse-portion` olarak bağlanması.
- **zeynepkucuk23:** Mobil uygulamadan çekilen fotoğrafın yerel belleğe kaydedilip boyutunun optimize edilmesi.

---

## 2. AY: Veri Etiketleme, RAG Tarif Altyapısı ve Kamera Servisi

### 5. Hafta (Veri Etiketleme Kampı)
- **Ahmet:** Yemek segmentasyonu (tabak sınırı ve yemek alanı) için poligon etiketleme çalışmalarının koordine edilmesi.
- **Yağmur Sayın:** 100 Türk yemeğine ait standart tarif metinlerinin toplanması (malzeme listeleri ve hazırlanış adımları).
- **ayss6502:** Roboflow üzerinde ilk 500 görselin etiketlenmesi (Çorbalar, Etli Yemekler, Zeytinyağlılar).
- **hlnzmn:** Görsel yükleme (`/api/v1/upload-image`) endpoint'inin yazılması, `python-multipart` ile güvenli dosya kabulü.
- **zeynepkucuk23:** Mobil arayüzde fotoğraf çekme ve galeriden seçme butonlarının fonksiyonel hale getirilmesi.

### 6. Hafta (RAG & Vektör Veritabanı Hazırlığı)
- **Ahmet:** Veri artırımı (Data Augmentation: döndürme, parlaklık, kesme) adımlarının pipeline'a eklenmesi.
- **Yağmur Sayın:** Tarif metinlerinin parçalanması (chunking) ve embedding modellerinin (Türkçe uyumlu) test edilmesi.
- **ayss6502:** Kalan 500 görselin etiketlenmesi; toplamda 1000 etiketli görsel havuzuna ulaşılması.
- **hlnzmn:** SQLite/ChromaDB üzerinde tarif vektör deposu entegrasyonu için servis katmanının hazırlanması.
- **zeynepkucuk23:** Mobil uygulamada "Evdeki Malzemeler" seçim arayüzünün (etiket/chip mantığında) kodlanması.

### 7. Hafta (Görsel İşleme Hattı & LLM Entegrasyonu)
- **Ahmet:** YOLOv8-seg modelinin yerel GPU üzerinde ilk ön-eğitim (pre-training) denemesinin başlatılması.
- **Yağmur Sayın:** LLM (Llama 3 / DeepSeek / Gemini API) için "Türk Şef Asistanı" sistem promptunun yazılması ve test edilmesi.
- **ayss6502:** Veri setinin Train (%70), Validation (%15) ve Test (%15) olarak ayrılması; sınıf dengesizliklerinin raporlanması.
- **hlnzmn:** LLM API anahtarlarının ve çevre değişkenlerinin (`.env`) backend mimarisine güvenli entegrasyonu.
- **zeynepkucuk23:** Fotoğraf çekildikten sonra beliren "Yükleniyor / Yapay Zeka Analiz Ediyor" animasyonunun kodlanması.

### 8. Hafta (2. Ay Değerlendirmesi & İlk Prototip)
- **Ahmet:** İlk model eğitim çıktılarının (loss eğrileri, mAP50 değerleri) analiz edilmesi.
- **Yağmur Sayın:** Kullanıcıdan gelen "patates, kıyma, salça" girdisine karşılık en iyi 3 Türk yemeğini öneren prototip scriptin tamamlanması.
- **ayss6502:** Besin değerleri tablosundaki eksik vitamin/mineral verilerinin TÜRKOMP üzerinden tamamlanması.
- **hlnzmn:** Backend'in mobil uygulama için JSON yanıt formatlarının kilitlenmesi.
- **zeynepkucuk23:** Mobil uygulamada HTTP isteklerini yöneten `ApiService` katmanının yazılması.

---

## 3. AY: Çekirdek Yapay Zeka Model Eğitimi & İnce Ayar (Fine-Tuning)

### 9. Hafta (Model Optimizasyonu & Transfer Learning)
- **Ahmet:** YOLOv8-seg modelinin 100 epokluk ana eğitiminin yapılması; tabak ve yemek segmentasyon hassasiyetinin artırılması.
- **Yağmur Sayın:** RAG mimarisinde tarif eşleştirme için eşik değerlerinin (similarity threshold) ayarlanması.
- **ayss6502:** Yanlış sınıflandırılan örnekler için negatif veri seti (yemek dışı nesneler) toplanıp eklenmesi.
- **hlnzmn:** Model inference süresini düşürmek için ONNX dönüşümü veya TorchScript optimizasyonu araştırılması.
- **zeynepkucuk23:** Mobil uygulamada "Önerilen Tarifler" listeleme ve detay ekranının tasarlanması.

### 10. Hafta (Porsiyon Kestirim Algoritması)
- **Ahmet:** 2D görüntüden alan (piksel sayısı) hesabı yaparak tabak referansına göre porsiyon ağırlığı tahmin eden fonksiyonun yazılması.
- **Yağmur Sayın:** Kullanıcı serbest metin girdiğinde ("2 kepçe mercimek, 1 dilim ekmek") besinleri ayıran NLP regex/NER modelinin tamamlanması.
- **ayss6502:** Gerçek yemek tartımları ile porsiyon doğrulama referans test tablosunun oluşturulması.
- **hlnzmn:** Porsiyon tahmin algoritması ile TÜRKOMP veritabanını bağlayan `/api/v1/calculate-nutrition` endpoint'inin yazılması.
- **zeynepkucuk23:** Besin sonuç ekranında dairesel grafik (Makro dağılımı: Karbonhidrat, Protein, Yağ) bileşeninin kodlanması.

### 11. Hafta (RAG & Malzeme Öneri Servisinin Bağlanması)
- **Ahmet:** CV model ağırlıklarının (`best.pt`) dışa aktarılması ve test seti üzerindeki başarı metriklerinin kaydedilmesi.
- **Yağmur Sayın:** Kullanıcının seçtiği malzemelerle sistemdeki tariflerin kesişim skorunu hesaplayan hibrit RAG modülünün koda dökülmesi.
- **ayss6502:** Farklı ışık ve açılardan çekilmiş zorlayıcı test fotoğraflarının (benchmark test seti) derlenmesi.
- **hlnzmn:** `/api/v1/recommend-recipes` endpoint'inin tamamlanması ve RAG pipeline ile birleştirilmesi.
- **zeynepkucuk23:** Tarif detay sayfasında pişirme süresi, zorluk ve malzeme listesi kartlarının kodlanması.

### 12. Hafta (3. Ay Değerlendirmesi & Ortak Model Testi)
- **Ahmet & Yağmur:** CV ve NLP modellerinin ilk entegrasyon toplantısı; çıktı formatlarının eşgüdümü.
- **ayss6502:** Modelin ürettiği kalori değerleri ile diyetisyen kaynaklarının karşılaştırılması.
- **hlnzmn:** Bilgisayarı harici erişime açmak için Cloudflare Tunnel / Ngrok altyapısının kurulması.
- **zeynepkucuk23:** Mobil uygulamanın yerel API yerine tünel adresine bağlanacak şekilde ayarlanması.

---

## 4. AY: Sistem Entegrasyonu (Uçtan Uca Mobil + AI)

### 13. Hafta (Kamera -> Backend -> AI Akışı)
- **Ahmet:** Mobil kameradan gelen dikey fotoğrafların model için otomatik kırpılması ve boyutlandırılması (pre-processing).
- **Yağmur Sayın:** LLM tarif çıktılarının Türkçe gramer ve Türk mutfağı üslubuna göre prompt ayarlamalarının yapılması.
- **ayss6502:** Sulu yemek ve tencere yemeklerinde porsiyon derinlik yanılsamalarını telafi eden katsayı tablosunun hazırlanması.
- **hlnzmn:** Görüntü işleme isteklerinin asenkron kuyruk yönetimi (Celery / Background Tasks) ile optimize edilmesi.
- **zeynepkucuk23:** Kullanıcının çektiği fotoğrafı backend'e gönderip gelen yemek sınıfını ekranda onaylatma akışı.

### 14. Hafta (Manuel Düzeltme & Kullanıcı Kontrolü)
- **Ahmet:** Modelin güven skoru (confidence) %70'in altında kaldığında alternatif 3 yemek sınıfı önerme mantığının eklenmesi.
- **Yağmur Sayın:** "Bir tutam", "avuç içi", "tatlı kaşığı" gibi birimlerin porsiyon katsayılarıyla çarpım testleri.
- **ayss6502:** Yanlış tahmin edilen yemek sınıflarının hata matrisinde (Confusion Matrix) incelenmesi.
- **hlnzmn:** Kullanıcının model tahminini manuel düzeltebilmesi için `/api/v1/feedback` log mekanizmasının kurulması.
- **zeynepkucuk23:** Kullanıcının yanlış tahmin durumunda listeden doğru yemeği seçebileceği açılır menü (dropdown/modal) yapımı.

### 15. Hafta (Günlük Kalori ve Besin Takibi Ekranı)
- **Ahmet:** Porsiyon kestiriminde MAPE (Mean Absolute Percentage Error) metriğinin hesaplanması.
- **Yağmur Sayın:** Evdeki malzemelere ek olarak "alerjen" veya "sevilmeyen malzeme" filtrelerinin RAG motoruna eklenmesi.
- **ayss6502:** Besin etiketleme verilerinin son doğrulaması ve veri tabanı yedeklemesi.
- **hlnzmn:** Günlük toplam kalori ve makro özetini tutan yerel/sunucu veri tabanı sorgularının yazılması.
- **zeynepkucuk23:** Mobil uygulamada "Günlük Tüketim Özeti" ve ilerleme çubuğu (progress bar) ekranının kodlanması.

### 16. Hafta (4. Ay Değerlendirmesi & Alfa Testi)
- **Ahmet, Yağmur, ayss6502, hlnzmn, zeynepkucuk23:** Ekip içi Alfa testi: Herkes kendi evinde 5 farklı öğünü telefonla çekip sistemi test eder.
- Tespit edilen hataların GitHub Issues üzerinde açılması ve kritik olanların önceliklendirilmesi.

---

## 5. AY: Doğrulama, Metrikler (MAPE / F1) ve Performans İyileştirme

### 17. Hafta (Hata Düzeltme & Model İnce Ayarı)
- **Ahmet:** Alfa testinde en çok karıştırılan yemeklerin (ör: Mercimek Çorbası vs Ezogelin) ek görsellerle yeniden eğitilmesi.
- **Yağmur Sayın:** NLP modülünde argo veya günlük dilde yazılan birimlerin ("bi avuç", "yarım kepçecik") temizlenmesi.
- **ayss6502:** TÜBİTAK bilimsel raporu için kullanılacak veri dağılım grafiklerinin ve istatistiklerinin çıkarılması.
- **hlnzmn:** API uç noktalarında yanıt süresinin 1.5 saniyenin altına düşürülmesi için önbellekleme (caching) eklenmesi.
- **zeynepkucuk23:** Uygulama arayüzündeki takılmaların (jank) giderilmesi ve ekran geçiş animasyonlarının optimize edilmesi.

### 18. Hafta (TÜBİTAK Bilimsel Metriklerinin Hesaplanması)
- **Ahmet:** Bilgisayarlı Görü modeli için Precision, Recall, F1-Score ve mAP değerlerinin hesaplanması ve tablo haline getirilmesi.
- **Yağmur Sayın:** RAG tarif önerisi başarısının (malzeme kapsama oranı ve tarif doğruluğu) ölçülmesi.
- **ayss6502:** Gerçek gramajlar ile model tahminleri arasındaki MAPE (Ortalama Mutlak Yüzde Hata) hesaplama çalışması.
- **hlnzmn:** API loglarının analiz edilerek olası sunucu çökmelerine karşı hata yakalama bloklarının (try-catch) sıkılaştırılması.
- **zeynepkucuk23:** İnternet bağlantısı koptuğunda veya sunucuya ulaşılamadığında gösterilecek hata ekranlarının kodlanması.

### 19. Hafta (Kullanılabilirlik ve Saha Testi)
- **Ahmet & Yağmur:** Akademik danışmanla (Doç. Dr. Ferhat Uçar) ara değerlendirme toplantısı; metrik sonuçlarının paylaşılması.
- **ayss6502:** Farklı tabak tipleriyle (çukur tabak, düz tabak, kase) yapılan test sonuçlarının dökümante edilmesi.
- **hlnzmn:** API dokümantasyonunun (Swagger/ReDoc) ve mimari diyagramların nihai haline getirilmesi.
- **zeynepkucuk23:** Kullanıcı arayüzüne "Nasıl Kullanılır?" rehberi ve porsiyon yardım kutucuklarının eklenmesi.

### 20. Hafta (5. Ay Değerlendirmesi & Kod Dondurma - Feature Freeze)
- **Tüm Ekip:** Yeni özellik eklemenin durdurulması; mevcut kodun kararlı (stable) sürüme getirilmesi.
- Kod tabanının temizlenmesi, kullanılmayan paketlerin silinmesi.

---

## 6. AY: TÜBİTAK Sonuç Raporu, Proje Kapanışı ve Sunum

### 21. Hafta (TÜBİTAK Sonuç Raporu: Giriş & Yöntem)
- **Yağmur Sayın (Yürütücü):** Raporun Giriş, Amaç ve Kapsam bölümlerinin yazımının tamamlanması.
- **Ahmet:** "Bilgisayarlı Görü ve Porsiyon Kestirim Yöntemi" bölümünün mimari şemalar ve formüllerle yazılması.
- **ayss6502:** "Kültürel Veri Tabanı ve TÜRKOMP Eşleme Metodolojisi" bölümünün kaleme alınması.
- **hlnzmn:** "Sistem Mimarisi, API Entegrasyonu ve MLOps Altyapısı" teknik metninin hazırlanması.
- **zeynepkucuk23:** Mobil uygulama ekran görüntülerinin yüksek çözünürlüklü olarak rapora eklenmek üzere derlenmesi.

### 22. Hafta (TÜBİTAK Sonuç Raporu: Bulgular & Tartışma)
- **Ahmet & ayss6502:** Elde edilen F1-Score, mAP ve MAPE grafiklerinin rapora yerleştirilmesi ve akademik tartışması.
- **Yağmur Sayın:** RAG motorunun öneri kalitesi ve kültürel ölçü dönüşüm doğruluk analizlerinin rapora eklenmesi.
- **hlnzmn:** Projenin açık kaynak olarak yayınlanması için GitHub reposunun lisanslanması ve `README.md` temizliği.
- **zeynepkucuk23:** Mobil uygulamanın Android APK çıktısının alınması ve sürüm etiketinin (`v1.0.0-tubitak`) basılması.

### 23. Hafta (Demo Videosu & Sunum Hazırlığı)
- **Ahmet & Yağmur:** 3-5 dakikalık projenin baştan sona nasıl çalıştığını gösteren etkileyici bir tanıtım/demo videosunun çekilmesi ve kurgulanması.
- **ayss6502 & hlnzmn:** Proje sunum slaytlarının (Canva/PowerPoint) akademik formatta hazırlanması.
- **zeynepkucuk23:** Demo esnasında kullanılacak örnek yemek senaryolarının (ör: Karnıyarık, Yayla Çorbası, Menemen) hazırlanması.

### 24. Hafta (Nihai Teslimat & Proje Kapanışı)
- **Yağmur Sayın:** TÜBİTAK Proje Sonuç Raporu'nun akademik danışman onayına sunulması ve TÜBİTAK BİDEB sistemine yüklenmesi.
- **Ahmet:** Model ağırlıklarının ve kodların GitHub Releases üzerinde güvenli şekilde arşivlenmesi.
- **Tüm Ekip:** Proje başarı kutlaması, deneyimlerin değerlendirilmesi ve gelecekteki olası yayın/makale fırsatlarının konuşulması.
