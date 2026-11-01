# Türk Kültürü Entegreli Beslenme Asistanı Yapay Zekâ Modülü

TÜBİTAK 2209-A Üniversite Öğrencileri Araştırma Projeleri Destekleme Programı kapsamında yürütülen bu proje; Türk mutfağına özgü yemekleri, geleneksel ölçü birimlerini ("bir çimdik", "avuç içi", "kepçe", "göz kararı") ve tencere yemeklerinin porsiyon analizini yapay zekâ desteğiyle gerçekleştiren kapsamlı bir mobil asistan sistemidir.

## Proje Mimarisi

- **`backend/`**: FastAPI tabanlı REST API servisi (Yemek sınıflandırma, porsiyon tahmini, LLM & RAG destekli tarif öneri motoru).
- **`mobile/`**: Flutter tabanlı kullanıcı arayüzü (Kamera çekimi, malzeme girişi, kalori takibi).
- **`data/`**: 
  - `raw/`: TÜRKOMP ve açık kaynak yemek veritabanları.
  - `processed/`: Temizlenmiş ve etiketlenmiş besin & porsiyon tabloları.
- **`notebooks/`**: Model eğitimi, veri ön işleme ve deney defterleri (PyTorch/TensorFlow).
- **`docs/`**: Proje mimarisi, araştırma notları ve TÜBİTAK raporları.

## Başlangıç (Backend)

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```
API arayüzü için: `http://localhost:8000/docs` adresini ziyaret edin.
