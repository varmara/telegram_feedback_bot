## Compile stage
FROM python:3.10-slim-bullseye AS compile-image
ENV PYTHONDONTWEITERBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache -r requirements.txt && \
    pip wheel --no-cache-dir --no-deps --wheel-dir /opt/pip_wheels -r /app/requirements.txt

# Run stage
FROM python:3.10-slim-bullseye AS run-image
WORKDIR /app
COPY --from=compile-image /opt/pip_wheels /opt/pip_wheels
RUN pip install --no-cache /opt/pip_wheels/* && rm -rf /opt/pip_wheels
# Copy code
COPY bot /app/bot
# Run bot
CMD ["python", "-m", "bot"]