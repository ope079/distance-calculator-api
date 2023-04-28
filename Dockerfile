FROM python:3.9
COPY . .
RUN pip install --upgrade -r requirements.txt
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]