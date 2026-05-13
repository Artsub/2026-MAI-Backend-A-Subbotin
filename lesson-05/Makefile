.PHONY: help up down migrate

help:
	@echo "🎯 Доступные команды:"
	@echo "  make up              - Запустить проект (сборка + запуск)"
	@echo "  make down            - Остановить проект"
	@echo "  make migrate         - Применить миграции"

up:
	docker compose up -d --build

down:
	docker compose down

migrate:
	docker compose exec web python manage.py migrate

