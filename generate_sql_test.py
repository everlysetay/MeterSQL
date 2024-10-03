import os
import glob
import csv
import unittest
from io import StringIO
from contextlib import redirect_stdout

from generate_sql import read_csv_files, generate_insert_statements 

class TestSqlGeneration(unittest.TestCase):
    def setUp(self):
        # Create test directories
        self.test_input_dir = 'test_res'
        self.test_output_dir = 'test_output'
        
        os.makedirs(self.test_input_dir, exist_ok=True)
        os.makedirs(self.test_output_dir, exist_ok=True)
        
        # Create a sample CSV file
        self.sample_csv_path = os.path.join(self.test_input_dir, 'test_data.csv')
        with open(self.sample_csv_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['200', 'nmi_value1', 'other_data1', 'other_data1', 'other_data1', 'other_data1', 'other_data1', 'kWh', '30', 'other_data1'])
            writer.writerow(['300', 'timestamp2', 'other_data2', 'other_data2', 'other_data2', 'other_data2', 'other_data2', 'other_data2', 'other_data2', 'other_data2', 'other_data2', 'other_data2', 'other_data2', 'other_data2', 'consumption2'])

    def tearDown(self):
        # Clean up test directories
        for folder in [self.test_input_dir, self.test_output_dir]:
            for filename in glob.glob(os.path.join(folder, '*')):
                os.remove(filename)
            os.rmdir(folder)

    def test_sql_generation(self):
        read_csv_files(self.test_input_dir, self.test_output_dir)
        
        # Check if SQL file was created
        output_sql_file = os.path.join(self.test_output_dir, 'test_data.sql')
        self.assertTrue(os.path.exists(output_sql_file))

        # Check the content of the generated SQL file
        with open(output_sql_file, 'r') as sql_file:
            content = sql_file.read()
            expected_statement = "INSERT INTO meter_readings (nmi, timestamp, consumption) VALUES (nmi_value1, 'timestamp2', 'consumption2');\n"
            self.assertIn(expected_statement, content)

if __name__ == "__main__":
    unittest.main()
