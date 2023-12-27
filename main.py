import boto3  
import csv    
import sys    

# Function to write a batch of items to a DynamoDB table
def batch_write(table_name, rows, region):
 """Writes a batch of items to a DynamoDB table.

 Args:
   table_name (str): Name of the DynamoDB table.
   rows (list): List of items to write to the table.
   region (str): AWS region where the table is located.

 Returns:
   bool: True if the batch write was successful, False otherwise.
 """

 dynamodb = boto3.resource('dynamodb', region_name=region)  # Create a DynamoDB resource
 table = dynamodb.Table(table_name)  # Get a reference to the table

 with table.batch_writer() as batch:  # Create a batch writer for efficient writes
   for row in rows:
     # Remove empty values from the row before writing to avoid errors
     row = {k: v for k, v in row.items() if v and v != '""'}
     batch.put_item(Item=row)  # Write the item to the table

 return True  # Indicate successful batch write

# Function to read data from a CSV file into a list of dictionaries
def read_csv(csv_file, list):
 """Reads data from a CSV file into a list of dictionaries.

 Args:
   csv_file (str): Path to the CSV file.
   list (list): List to store the parsed data.
 """

 rows = csv.DictReader(open(csv_file))  # Create a CSV reader
 for row in rows:
   list.append(row)  # Add each row as a dictionary to the list

# Main execution block
if __name__ == '__main__':
 # Get command-line arguments for table name, CSV file, and region
 table_name = sys.argv[1]
 csv_file = sys.argv[2]
 region = sys.argv[3]

 items = []  
 rows = read_csv(csv_file, items)  
 batch_write(table_name, rows, region)  # Write the data to DynamoDB