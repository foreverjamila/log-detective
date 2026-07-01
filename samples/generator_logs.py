# Imports
from datetime import datetime, timedelta
import random
import os

# Configuration
START_TIME = datetime(2026, 7, 1, 9, 0, 0)
END_TIME = datetime(2026, 7, 1, 17, 0, 0)

GAP_START = datetime(2026, 7, 1, 11, 0, 0)
GAP_END = datetime(2026, 7, 1, 13, 0, 0)

SPIKE_START = datetime(2026, 7, 1, 14, 0, 0)
SPIKE_END = datetime(2026, 7, 1, 14, 10, 0)

# Log Messages
INFO_MESSAGES = [
    "Application started",
    "User logged in",
    "User logged out",
    "Request processed",
    "Dashboard loaded",
    "Cache refreshed",
    "Settings updated",
    "Payment received",
    "Session created",
    "Email sent"
]

WARNING_MESSAGES = [
    "High memory usage",
    "Slow database query",
    "Disk usage above 80%",
    "High CPU usage",
    "Retrying API request"
]

ERROR_MESSAGES = [
    "Database connection failed",
    "Authentication failed",
    "API timeout",
    "Payment processing failed",
    "Unable to save record"
]

REPEATED_ERROR = "Database connection failed"

# Storage 
log_entries = []

def add_log(timestamp, level, message):
    """Store one log entry"""
    log_entries.append({
        "timestamp": timestamp,
        "level": level,
        "message": message
    })

# Generate baseline logs
current = START_TIME

while current <= END_TIME:

    # Skip the silence gap (11am-1pm)
    if GAP_START <= current < GAP_END:
        current = GAP_END
        continue

    # Mostly INFO, occasional WARNING, rare ERROR
    level = random.choices(
        ["INFO", "WARNING", "ERROR"],
        weights=[85, 12, 3],
        k=1
    )[0]

    if level == "INFO":
        message = random.choice(INFO_MESSAGES)

    elif level == "WARNING":
        message = random.choice(WARNING_MESSAGES)

    else:
        message = random.choice(ERROR_MESSAGES)

    add_log(current, level, message)

    # Next log occurs 1-5 minutes later
    current += timedelta(minutes=random.randint(1, 5))


# Ensure max 2 baseline errors/hour
# Remove extra errors if any
errors_per_hour = {}

filtered_logs = []

for log in log_entries:

    if log["level"] != "ERROR":
        filtered_logs.append(log)
        continue

    hour = log["timestamp"].hour

    errors_per_hour.setdefault(hour, 0)

    if errors_per_hour[hour] < 2:
        filtered_logs.append(log)
        errors_per_hour[hour] += 1

log_entries = filtered_logs


# Error spike (20 errors)

for _ in range(20):

    seconds = random.randint(
        0,
        int((SPIKE_END - SPIKE_START).total_seconds())
    )

    timestamp = SPIKE_START + timedelta(seconds=seconds)

    add_log(
        timestamp,
        "ERROR",
        random.choice(ERROR_MESSAGES)
    )


# Repeated failure

for _ in range(12):

    while True:
        

        random_minutes = random.randint(
            0,
            int((END_TIME - START_TIME).total_seconds() // 60)
        )

        timestamp = START_TIME + timedelta(minutes=random_minutes)

        # Don't place inside silence gap
        if not (GAP_START <= timestamp < GAP_END) and not (SPIKE_START <= timestamp < SPIKE_END):
            break

    add_log(
        timestamp,
        "ERROR",
        REPEATED_ERROR
    )


# Sort by timestamp

log_entries.sort(key=lambda log: log["timestamp"])

# 6. Write to file

with open("samples/sample.log", "w") as file:

    for log in log_entries:

        line = (
            f"{log['timestamp']:%Y-%m-%d %H:%M:%S} "
            f"{log['level']} "
            f"{log['message']}\n"
        )

        file.write(line)

print(f"Generated {len(log_entries)} log entries.")
print("Saved to samples/sample.log")