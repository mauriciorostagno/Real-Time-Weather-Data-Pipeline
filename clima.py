import os
from dotenv import load_dotenv
import requests
import uuid
from datetime import datetime
from google.cloud import bigquery
import pandas as pd

# Load environment variables from .env file
load_dotenv()

# Read sensitive data from .env
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
api_key = os.getenv('API_KEY')
project_id = os.getenv('PROJECT_ID')
dataset_id = os.getenv('DATASET_ID')

# Build BigQuery table path
table_id = f'{project_id}.{dataset_id}.weather_data'

# API setup
city = 'San Salvador de Jujuy,AR'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

# API request
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    # Generate unique ID
    record_id = str(uuid.uuid4())

    # Get current timestamp
    now = datetime.now()
    date_query = now.strftime('%Y-%m-%d %H:%M:%S')

    # Extract weather data
    city_name = data['name']
    temperature = data['main']['temp']
    humidity = float(data['main']['humidity'])  # Ensure is float, because of problems in bigquery then.
    weather = data['weather'][0]['description']
    temp_min = data['main']['temp_min']
    temp_max = data['main']['temp_max']
    wind_chill = data['main']['feels_like']
    wind = data['wind']['speed']

    # Show data in console
    print(f"date and time: {date_query}")
    print(f"city: {city_name}")
    print(f"temperature: {temperature} °C")
    print(f"wind chill: {wind_chill} °C")
    print(f"temp min: {temp_min} °C")
    print(f"temp max: {temp_max} °C")
    print(f"humidity: {humidity}%")
    print(f"weather: {weather}")
    print(f"wind: {wind} m/s")

    # Save to temporary CSV
    df = pd.DataFrame([{
        'id': record_id,
        'date_query': date_query,
        'city': city_name,
        'temperature': temperature,
        'wind_chill': wind_chill,
        'temp_min': temp_min,
        'temp_max': temp_max,
        'humidity': humidity,
        'weather': weather,
        'wind': wind
    }])

    csv_file = 'weather_temp.csv'
    df.to_csv(csv_file, index=False)

    # Load CSV to BigQuery
    client = bigquery.Client()
    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,
        write_disposition=bigquery.WriteDisposition.WRITE_APPEND
    )

    with open(csv_file, "rb") as source_file:
        load_job = client.load_table_from_file(source_file, table_id, job_config=job_config)

    load_job.result()  # wait here

    print("✅ New row inserted successfully into BigQuery via batch load!")

else:
    print(f'Error in the API request: {response.status_code}')
