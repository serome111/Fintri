from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import transaction, auth, word_predic
# from app.routers.word_predic import router as palabras_router
from app.db.database import engine, Base, get_db, init_db
from apscheduler.schedulers.background import BackgroundScheduler
from app.crud.transaction import update_fixed_transactions
import logging

app = FastAPI()

# Enable CORS
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://finanzas.test"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(transaction.router)
app.include_router(auth.router)
app.include_router(word_predic.router, prefix="/v1", tags=["palabras"])
scheduler = BackgroundScheduler()

@app.on_event("startup")
def on_startup():
    init_db()
    scheduler.add_job(lambda: update_fixed_transactions(next(get_db())), 'cron', day=1, hour=0, minute=0)
    scheduler.start()

@app.on_event("shutdown")
def on_shutdown():
    scheduler.shutdown()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Fintiri api in this moment Running ok"}
