## Project Overview
This project demonstrates the implementation of an end-to-end data pipeline for extracting, transforming, and analyzing data from the **News API**. The pipeline is built using AWS services, enabling automated data collection, transformation, and storage for analytics purposes. The data is categorized into three sections: **Health**, **Sports**, and **Business**.

## Objective
The primary goal of this project is to:
- Automate data extraction from the News API using AWS Lambda.
- Store raw data in AWS S3 for processing and archiving.
- Perform data transformation to clean and format the data using another AWS Lambda function.
- Automate the data transformation trigger upon the arrival of raw data in S3.
- Enable analytics by creating tables in AWS Glue and querying with Amazon Athena.

## Features
1. **Automated Data Extraction**:
   - Data is fetched from the News API once a day using AWS Lambda.
   - Three categories of news articles are extracted: **Health**, **Sports**, and **Business**.

2. **Raw Data Storage**:
   - Extracted data is stored in raw JSON format in an organized structure within an S3 bucket.

3. **Data Transformation**:
   - A secondary AWS Lambda function is triggered when raw data is uploaded to S3.
   - The transformation function cleans, normalizes, and converts the data into CSV format.
   - Transformed data is saved back into another location in the same S3 bucket.

4. **Analytics Integration**:
   - AWS Glue crawlers catalog the transformed data.
   - Amazon Athena is used to create analytics tables for querying and analyzing the data efficiently.

---

## Architecture
### Services Used:
- **News API**: A RESTful API that provides access to the latest news articles from multiple sources and categories.
- **AWS Lambda**: Handles automated data extraction and transformation functions.
- **AWS S3**: Stores raw and transformed data in an organized structure.
- **AWS Glue**: Automates the creation of data schemas and catalogs.
- **Amazon Athena**: Enables querying and analyzing transformed data directly from S3.

![Untitled design](https://github.com/user-attachments/assets/07d55d0d-5197-4089-9d09-1440a9e2bf97)

---

## How It Works
1. **News API Integration**:
   The [News API](https://newsapi.org/) is a powerful tool that provides real-time access to news articles from thousands of sources. In this project:
   - Articles are fetched using the `get_top_headlines` method, specifying the desired categories.
   - Example API calls:
     ```python
     from newsapi import NewsApiClient

     newsapi = NewsApiClient(api_key='my_api_key')
     call1 = newsapi.get_top_headlines(category="health")
     call2 = newsapi.get_top_headlines(category="sports")
     call3 = newsapi.get_top_headlines(category="business")
     ```

2. **AWS Lambda for Data Extraction**:
   - A Lambda function runs once daily (using a CloudWatch schedule) to fetch data from the News API.
   - Data is stored as raw JSON files in an S3 bucket with the following structure:
     ```
     s3://news-pipeline-plumber47/raw_data/health/
     s3://news-pipeline-plumber47/raw_data/sports/
     s3://news-pipeline-plumber47/raw_data/business/
     ```

3. **AWS Lambda for Data Transformation**:
   - A second Lambda function is triggered whenever new raw data is uploaded to S3.
   - This function:
     - Cleans the data (e.g., removing unnecessary fields, handling missing values).
     - Converts the JSON data into CSV format.
     - Saves the transformed data back into S3 in the following structure:
       ```
       s3://news-pipeline-plumber47/transformed_data/health/
       s3://news-pipeline-plumber47/transformed_data/sports/
       s3://news-pipeline-plumber47/transformed_data/business/
       ```

4. **Glue and Athena for Analytics**:
   - AWS Glue crawlers detect the transformed data and create schemas in the Glue Data Catalog.
   - Amazon Athena enables querying the data for insights.

---

## Future Enhancements
- Add support for more categories.
- Implement sentiment analysis on the news articles.
- Build dashboards using Amazon QuickSight or Tableau for visualizing analytics.
