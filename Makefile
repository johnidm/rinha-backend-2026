deps:
	uv sync

run:
	uv run uvicorn src.main:app --reload --port 9999

up:
	docker compose up --build

down:
	docker compose down
