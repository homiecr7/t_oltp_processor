import os
import site


site.addsitedir(os.path.join(os.getcwd(), 'src'))
from utils import get_connections, ingest_to_database

HOST = "redacted"
USER = "redacted"
PASSWORD = "redacted"
DATABASE = "redacted"
PORT = 3306

def main():
    conn = get_connections(HOST, USER, PASSWORD, DATABASE, PORT)
    table_name = "weather_daily_information"
    ingest_to_database(conn, table_name)


if __name__ == "__main__":
    main()



# import pandas as pd
# import os

# def compile_csv_files(output_file):
#     # Read the first CSV file to get the header
#     folder_path = "data/london_smart_meters/daily_dataset/daily_dataset/"
#     csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
#     file_path = os.path.join(folder_path, csv_files[0])
#     first_file = pd.read_csv(file_path)
#     header = first_file.columns.tolist()

#     # Initialize an empty DataFrame to store the concatenated data
#     header = ["LCLid", "day", "energy_median", "energy_mean", "energy_max", "energy_count", "energy_std", "energy_sum", "energy_min", "block"]
#     compiled_data = pd.DataFrame(columns=header)
#     # Iterate through the input CSV files, skipping the header for the rest
#     print(csv_files)
#     for file in csv_files:
#         file_path = os.path.join(folder_path, file)
#         if file == csv_files[0]:
#             # Skip reading header for the first file (already obtained)
#             data = first_file
#             data["block"] = file.replace(".csv", "")
#         else:
#             # Read the file without header
#             data = pd.read_csv(file_path, header=None, names=header)
#             data["block"] = file.replace(".csv", "")
#         # Append data to the compiled DataFrame
#         compiled_data = compiled_data._append(data, ignore_index = True)
#     # Write the compiled data to a new CSV file

#     compiled_data.to_csv(output_file, index=False)


# # Example usage:
# # Replace 'file1.csv', 'file2.csv', ..., 'file100.csv' with your actual file names
# output_file_name = 'all_blocks.csv'

# compile_csv_files(output_file_name)

# df = pd.read_csv("all_blocks.csv")
# distinct_values = df.shape[0]
# print(distinct_values)

