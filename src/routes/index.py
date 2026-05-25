from litestar import get
from litestar.response import Response
from litestar.status_codes import HTTP_200_OK


@get("/", sync_to_thread=False)
def index() -> Response[str]:
    return Response("ok", status_code=HTTP_200_OK, media_type="text/plain")
