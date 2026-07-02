from log_detective.parser import parse_file
from log_detective.detector import detect_repeated_failures, detect_error_spike, detect_time_gaps
def main():
    print("Log Detective - starting up")
    
    result = parse_file("samples/sample.log")

    repeated_failures = detect_repeated_failures(result)
    error_spikes = detect_error_spike(result)
    time_gaps = detect_time_gaps(result)

    for failure in repeated_failures:
        print(f" Repeated failure: {failure}")

    for spike in error_spikes:
        print(f" Error spike at: {spike.strftime('%Y-%m-%d %H:%M:%S')}")

    for start, end in time_gaps:
        print(f" No activity between {start.strftime('%Y-%m-%d %H:%M:%S')} and {end.strftime('%Y-%m-%d %H:%M:%S')}")
    
   

if __name__ == "__main__":
    main()
