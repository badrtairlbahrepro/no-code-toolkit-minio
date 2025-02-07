import os
import boto3
import logging
from urllib.parse import urlparse

logger = logging.getLogger(__name__)

def upload_to_s3(file_path, endpoint_url, access_key, secret_key):
    bucket_name = os.getenv('S3_BUCKET_NAME', 'bucket-no-code-tools')
    
    session = boto3.Session(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name='us-east-1'  # MinIO ignore la région
    )
    
    client = session.client('s3', 
                          endpoint_url=endpoint_url,
                          config=boto3.Config(s3={'addressing_style': 'path'}))

    try:
        # Upload the file to the specified S3 bucket
        with open(file_path, 'rb') as data:
            client.upload_fileobj(data, bucket_name, os.path.basename(file_path), ExtraArgs={'ACL': 'public-read'})

        file_url = f"{endpoint_url}/{bucket_name}/{os.path.basename(file_path)}"
        return file_url
    except Exception as e:
        logger.error(f"Error uploading file to S3: {e}")
        raise
