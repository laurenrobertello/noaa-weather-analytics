# Snowflake setup

Account edition: Standard (trial)
Region: <whatever you picked>
Role used: ACCOUNTADMIN for setup, SYSADMIN for everyday work

## Warehouse
Name: NOAA_WH
Size: X-Small
Auto-suspend: 60 seconds
Auto-resume: on

## Database and schemas
Database: NOAA
Schemas: RAW (ingestion target), ANALYTICS (dbt output)

## Resource monitor
Name: NOAA_MONITOR
Credit quota: 50 per month
Action at 100%: suspend immediately
Action at 80%: notify
Assigned to: NOAA_WH

## Notes
Trial includes $400 in credits, expiring 2026-10-18.
Credentials live in .env locally and are never committed.
