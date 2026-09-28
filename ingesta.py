import boto3
import pymysql
import pandas as pd
 
ficheroUpload = "data.csv"
nombreBucket = "dvvs-output-01"
 
conexion = pymysql.connect(host="localhost", port=8005, user="root", password="utec", database="bd_api_employees")
pd.read_sql("SELECT * FROM employees", conexion).to_csv(ficheroUpload, index=False)
conexion.close()
 
s3 = boto3.client('s3')
s3.upload_file(ficheroUpload, nombreBucket, ficheroUpload)
 
print("Ingesta completada")
