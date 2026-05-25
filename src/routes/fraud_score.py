from litestar import post
from litestar.datastructures import State

from src.schemas.fraud import FraudScoreRequest, FraudScoreResponse


@post("/fraud-score", sync_to_thread=False)
def fraud_score(data: FraudScoreRequest, state: State) -> FraudScoreResponse:
    return FraudScoreResponse(approved=True, fraud_score=0.0)
