# Multi-stage build for minimal production image
FROM python:3.14.0-alpine3.21 AS builder

# Create virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Production stage
FROM python:3.14.0-alpine3.21

# Copy virtual environment from builder stage
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Set working directory
WORKDIR /app

# Create dedicated user && set ownership
RUN adduser -D app && chown -R app:app /app

# Switch to app user
USER app

# Set environment variables
ENV FLASK_APP=counter-service.py
ENV PYTHONPATH=/app

# Copy application files
COPY counter-service.py .

# Run with gunicorn
ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:8000", "counter-service:app"]