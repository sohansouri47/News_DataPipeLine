import json
import pandas as pd
import boto3
from io import StringIO
from datetime import datetime
def create_dataframe(data):
    
    articles=data['articles']
    df=pd.DataFrame(articles)
    df[['source_id', 'source_name']] = df['source'].apply(pd.Series)
    df['publishedAt'] = pd.to_datetime(df['publishedAt'], format='%Y-%m-%dT%H:%M:%SZ')
    df=df.drop(labels='source',axis=1)
    return df


def lambda_handler(event, context):
    
    s3=boto3.client('s3')
    Bucket="news-pipeline-plumber47"
    Key="raw_data/to_processed/"
    print(".")
    key_list=[]
    for file in s3.list_objects(Bucket=Bucket,Prefix=Key)['Contents']:
        file_key=file['Key']
        #print(file_key)
        if file_key.split('.')[-1]=='json':
            temp=file_key.split('/')[-1].strip()
            fir=temp.split("_")[0].strip()
            key_list.append(file_key)
            response=s3.get_object(Bucket=Bucket,Key=file_key)
            content=response['Body']
            jsonObject=json.loads(content.read())
            file_df=create_dataframe(jsonObject)
            transformed_key="transformed_data/"+fir+"/"+fir+"_news_transformed_"+str(datetime.now())+".csv"
            file_buffer=StringIO()
            file_df.to_csv(file_buffer)
            file_content=file_buffer.getvalue()
            s3.put_object(Bucket=Bucket,Key=transformed_key,Body=file_content)

    s3_resource=boto3.resource("s3")
    for key in key_list:
        copy_source={
            'Bucket':Bucket,
            'Key':key
        }
        s3_resource.meta.client.copy(copy_source,Bucket,'raw_data/processed/'+key.split('/')[-1])
        s3_resource.Object(Bucket,key).delete()
    
