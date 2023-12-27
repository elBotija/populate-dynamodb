# DynamoDB Batch Writer

This Python script writes data from a CSV file to a DynamoDB table.

## Description

This script uses the Boto3 library to interact with DynamoDB. It reads data from a CSV file and writes it to the table.  
This helps to improve performance for bulk data operations.

## Requirements

* Python 3.x
* Boto3 library (`pip install boto3`)

## Usage

1. Set up AWS credentials:

    + Ensure you have AWS credentials configured for programmatic access. You can use environment variables, a credentials file, or an IAM role.

    + Refer to the official Boto3 documentation for details: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html
2. Run the script from the terminal:

    ´´´bash
    python3 main.py <table_name> <csv_file> <region>
    ´´´

  + Replace placeholders with actual values:
    + <table_name>: Name of the DynamoDB table
    + <csv_file>: Path to the CSV file containing the data
    + < region>: AWS region where the table is located (e.g., us-east-1)

## Additional Notes
  - The script handles empty values in CSV rows by removing them before writing to DynamoDB.

  - It uses a batch writer for efficient writes, optimizing performance for bulk data operations.
  
  - For more customization, explore additional Boto3 features for DynamoDB interactions.

  - Consider error handling and logging for production use.

## Disclaimer
This script is not recommended for production use or large-scale data ingestion due to the following limitations:

 - Lack of capacity planning and monitoring: It does not assess or adjust provisioned read/write capacity units (WCUs/RCUs) to handle varying workloads, potentially leading to throttling or cost overruns.

  - Unoptimized batch size: The fixed batch size of 100 items may not be optimal for all data sizes, potentially affecting performance and efficiency.
  - No retry logic: It does not handle throttled requests, which could result in incomplete data ingestion.

 - Potential hot partition issues: It does not address skewed data distribution, which could exhaust capacity units for specific partitions.

For large-scale data ingestion, consider using tools and techniques that address these limitations, such as:

 - DynamoDB Streams for complex data pipelines
  - Capacity planning and monitoring tools
  - Optimized batch sizing strategies
  - Retry mechanisms for throttled requests
  - Data distribution and write sharding to prevent hot partitions

The creator is not responsible for any use of this script. Use it at your own risk and consider the aforementioned limitations.
