IMAGE ?= ghcr.io/johnidm/rinha-backend-2026:latest

deps:
	uv sync

run:
	uv run uvicorn src.main:app --reload --port 9999

up:
	docker compose up --build

down:
	docker compose down

push:
	docker buildx build \
	  -t $(IMAGE) \
	  --push \
	  .

publish: push
