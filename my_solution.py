import sys
import os


def find_longest_cycle(graph):
    max_cycle = 0

    def dfs(node, path, path_set):
        nonlocal max_cycle

        path.append(node)
        path_set.add(node)

        for neighbor in graph.get(node, []):
            if neighbor in path_set:
                # print('Cycle found')
                cycle_length = len(path) - path.index(neighbor)
                if cycle_length > max_cycle:
                    max_cycle = cycle_length
            else:
                dfs(neighbor, path, path_set)

        path.pop()
        path_set.remove(node)

    for start_node in graph:
        dfs(start_node, [], set())

    return max_cycle


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

    max_cycle_length = 0
    max_cycle_claim = None
    max_cycle_status = None

    for (claim_id, status_code), edges in routes.items():
        graph = {}

        for source, destination in edges:
            graph.setdefault(source, []).append(destination)

        longest_cycle = find_longest_cycle(graph)

        if longest_cycle > max_cycle_length:
            max_cycle_length = longest_cycle
            max_cycle_claim = claim_id
            max_cycle_status = status_code

    if max_cycle_claim is None:
        return

    result = f"{max_cycle_claim},{max_cycle_status},{max_cycle_length}"

    print(result)

    with open("solution.txt", "w", encoding="utf-8") as f:
        f.write(result)


if __name__ == "__main__":
    main()
