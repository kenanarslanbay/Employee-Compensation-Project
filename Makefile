.PHONY: setup start trigger-pipeline all 

# Define your project name here
PROJECT_NAME := mage
DOCKER_IMAGE := mageai/mageai
CONTAINER_NAME := $(PROJECT_NAME)_cont
HOST_PORT := 6789
CONTAINER_PORT := 6789
# Define the directory you want to work from
WORKING_DIR := $(shell pwd)/02-Orchestration
DOCKER_USER := $(shell id -u):$(shell id -g)

all: setup start trigger-pipeline

setup:
	@(cd $(WORKING_DIR) && \
	docker pull $(DOCKER_IMAGE))

start:
	@(cd $(WORKING_DIR) && \
	docker run -d --name $(CONTAINER_NAME) -p $(HOST_PORT):$(CONTAINER_PORT) -v "$(WORKING_DIR)":/home/src --user $(DOCKER_USER) $(DOCKER_IMAGE) /app/run_app.sh mage start $(PROJECT_NAME) && \
	sleep 20) # Give some initial time for the server to start up before checking

trigger-pipeline:
	@(cd $(WORKING_DIR) && \
	curl --fail -X POST http://localhost:6789/api/pipeline_schedules/1/pipeline_runs/d632dff404a1407b99fa00bf011e0f52 -v || echo "Failed to trigger pipeline. Is the service up?"; \ 
	sleep 90; \
	curl --fail -X POST http://localhost:6789/api/pipeline_schedules/2/pipeline_runs/0c5dfbe5fa6d47c6bc0050c188e585cb -v || echo "Failed to trigger the second request. Is the service up?")
