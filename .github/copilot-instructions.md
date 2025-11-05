## Purpose
This repository is a collection of small, standalone Python scripts and learning exercises. The guidance below helps AI coding agents make productive, low-risk edits: run scripts, find data files, and keep changes compatible with how files are executed today.

## Big picture
- No single application or package — mostly top-level, runnable scripts (for example `EGM.py`, `Number Guessing Game.py`, `hello_world.py`).
- Some scripts are interactive (use `input()`), some read/write JSON/text (see `egm_stats.json`, `egm_audit_log.txt`), and one local DB exists (`integration_practice.db`).

## How files are run (developer workflow)
- Run a script from the repo root with the system Python; on Windows PowerShell use:
  - `python .\EGM.py` or `python .\"Number Guessing Game.py"` (note: several filenames contain spaces).
- There is no centralized test runner or requirements manifest in the repo. If new third-party packages are introduced, add a `requirements.txt` and document install steps.

## Project-specific patterns and gotchas (do not assume defaults)
- Filenames often contain spaces (e.g. `Number Guessing Game.py`). When creating imports or referencing files, prefer safe names or use quoted paths. Avoid refactoring filenames unless you update all references and verify run commands.
- Scripts are primarily taught-style examples: they expect console interaction and side-effects (printing, opening web pages via `webbrowser`, reading/writing local files). Changes should not convert interactive scripts into background services without a clear reason.
- Data files are stored at repo root (e.g. `egm_stats.json`, `egm_audit_log.txt`, `integration_practice.db`). When modifying I/O, preserve existing schema/format unless the change is deliberate and backward-compatible.

## Integration points & external dependencies
- Search for `import` lines to find external modules. Example: some files reference `numpy` (e.g. `import numpy as np` appears in a filename). If a script requires external packages, add them to `requirements.txt` and mention how to install (`pip install -r requirements.txt`).
- Network or system calls: `webbrowser.open(...)` is used in `hello_world.py`. Avoid making network calls during automated runs unless explicitly required.

## Concrete examples agents can use
- To run the EGM/game script manually and observe behavior:
  - `python .\EGM.py` — prompts for credits, uses `random.randint`, writes/reads `egm_stats.json` (if you change the JSON layout, update any parsing code).
- To inspect a quick script that opens a URL:
  - `python .\hello_world.py` — demonstrates `webbrowser.open(...)` and basic string methods.

## Editing guidance for AI agents
- Prefer small, localized edits. Many scripts are single-file; changing interfaces (function signatures, file names) often requires multiple coordinated edits.
- When adding new modules, use snake_case filenames and place reusable code in a new package directory (create `__init__.py`) rather than editing multiple top-level scripts.
- If you add tests or CI, include a lightweight runner (pytest) and a README section explaining how to run them.

## What *not* to change without confirmation
- Renaming or moving interactive scripts with spaces in their names.
- Changing the structure or schema of existing JSON/text files unless you update all readers/writers.

## Where to look first (high-value files)
- `EGM.py` — example of interactive game + JSON usage.
- `Number Guessing Game.py` — input parsing and looping patterns.
- `hello_world.py` — small helpers and `webbrowser` usage.
- `egm_stats.json`, `egm_audit_log.txt`, `integration_practice.db` — data files to inspect before modifying I/O.

---
If anything above is unclear or you want the file tailored (for example, to prefer automated tests or to add a `requirements.txt`), tell me which area to expand and I will iterate.
