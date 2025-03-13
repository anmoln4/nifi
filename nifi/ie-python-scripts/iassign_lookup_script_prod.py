#!/usr/bin/python3
 
import sys
import csv
import argparse
def filter_csv(file_path, client_name, ci_name, probe, parameter):
    unique_groups = set()  # To store unique (CustomAssignmentGrp, CustomAssignmentGrpID) pairs
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            # Iterate through each row in the CSV
            for row in csv_reader:
                if (row['clientName'] == client_name and
                    row['ciName'] == ci_name and
                    row['Probe'] == probe and
                    row['Parameter'] == parameter):
                    # Add the unique values to the set
                    unique_groups.add((row['CustomAssignmentGrp'], row['CustomAssignmentGrpID']))
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
    # Print the unique groups
    #print("Unique CustomAssignmentGrp and CustomAssignmentGrpID:")
    for grp, grp_id in unique_groups:
        print(f"CustomAssignmentGrp: {grp}, CustomAssignmentGrpID: {grp_id}")
if __name__ == "__main__":
    file_path= sys.argv[1]
    client_name=sys.argv[2]
    ci_name=sys.argv[3]
    probe=sys.argv[4]
    parameter=sys.argv[5]

    filter_csv(file_path, client_name, ci_name, probe, parameter)