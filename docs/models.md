# Model list

## Staging
- **stg_ghcnd_observations** — one row per station, date, and element.
  Values converted from tenths of degrees to real units. Quality flags kept.
- **stg_ghcnd_stations** — one row per station: ID, name, lat, lon, elevation.

## Intermediate
- **int_daily_observations** — one row per station-day, with tmax, tmin and
  prcp as columns instead of separate rows.
- **int_station_day_spine** — every station crossed with every date from
  1937-01-01 to 1946-12-31, so missing days show up as rows rather than absences.
- **int_station_pairs** — each valley station paired with Whiteface, with the
  elevation difference between them.

## Marts
- **dim_station** — one row per station: elevation, and whether it's summit or valley.
- **fct_station_day** — one row per station-day: temperatures, quality flags,
  and whether the reading is missing.
- **fct_inversion_night** — one row per station-pair per night: valley low,
  summit low, the difference, and whether it counts as an inversion.
