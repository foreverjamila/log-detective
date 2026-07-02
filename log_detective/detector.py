from datetime import datetime, timedelta

def detect_repeated_failures(entries):
    counts = {}

    for entry in entries:
        if entry.level == "ERROR":
            if entry.message in counts:
                counts[entry.message] += 1
            else:
                counts[entry.message] = 1

    repeated = []

    for key, value in counts.items():
        if value > 10:
            repeated.append(key)

    return repeated


def detect_error_spike(entries, threshold=10, window_minutes=10):
    spikes = []

    for i, entry in enumerate(entries):
        if entry.level == "ERROR":
            count = 0
            for other in entries[i:]:
                diff = other.timestamp - entry.timestamp
                if diff < timedelta(minutes=window_minutes):
                    count += 1
                else:
                    break
            if count >= threshold:
                if len(spikes) == 0 or entry.timestamp - spikes[-1] > timedelta(minutes=window_minutes):
                    spikes.append(entry.timestamp)
                
    return spikes
                     
def detect_time_gaps(entries, threshold=30):
    gaps = []

    for i in range(1, len(entries)):

        diff = entries[i].timestamp - entries[i - 1].timestamp

        if diff > timedelta(minutes=threshold):
            gaps.append((entries[i - 1].timestamp, entries[i].timestamp))

    return gaps

