from litestar import get
from litestar.response import Response
from litestar.status_codes import HTTP_200_OK


@get("/ready", sync_to_thread=False)
def ready() -> Response[dict[str, str]]:
    return Response({"status": "ready"}, status_code=HTTP_200_OK)
