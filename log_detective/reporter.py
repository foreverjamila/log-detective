
def generate_report(entries, repeated_failures, error_spikes, time_gaps):
    print("=== Log Detective Report ===\n")
    print(f"Parsed {len(entries)} entries. \n")

    print("REPEATED FAILURES")
    if repeated_failures:
        for failure in repeated_failures:
            print(f'  - "{failure}" occurred repeatedly.')
    else:
        print("  - None detected.")

    print("\nERROR SPIKES")
    if error_spikes:
        for spike in error_spikes:
            print(f"  - Spike detected starting at {spike.strftime('%Y-%m-%d %H:%M:%S')}.")
    else:
        print("  - None detected.")

    print("\nTIME GAPS")
    if time_gaps:
        for start, end in time_gaps:
            diff = end - start
            hours = diff.seconds // 3600
            minutes = (diff.seconds % 3600) // 60
            print(f"  - No activity between {start.strftime('%Y-%m-%d %H:%M:%S')} and {end.strftime('%Y-%m-%d %H:%M:%S')} ({hours}h {minutes}m).")
    else:
        print("  - None detected.")
