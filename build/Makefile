COMPOSE_FILE := docker-compose.yml

run:
	docker compose -f $(COMPOSE_FILE) up --build -d chatmate-vote-talk

test:
	docker compose -f $(COMPOSE_FILE) build chatmate-autolike
	docker compose -f $(COMPOSE_FILE) run --rm chatmate-tests
