FROM python:3.11-slim
WORKDIR /bot1
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY task-3.py .
CMD ["python", "task-3.py"]