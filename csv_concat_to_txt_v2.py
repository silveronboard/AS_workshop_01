""" Simple script to extract specific columns from provided "complete_data.csv" file and to save it as the text file.

It can also be used with any csv file to save specific columns as the text.

Usage:
python csv_concat_to_txt.py input_file_path output_file_path "['Column name 1','Column name 2']"

Example:
py csv_concat_to_txt.py complete_data.csv complete_data_out.txt "['Project Title','Abstract Text']"

Please note:
Input and output file path should be in quotes if it contains space characters.
"""

import os
import sys              # Standard library
import ast              # Standard library

import pandas as pd     # 3rd party package


def csv_concat_to_txt(infile: str, outfile: str, columns: str):
    infile = str(infile)                                   # Ensure input file name argument data type is string
    outfile = str(outfile)                                 # Ensure output file name argument data type is string
    columns = ast.literal_eval(columns)                    # Convert columns argument string argument to list variable
    input_to_df = pd.read_csv(infile,
                              usecols=columns).replace('(^\s+|\s+$|\n)',
                                                       ' ', regex=True)     # Replaced EOL symbols with space
    input_to_df.to_csv("outfile.tmp", header=0, index=0, sep='\t')  # Output to temporary file
    tempfile = open("outfile.tmp", 'r')                             # Open temporary file for read
    tabless = open(outfile, 'w')                                     # Open output file for write
    for line in tempfile:                                           # Loop through lines
        tabless.write(line.replace("\t", " "))                      # Loop through lines
    tempfile.close()                                                # Close temporary file
    tabless.close()                                                 # close output file
    os.remove("outfile.tmp")                                        # delete temporary file


if __name__ == "__main__":
    csv_concat_to_txt(sys.argv[1], sys.argv[2], sys.argv[3])
    print("Extraction completed successfully.")

