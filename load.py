import json
import os
import pandas
import newsapi
from newsapi import NewsApiClient
import boto3
from datetime import datetime

def lambda_handler(event, context):
    #sec=os.environ.get(api_secret)
    newsapi = NewsApiClient(api_key='daeec14fc19b41ca88f85ac6dd69cfb1')
    cat_list=["health","sports","business"]
    for i in cat_list:
        call=newsapi.get_top_headlines(category=i)
        fname1=i+"_news_raw_"+str(datetime.now())+'.json'
        client=boto3.client('s3')
        client.put_object(
            Bucket="news-pipeline-plumber47",
            Key="raw_data/to_processed/"+fname1,
            Body=json.dumps(call)
            )
