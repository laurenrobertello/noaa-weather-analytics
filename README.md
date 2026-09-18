# NOAA Weather Analytics

An analytics engineering project that transforms raw NOAA Global Historical
Climatology Network (GHCNd) weather data into clean, tested, well-documented
data models using dbt.

## The question

Which Adirondack valleys trap cold air, how often, and in which months?

On calm, clear nights, air near the ground cools and drains downhill, pooling in
valley bottoms. When enough cold air collects, the valley floor ends up colder
than the mountain above it — a temperature inversion, the reverse of the normal
pattern where air gets colder with altitude. Inversions are also what set up the fog that fills Adirondack valleys at dawn while summits stay clear above it — though fog additionally requires enough moisture in the trapped air, which daily temperature records alone can't tell you.

Measuring one requires temperature readings from two places at once: somewhere
high and somewhere low, close enough together to share the same weather. That
pairing is rare in mountain terrain, because weather stations are built where
people live and where planes land — in valleys.

## The data

Whiteface Mountain is the anchor. At 1,483m it is the only high-elevation weather
station in this dataset, sitting roughly 900m above the valley floors around it.
Without Whiteface there is no summit reading to compare against, and no way to
detect an inversion at all. The other five stations span the terrain below it,
close enough that all six experience the same passing weather systems — so
differences between them reflect local terrain rather than different storms.

| Station | Elevation | Setting |
|---|---|---|
| Whiteface Mountain | 1,483m | Summit |
| Newcomb | 576m | High Peaks valley |
| Lake Placid | 575m | High Peaks valley |
| Tupper Lake | 512m | High Peaks valley |
| Saranac Lake | 482m | High Peaks valley |
| Plattsburgh AFB | 50m | Lake Champlain plain |

**Date range: 1937–1946.** This is the only decade in which the summit station and
the valley stations all reported at once. Whiteface recorded temperatures from 1937
to 1946 and then stopped. The valley stations continue for decades afterward, but
with no summit reading to pair against them, later years cannot answer the question.

A research observatory has operated on the Whiteface summit since 1970, run by the
University at Albany's Atmospheric Sciences Research Center, but its measurements
are not part of GHCNd and are not used here.

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
