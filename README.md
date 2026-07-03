# Log Detective

A command-line tool that parses log files, detects patterns, and outputs a plain-English summary report.

## What it detects

- **Repeated failures** — error messages that appear an unusual number of times
- **Error spikes** — bursts of 10+ errors within a 10-minute window
- **Time gaps** — periods of silence longer than 30 minutes

## Usage

```bash
python -m log_detective.main <path-to-log>
```

Example:

```bash
python -m log_detective.main samples/sample.log
```

Output:

```
=== Log Detective Report ===

Parsed 158 entries.

REPEATED FAILURES
  - "Database connection failed" occurred repeatedly.

ERROR SPIKES
  - Spike detected starting at 2026-07-01 14:00:15.

TIME GAPS
  - No activity between 2026-07-01 10:58:00 and 2026-07-01 13:00:00 (2h 2m).
```

## Log format

Log lines must follow this format:

```
YYYY-MM-DD HH:MM:SS LEVEL message
```

Example:

```
2026-07-01 14:03:11 ERROR Connection refused
2026-07-01 14:05:00 INFO  Request processed
```

## Project structure

```
log_detective/
    parser.py    # Parses raw log lines into LogEntry objects
    detector.py  # Detects patterns in parsed entries
    reporter.py  # Formats findings into a readable report
    main.py      # CLI entrypoint
samples/
    sample.log        # Example log file
    generator_logs.py # Script to regenerate 
```

## Generate a new sample log

```bash
python samples/generator_logs.py
```

## Requirements

Python 3.13+. No external dependencies.
