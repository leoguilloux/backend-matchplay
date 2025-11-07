from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "MatchPlay backend activo"}

@app.post("/cron")
def run_cron(token: str):
    # simulación del proceso de actualización diario
    return {"ok": True, "message": "cron ejecutado correctamente"}
