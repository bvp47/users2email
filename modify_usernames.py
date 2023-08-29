import argparse

# Function to read lines from a file


def read_lines(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

# Function to write lines to a file


def write_lines(filename, lines):
    with open(filename, 'w') as file:
        for line in lines:
            file.write(f"{line}\n")


def main():
    parser = argparse.ArgumentParser(
        description="Add a domain to usernames or strip the domain from usernames.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-a', '--add', help='Domain to add to usernames')
    group.add_argument('-s', '--strip', action='store_true',
                       help='Strip domain from usernames')
    parser.add_argument('-i', '--input', required=True, help='Input filename')
    parser.add_argument('-o', '--output', required=True,
                        help='Output filename')

    args = parser.parse_args()

    # Read lines from the input file
    lines = read_lines(args.input)

    if args.add:
        # Add domain to usernames
        modified_lines = [f"{line}@{args.add}" for line in lines]
    elif args.strip:
        # Strip domain from usernames
        modified_lines = [line.split('@')[0] for line in lines]

    # Write modified lines to the output file
    write_lines(args.output, modified_lines)

    print(f"Operation complete. Output written to {args.output}.")


if __name__ == "__main__":
    main()
