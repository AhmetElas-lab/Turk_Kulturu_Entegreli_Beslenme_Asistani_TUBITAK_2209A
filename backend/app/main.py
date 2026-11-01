from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Türk Kültürü Entegreli Beslenme Asistanı API",
    description="TÜBİTAK 2209-A projesi kapsamında Türk mutfağına özel besin, porsiyon ve tarif öneri servisi.",
    version="0.1.0"
)

# Mobil uygulamanın ve yerel istemcilerin rahat bağlanabilmesi için CORS ayarı
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {
        "status": "online",
        "project": "Türk Kültürü Entegreli Beslenme Asistanı",
        "version": "0.1.0"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}
