FROM python:3-slim
WORKDIR /app
RUN pip install boto3 pymysql pandas
COPY ingesta.py .
CMD ["python3", "ingesta.py"]
