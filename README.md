# Real Time Weather Data Pipeline
<img src="images/introduction.jpg" alt="introduction" width="700"/>

---
<img src="images/atom-logo.jpg" alt="Atom Logo" width="110"/> <img src="images/bigquery-logo.png" alt="BigQuery Logo" width="110"/> <img src="images/dotenv-logo.png" alt="dotenv Logo" width="110"/> <img src="images/pandas-logo.jpg" alt="Pandas Logo" width="110"/> <img src="images/openweather-logo.png" alt="OpenWeather Logo" width="110"/>  <img src="images/window-task-scheduler-logo.png" alt="Window Task Scheduler Logo" width="110"/>

This project is a **real-time weather data pipeline** designed to collect, store, and automate the extraction of weather information using the OpenWeather API, Google BigQuery and Python.  
It is fully automated with Windows Task Scheduler and made with principies of pipeline-code standards.

## Project Context and Problem
The goal of this project was to **simulate a real-world ETL pipeline**, by extracting data from an external API, transforming it, and loading it into a cloud data warehouse using only free tools.

I wanted to explore how to:
- Design a simple but scalable pipeline with cloud tools, in this case I used Atom.
- Solve the challenge of working under Google BigQuery Free Tier restrictions, for example cannot insert streaming.
- Automate the process without paid platforms.

The reason I chose this project because **real-time weather data is one of the best examples of constantly changing information that needs to be captured regularly**

## Why These Technologies?

| Technology | Reason |
|------------|--------|
| Python     | Perfect for API requests, data processing, and cloud interactions. |
| Atom     | A perfect text editos and comfortable for making and running python scripts |
| Google BigQuery | Cloud data warehouse with free-tier access and a lot of functionalities. |
| OpenWeather API | For real-time weather data via a simple REST API. |
| pandas     | Easy to structure and export the data for batch loading to BigQuery. |
| Windows Task Scheduler | A free and effective way to automate scripts on a local machine (in this case). |
| dotenv     | It makes that sensitive credentials are not exposed in the code. |

## Key Features

- Real-time API extraction.
- Batch loading to BigQuery (compatible with Free Tier).
- Secure credential management with `.env` files.
- Full automation with Windows Task Scheduler.
- Professional project/documentation structure, GitHub-ready.

## Challenges and Solutions

### Challenge 1: BigQuery Free Tier Limitations
The free tier does not allow **streaming inserts.**
**Solution:** In this case I switched to batch loads via CSV files. Automated and continued successfully the process.

### Challenge 2: Credential Security
Exposing API keys, service account keys or computer information in public repositories is a common security risk.
**Solution:** Implemented `python-dotenv` to read environment variables securely from a local `.env` file.

### Challenge 3: Automation Without Scheduler
The project needed to run automatically at regular intervals (mostly daily) without using cloud paid tools.
**Solution:** Configured Windows Task Scheduler (only in this case) to execute the Python script every day at the morning.

## Potential Improvements

- Expand the pipeline to collect weather data from different cities at the same time at different times (next project).
- Build a Looker/Power BI dashboard connected to this data source for real-time visualization.
- Move the pipeline to the cloud using Cloud Functions or Cloud Composer for scalable automation (next project).
- Integrate alerts when certain weather conditions are detected or when data is not collected well (next project).








