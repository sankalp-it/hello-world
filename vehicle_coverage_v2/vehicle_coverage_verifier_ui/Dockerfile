# Use official Python base image
FROM python:3.10-slim

# Set environment variables for default values
ENV BASE_URL=http://localhost:8000
ENV ENDPOINT_PATH=/api/coverage

# Set working directory
WORKDIR /app

# Copy app files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir streamlit requests

# Expose Streamlit default port
EXPOSE 8501

# Run Streamlit app with env vars passed to it
CMD streamlit run app.py --server.port=8501
