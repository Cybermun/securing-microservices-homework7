FROM python:3.11-slim as base

# Install requirements
WORKDIR /app
COPY secure_app /app
RUN pip install flask

# Add a non-root user
RUN adduser --disabled-password --gecos "" appuser
USER appuser

# Healthcheck
HEALTHCHECK CMD curl --fail http://localhost:5000/ || exit 1

CMD ["python", "app.py"]
