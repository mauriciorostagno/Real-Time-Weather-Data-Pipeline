# Real Time Weather Data Pipeline


---
This project is a **real-time weather data pipeline** designed to collect, store, and automate the extraction of weather information using the OpenWeather API, Google BigQuery and Python.  
It is fully automated with Windows Task Scheduler and made with principies of pipeline-code standards.

## Project Context and Problem
The goal of this project was to **simulate a real-world ETL pipeline**, by extracting data from an external API, transforming it, and loading it into a cloud data warehouse using only free tools.

I wanted to explore how to:
- Design a simple but scalable pipeline with cloud tools.
- Solve the challenge of working under Google BigQuery Free Tier restrictions, for example cannot insert streaming.
- Automate the process without paid platforms.

The reason I chose this project because **real-time weather data is one of the best examples of constantly changing information that needs to be captured regularly**

## Why These Technologies?

| Technology | Reason |
|------------|--------|
| Python     | Perfect for API requests, data processing, and cloud interactions. |
| Google BigQuery | Cloud data warehouse with free-tier access and a lot of functionalities. |
| OpenWeather API | For real-time weather data via a simple REST API. |
| pandas     | Makes it easy to structure and export the data for batch loading. |
| Windows Task Scheduler | A free and effective way to automate scripts on a local machine. |
| dotenv     | Ensures that sensitive credentials are not exposed in the code. |
