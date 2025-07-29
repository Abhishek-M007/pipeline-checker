# Use a lightweight base image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy everything into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run your pipeline script
CMD ["python", "src/pipeline.py"]