# Decisions

A running log of choices made on this project and the reasoning behind them.
Oldest first.

---

## 2026-09-17

### Warehouse: Snowflake, not BigQuery
BigQuery was free and already configured, but finding public datasets and getting
started there was a persistent source of friction. At 5–7 hrs/week, friction costs
more than the ~$15–25/month Snowflake will run. The trial covers the first month.

### BigQuery returns as a second dbt target (N10)
Not abandoned — deferred. Building the same models against two warehouses
demonstrates dialect handling via dbt's dispatch macros, and reuses the setup
already done.

### Local development on DuckDB
dbt runs against DuckDB locally and is verified against Snowflake. Keeps the
Snowflake bill near zero and lets CI run without warehouse credentials. Not an
optional add-on.

### Source: raw NCEI files, not Snowflake Marketplace
Snowflake's Marketplace GHCNd listing drops observations that failed NOAA's quality
checks and only goes back to 2000. This project is about quality flags, so the
filtered copy removes the subject. Raw files are also warehouse-agnostic.

### Containerize at N2 and N3b, not from the start
A minimal Dockerfile once there's a script to run (N2); full Compose setup once
there's a dbt project to put in it (N3b). Nothing to containerize before that.

---

## 2026-09-18

### Daily data only; hourly is not available for this question
Whiteface (USC00309383) is a COOP station — a volunteer reading instruments once
daily. It is not in GHCNh. There are no high-elevation hourly stations in the
Adirondacks, because airports are in valleys. Hourly would have given inversion
*timing*; daily still gives frequency and seasonality.

### Scope: detect and characterize, not predict
Predicting inversions requires humidity, wind and cloud base. Detecting historical
inversions from daily minimum temperatures is defensible with the data available.
Prediction would be overclaiming.

### Six stations, one per location
Where two stations covered the same place, kept the longer TMIN record.
Dropped: Plattsburgh 1 S and Tahawus (no TMIN), Newcomb (TMIN starts 1967),
Keene Valley 1 W (TMIN ends 1918).

### Date range: 1937–1946
The only decade in which Whiteface and the valley stations reported simultaneously.
Whiteface TMIN ends in 1946. A research observatory has run on the summit since
1970, but its data is not in GHCNd and is not used here.

### README states the fog caveat explicitly
Inversions are necessary but not sufficient for valley fog — the trapped air must
also be moist enough to saturate, which daily temperature records can't show.
Stated up front rather than left for a reader to catch.

### Cost controls created before any data was loaded
NOAA_MONITOR: 50 credits monthly, notify at 80%, suspend at 100%, suspend
immediately at 110%. NOAA_WH: Standard Gen1, X-Small, 60-second auto-suspend.
Chose Gen1 over Adaptive because Adaptive auto-scales to workload, which is the
opposite of what a cost-capped learning project wants.

### Download full station history; filter dates in dbt
Each station has one file covering its entire record — there is no per-year
option. Changing the date range later means editing a filter, not re-downloading.
Full history is also needed for the N4 completeness analysis.

### Unit conversion happens in staging, not ingestion
Elements don't share units: temperature is tenths of a degree C, precipitation
tenths of a mm, snow depth whole mm. A blanket divide-by-10 would be wrong. Raw
load preserves the source exactly, so a conversion error means fixing a model
rather than re-downloading.

### Missing values are skipped at parse time
The .dly format pads every month to 31 days, so February carries slots for the
30th and 31st filled with -9999. These become absent rows rather than rows with
null values. Genuine gaps still surface later against the date spine.

### Snowflake authentication: browser-based SSO for now, key-pair later
The Snowflake account was created through Google sign-in, so no password exists.
The ingestion script uses `externalbrowser` authentication: it opens a browser
window, Google handles the login, and no credential is stored on disk. Better than
storing a password, but it requires a human present to click through, so it cannot
run unattended. At N9, when GitHub Actions builds the project automatically, this
switches to key-pair authentication (a cryptographic key file instead of an
interactive login). Noted now so the change isn't a surprise then.

### Account edition is Enterprise, not Standard
The trial account provisioned as Enterprise edition, where credits cost more than
the Standard rate assumed when the resource monitor was set. The 50-credit monthly
cap is therefore worth roughly $150, not $100. Left the cap unchanged — actual
usage is expected to be a few credits per month, and the cap exists to catch
runaway queries rather than to budget.

---

## Gotchas

- **macOS certificates.** Python installed from python.org cannot verify HTTPS
  until you run `/Applications/Python 3.10/Install Certificates.command`.
  Symptom: `CERTIFICATE_VERIFY_FAILED`.
- **Snowflake Workspaces editor.** Will not run multi-statement scripts. Errors
  with "Actual statement count N did not match the desired statement count 1."
  Run statements individually, or use the UI.
- **Station file URL pattern.**
  `https://www.ncei.noaa.gov/pub/data/ghcn/daily/all/{station_id}.dly`
