# Learnings

## Python
- Use underscores in filenames, not hyphens. A hyphen means subtraction to
  Python, so `download-all.py` can't be imported by other code. Runs fine
  directly, breaks later.
- Number scripts by pipeline order (`01_download.py`) so the sequence is obvious
  without asking.
- `urlretrieve` overwrites silently. No warning, no skip. Idempotency has to be
  written in deliberately.

## GHCNd format
- Each line is one station, one month, one element — with 31 day-slots regardless
  of month length. February carries slots for the 30th and 31st, filled with -9999.
- Station ID network code is the third character: C = COOP (daily volunteer),
  W = WBAN (automated airport), R = RAWS, 1 = CoCoRaHS (precipitation only).
- Blank quality flag means the value passed NOAA's checks.

## Terminal
- `nano` saves with Ctrl+O then Enter, exits with Ctrl+X. Ctrl, not Cmd, on a Mac.
- `grep "text" file` searches a file for matching lines.
- `wc -l file` counts lines. `head -3 file` shows the first three.
