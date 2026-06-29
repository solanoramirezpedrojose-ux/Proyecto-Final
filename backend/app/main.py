from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config.data_base import init_db
from app.controller.usuario_controller import router as usuario_router
from app.controller.login_controller import router as login_router
from app.controller.aviso_controller import router as aviso_router
from app.controller.seguimiento_controller import router as seguimiento_router
from app.controller.reporte_controller import router as reporte_router


app = FastAPI(
    title="Sistema de Gestion de Avisos Ciudadanos",
    description="API REST para administrar usuarios, avisos ciudadanos, seguimientos y reportes.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

init_db()
app.include_router(usuario_router)
app.include_router(login_router)
app.include_router(aviso_router)
app.include_router(seguimiento_router)
app.include_router(reporte_router)

@app.get("/api/status")
def status():
    return {
        "message": "API de Avisos Ciudadanos funcionando correctamente"
    }