FROM python:3.11-slim

WORKDIR /app

# Install project requirements
RUN pip install poetry==1.8.3
COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.in-project true
RUN poetry install --only main --no-root

# Copy the application code to the working directory
COPY . .

# Expose the port on which the application will run
EXPOSE 8080

# Run the FastAPI application using uvicorn server
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]

# ToDo: Add test stage
