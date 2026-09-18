# NOAA Weather Analytics

An analytics engineering project that transforms raw NOAA Global Historical
Climatology Network (GHCNd) weather data into clean, tested, well-documented
data models using dbt.

## The question

Which Adirondack valleys trap cold air, how often, and in which months?

On calm, clear nights, air near the ground cools and drains downhill, pooling in
valley bottoms. When enough cold air collects, the valley floor ends up colder
than the mountain above it — a temperature inversion, the reverse of the normal
pattern where air gets colder with altitude. Inversions are what produce the fog
that fills Adirondack valleys at dawn while summits stay clear above it.

Measuring one requires temperature readings from two places at once: somewhere
high and somewhere low, close enough together to share the same weather. That
pairing is rare in mountain terrain, because weather stations are built where
people live and where planes land — in valleys.

## Why these stations

Whiteface Mountain is the anchor. At 1,483m it is the only high-elevation
weather station in the Adirondacks, sitting roughly 900m above the valley floors
around it. Without Whiteface there is no summit reading to compare against, and
no way to detect an inversion at all.

The other five stations span the terrain below it, from Plattsburgh at 50m on the
Lake Champlain plain to Lake Placid, Saranac Lake, Tupper Lake and Newcomb between
480m and 580m in the valleys of the High Peaks. Together they cover about 1,400m
of vertical range within a 40km radius — close enough that all six stations
experience the same passing weather systems, so differences between them reflect
local terrain rather than different storms.

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
