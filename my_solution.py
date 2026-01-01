import sys
import os


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 my_solution.py <input_file>")
        sys.exit(1)

    file_path = sys.argv[1]

    if not os.path.isfile(file_path):
        print(f"File not found: {file_path}")
        sys.exit(1)

    # Key: (claim_id, status_code)
    # Value: list of (source, destination)
    routes = {}

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            source, destination, claim_id, status_code = line.split("|")
            key = (claim_id, status_code)

            if key not in routes:
                routes[key] = []

            routes[key].append((source, destination))


if __name__ == "__main__":
    main()
