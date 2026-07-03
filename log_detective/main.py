from log_detective.parser import parse_file
from log_detective.detector import detect_repeated_failures, detect_error_spike, detect_time_gaps
from log_detective.reporter import generate_report
import sys

def main():
    print("Log Detective - starting up")

    if len(sys.argv) < 2:
        print("Usage: python -m log_detective.main <path-to-log>")
        sys.exit(1)
    
    result = parse_file(sys.argv[1])

    repeated_failures = detect_repeated_failures(result)
    error_spikes = detect_error_spike(result)
    time_gaps = detect_time_gaps(result)

    generate_report(result, repeated_failures, error_spikes, time_gaps)

    
   

if __name__ == "__main__":
    main()
