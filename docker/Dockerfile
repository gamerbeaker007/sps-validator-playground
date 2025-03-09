# First stage: Use Python to update OpenAPI
FROM python:3.9-slim AS builder

WORKDIR /app

# Install dependencies
RUN pip install requests pyyaml

# Copy scripts and custom endpoints
COPY update_openapi.py custom_endpoints.yml ./

# Run the script to update OpenAPI dynamically
RUN python update_openapi.py

# Second stage: Use Swagger UI to serve the updated OpenAPI spec
FROM swaggerapi/swagger-ui:latest

# Copy the updated OpenAPI spec
COPY --from=builder /app/openapi.yaml /openapi.yaml

# Set Swagger UI environment variable
ENV SWAGGER_JSON=/openapi.yaml
