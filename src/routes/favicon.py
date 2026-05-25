from litestar import get
from litestar.response import Response
from litestar.status_codes import HTTP_204_NO_CONTENT


@get("/favicon.ico", sync_to_thread=False)
def favicon() -> Response[str]:
    return Response("", status_code=HTTP_204_NO_CONTENT)
