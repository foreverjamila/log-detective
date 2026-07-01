from datetime import datetime

class LogEntry():
    def __init__(self, timestamp, level, message):
        self.timestamp = timestamp
        self.level = level
        self.message = message


def parse_line(line):
    result = line.split(" ", 3)

    timestamp_str = result[0] + " " + result [1]
    timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")

    level = result[2]
    message = result[3].strip()

    return LogEntry(timestamp, level, message)
    
def parse_file(filepath):
    entries = []
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                entries.append(parse_line(line))
            except ValueError:
                continue
    return entries


