# Learnings

## Virtual environments
- A virtual environment (venv) is a per-project folder holding that project's
  packages, so versions can't collide between projects. Use one for any project
  that installs packages.
- Create once per project: `python3 -m venv .venv`
- Activate every time you open a new Terminal window: `source .venv/bin/activate`
  You'll see `(.venv)` at the start of the prompt when it's active. Activation
  does not persist across windows or reboots.
- Install into it with `pip install <package>`. If `(.venv)` isn't showing, pip
  installs system-wide instead — check the prompt first.
- Record exact versions with `pip freeze > requirements.txt`, and commit that file.
  Reinstall elsewhere with `pip install -r requirements.txt`.
- Commit `requirements.txt`; never commit `.venv/` — it's large and specific to
  one machine.
- pip warns when a newer pip exists. Harmless, unrelated to your code.
  
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
