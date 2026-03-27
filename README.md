# NOAA Weather Analytics

An analytics engineering project that transforms raw NOAA Global Historical 
Climatology Network (GHCND) weather data into clean, tested, well-documented 
data models using dbt and BigQuery to analyze historical temperature inversion patterns in mountain valleys and predict viewing opportunities atop mountain summits for backcountry recreation and photography.

## Project Goals

- Build an end-to-end data pipeline from raw NOAA data to analysis-ready tables
- Demonstrate dbt best practices: staging/intermediate/mart layers, testing, 
  documentation
- Handle real-world data quality issues (missing values, station gaps, 
  quality flags)
- Separate data completeness from data accuracy in quality assessment

## Tech Stack

- **Warehouse:** Google BigQuery (free tier)
- **Transformation:** dbt Core
- **Ingestion:** Python (NOAA CDO API)
- **Version Control:** Git/GitHub

## Project Status

🚧 In progress — currently setting up infrastructure and raw data loading.

## Architecture

(Architecture diagram coming soon)