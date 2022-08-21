'''

Script was made to extract specific columns from complete_data.csv file and to save it as the text file.

It can also be used with any csv file to save specific columns as the text.

Usage:
py csv_concat_to_txt.py input_file_path output_file_path "['Column name 1','Column name 2']"

Example:
py csv_concat_to_txt.py complete_data.csv complete_data_out.txt "['Project Title','Abstract Text']"

Please note:
Input and output file path should be in quotes if it contains space characters.

'''


import sys      #standard library
import ast      #standard library

import pandas as pd #3rd party package


def csv_concat_to_txt(infile : str, outfile : str, columns : str):
    infile = str(infile)
    outfile = str(outfile)
    columns = ast.literal_eval(columns)
    input_to_df = pd.read_csv(infile, usecols=columns).replace('(^\s+|\s+$|\n)', ' ', regex=True)
    input_to_df.to_csv(outfile, header=0, index=0, sep='\t')


if __name__ == "__main__":
    try:
        csv_concat_to_txt(sys.argv[1], sys.argv[2], sys.argv[3])
        print("Extraction completed successfully.")
    except:
        print("Extraction failed. Please check script arguments.")




