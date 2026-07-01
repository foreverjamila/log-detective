from log_detective.parser import parse_file

def main():
    print("Log Detective - starting up")
    
    result = parse_file("samples/sample.log")

    print(f"Parsed {len(result)} entries")
   


if __name__ == "__main__":
    main()