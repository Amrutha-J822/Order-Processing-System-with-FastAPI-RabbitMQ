# Step 1: Use an official Python runtime as a parent image
FROM python:3.10

# Step 2: Set the working directory in the container
WORKDIR /app

# Step 3: Copy the current directory contents into the container at /app
COPY . /app

# Step 4: Install the necessary dependencies
RUN pip install --no-cache-dir fastapi uvicorn pika pydantic

# Step 5: Command to run the FastAPI app using uvicorn when the container starts
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
