import os
import glob
import csv

def read_csv_files(input_directory, output_directory):
    # Create a path for the directory and search for all .csv files
    csv_files = glob.glob(os.path.join(input_directory, '*.csv'))
    
    # Ensure output directory exists
    os.makedirs(output_directory, exist_ok=True)

    # Read each CSV file
    for csv_file in csv_files:
        # Construct output SQL file name
        output_sql_file = os.path.join(output_directory, os.path.basename(csv_file)[:-4] + '.sql')
        generate_insert_statements(csv_file, output_sql_file)

def generate_insert_statements(csv_file, output_sql_file):
    # Open the input CSV file
    with open(csv_file, mode='r', newline='') as file:
        reader = csv.reader(file)
        
        # Initialize a list to hold the SQL statements
        sql_statements = []
        
        # Read rows
        rows = list(reader)
        for i in range(len(rows)):
            # Ensure we have enough lines to process
            if i + 1 < len(rows):
                line_1 = rows[i]
                line_2 = rows[i + 1]
                
                if line_1[0] == '200' and line_2[0] == '300':
                    # Prepare INSERT statements
                    insert_statement = f"INSERT INTO meter_readings (nmi, timestamp, consumption) VALUES ({line_1[1]}, '{line_2[1]}', '{line_2[14]}');"
                    sql_statements.append(insert_statement)

    # Write SQL statements to the output file
    with open(output_sql_file, mode='w') as sql_file:
        for statement in sql_statements:
            sql_file.write(statement + "\n")

if __name__ == "__main__":
    input_directory = 'res'  # Path to your 'res' directory
    output_directory = 'output'  # Path to your desired output directory
    read_csv_files(input_directory, output_directory)
