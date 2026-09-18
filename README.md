# NOAA Weather Analytics

An analytics engineering project that transforms raw NOAA Global Historical
Climatology Network (GHCNd) weather data into clean, tested, well-documented
data models using dbt.

## The question

Which Adirondack valleys trap cold air, how often, and in which months? On calm
clear nights cold air drains downhill and pools in valley bottoms, sometimes
leaving the valley floor colder than the summit above it. This project measures
how often that happened across an elevation transect in the Adirondack High Peaks.

## Scope

**Stations (6):** Whiteface Mountain (1,483m) as the summit anchor, with
Plattsburgh AFB, Saranac Lake, Tupper Lake, Lake Placid and Newcomb as valley
and mid-elevation comparisons — roughly 1,400m of vertical range within 40km.

**Date range:** 1937–1946. This is the only decade in which the Whiteface summit
station and the surrounding valley stations reported simultaneously. The summit
record ends in 1946; most valley stations continue for decades afterward.

## Project goals

- Build an end-to-end data pipeline from raw NOAA data to analysis-ready tables
- Demonstrate dbt best practices: staging/intermediate/mart layers, testing, documentation
- Handle real-world data quality issues (missing values, station gaps, quality flags)
- Separate data completeness from data accuracy in quality assessment

## Tech stack

- **Warehouse:** Snowflake
- **Local development:** DuckDB via dbt-duckdb
- **Transformation:** dbt Core
- **Ingestion:** Python, reading raw GHCNd station files from NOAA NCEI
- **Version control:** Git / GitHub

## Project status

In progress — scoping complete, raw data loading next.
See [docs/models.md](docs/models.md) for the planned model list.
