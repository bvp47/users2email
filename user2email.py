### Usernames to Emails ###
# Append a list of usernames to a domain name to create a list of email addresses

# Function to read usernames from a file
def read_usernames(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

# Function to write email addresses to a file


def write_emails(filename, emails):
    with open(filename, 'w') as file:
        for email in emails:
            file.write(f"{email}\n")


# Ask the user for a domain
domain = input("Please enter a domain (e.g., domain.com): ")

# Ask the user for the input and output filenames
input_filename = input(
    "Please enter the input filename with usernames (e.g., usernames.txt): ")
output_filename = input(
    "Please enter the output filename for email addresses (e.g., emails.txt): ")

# Read usernames from the input file
usernames = read_usernames(input_filename)

# Add the domain to each username to create the email addresses
email_addresses = [f"{username}@{domain}" for username in usernames]

# Write the email addresses to the output file
write_emails(output_filename, email_addresses)

print(f"Email addresses have been written to {output_filename}.")
