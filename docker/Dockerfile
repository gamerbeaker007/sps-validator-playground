# Use Python slim image (smaller than the default)
FROM python:3.9-slim

# Set a working directory
WORKDIR /app

# Copy your index.html into /app
COPY index.html /app/index.html

# Expose the desired port (3000)
EXPOSE 3000

# Run Python's built-in HTTP server
CMD ["python", "-m", "http.server", "3000"]
