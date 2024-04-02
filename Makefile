include .env

.PHONY: setup start trigger-pipeline all

# Main target to run all tasks
all: setup start trigger-pipeline

# Target to pull docker image
setup:
	@echo "Pulling Docker image..."
	@(cd $(WORKING_DIR) && \
	docker pull $(DOCKER_IMAGE))

# Target to start the container
start: setup
	@echo "Starting container..."
	@(cd $(WORKING_DIR) && \
	docker run -d --name $(CONTAINER_NAME) -p $(HOST_PORT):$(CONTAINER_PORT) -v "$(WORKING_DIR)":/home/src --user $(DOCKER_USER) $(DOCKER_IMAGE) /app/run_app.sh mage start $(PROJECT_NAME) && \
	sleep 45) # Give some initial time for the server to start up before checking

# Target to trigger pipeline(2 minutes break between pipelines run)
trigger-pipeline: start
	@echo "Triggering pipeline..."
	@(cd $(WORKING_DIR) && \
	curl --fail -X POST http://localhost:$(HOST_PORT)/api/pipeline_schedules/1/pipeline_runs/d632dff404a1407b99fa00bf011e0f52 -v && \
	sleep 120 && \
	curl --fail -X POST http://localhost:$(HOST_PORT)/api/pipeline_schedules/2/pipeline_runs/0c5dfbe5fa6d47c6bc0050c188e585cb -v) || echo "Failed to trigger pipeline. Is the service up?"
