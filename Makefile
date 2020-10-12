# Create the image
build:
	docker build . --file Dockerfile --tag bildeord:latest

# Launch the container to run the service
start:
	docker-compose --file docker-compose.yml up -d
