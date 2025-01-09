import boto3
import os

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
S3_BUCKET = os.getenv("S3_BUCKET")

s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
)

def upload_to_s3(file_path, file_name):
    s3.upload_file(file_path, S3_BUCKET, file_name)
    return f"https://{S3_BUCKET}.s3.amazonaws.com/{file_name}"
