import csv
import datetime
import glob
import os

OUTPUT = "observations.csv"

def parse_line(line):
    station = line[0:11]
    year = int(line[11:15])
    month = int(line[15:17])
    element = line[17:21]

    rows = []
    for day in range(1, 32):
        start = 21 + (day - 1) * 8
        value = line[start:start + 5].strip()
        mflag = line[start + 5:start + 6].strip()
        qflag = line[start + 6:start + 7].strip()
        sflag = line[start + 7:start + 8].strip()

        if value == "-9999":
            continue

        try:
            obs_date = datetime.date(year, month, day)
        except ValueError:
            continue

        rows.append({
            "station_id": station,
            "obs_date": obs_date.isoformat(),
            "element": element,
            "value": int(value),
            "mflag": mflag,
            "qflag": qflag,
            "sflag": sflag,
        })
    return rows


files = sorted(glob.glob("*.dly"))
print(f"Found {len(files)} files.")

total = 0
with open(OUTPUT, "w", newline="") as out:
    writer = csv.DictWriter(out, fieldnames=[
        "station_id", "obs_date", "element", "value", "mflag", "qflag", "sflag"
    ])
    writer.writeheader()

    for path in files:
        count = 0
        with open(path) as f:
            for line in f:
                for row in parse_line(line):
                    writer.writerow(row)
                    count += 1
        total += count
        print(f"{os.path.basename(path)}: {count:,} rows")

print(f"\nTotal: {total:,} rows written to {OUTPUT}")
