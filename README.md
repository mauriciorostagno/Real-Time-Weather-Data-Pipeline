# Real Time Weather Data Pipeline
![](images/introduction.jpg)

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
✅ **Solution:** Switched to batch loads via CSV files and successfully automated the process.

### Challenge 2: Credential Security
Exposing API keys or service account keys in public repositories is a common security risk.
✅ **Solution:** Implemented `python-dotenv` to read environment variables securely from a local `.env` file.

### Challenge 3: Automation Without Cloud Scheduler
The project needed to run automatically at regular intervals without using cloud paid tools.
✅ **Solution:** Configured Windows Task Scheduler to execute the Python script every few minutes.








