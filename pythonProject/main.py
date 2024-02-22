

import csv

def create_key(first_name, last_name, dob):
    # Extract month and day from DOB
    mm_dd = dob[-5:].replace("-", "")

    # Create the key
    key = first_name[0] + last_name[:5] + mm_dd
    return key

def process_csv(input_file, output_file):
    with open(input_file, 'r') as csv_input:
        reader = csv.reader(csv_input)
        next(reader)

        rows = []
        for row in reader:
            first_name = row[0]
            last_name = row[1]
            dob = row[2]
            key = create_key(first_name, last_name, dob)
            row.append(key)
            rows.append(row)

    with open(output_file, 'w', newline='') as csv_output:
        writer = csv.writer(csv_output)
        writer.writerow(["FirstName", "LastName", "DOB", "Key"])
        writer.writerows(rows)

# Input and output file paths
input_file = "MidTermIn.csv"
output_file = "MidTermOut.csv"

# Process the CSV files
process_csv(input_file, output_file)