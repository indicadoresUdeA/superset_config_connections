PUBLIC_ROLE_LIKE = "Gamma" 

CELERY_CONFIG = CeleryConfig

FEATURE_FLAGS = {
    "EMBEDDED_SUPERSET": True,   # muestra la opción “Embed dashboard”
    "DASHBOARD_RBAC": True       # podrás asignar roles por dashboard
}

# Dominios desde los que se permitirá el iframe
TALISMAN_ENABLED = True
TALISMAN_CONFIG = {
    "content_security_policy": {
        "frame-ancestors": ["https://plataforma-indicadores.flutterflow.app"], #Pagina en la que se permitira los embebidos
    },
}

# Clave que firmará los guest tokens
GUEST_TOKEN_JWT_SECRET = "pon_aqui_una_clave_muy_larga_y_unica"

ENABLE_PROXY_FIX = True
PROXY_FIX_CONFIG = {"x_proto": 1, "x_host": 1}
SUPERSET_WEBSERVER_DOMAINS = ["dashboards.parque-e.co"]