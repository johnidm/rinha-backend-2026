from litestar import Litestar
from litestar.openapi import OpenAPIConfig
from litestar.openapi.spec import Contact

from src.routes.fraud_score import fraud_score
from src.routes.index import index
from src.routes.ready import ready

route_handlers = [
    ready,
    fraud_score,
    index,
]

openapi_config = OpenAPIConfig(
    title="Rinha de Backend 2026",
    version="0.1.0",
    description="API de detecção de fraude em transações de cartão.",
    contact=Contact(
        name="Johni Douglas Marangon",
        url="https://github.com/johnidm",
        email="johni.douglas.marangon@gmail.com",
    ),
)

app = Litestar(
    route_handlers=route_handlers,
    openapi_config=openapi_config,
    debug=True,
)
