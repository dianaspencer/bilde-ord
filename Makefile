
build:
	docker build . --file Dockerfile --tag bildeord:latest

start:
	docker-compose --file docker-compose.yml up -d
