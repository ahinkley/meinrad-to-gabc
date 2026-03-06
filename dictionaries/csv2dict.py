#!/usr/bin/python3

import subprocess, sys, re, os, csv

input_csv = sys.argv[1]
output_csv = input_csv
output_dict = re.sub(r"csv$", "dict", output_csv)
output_file = re.sub(r".csv$", "", output_csv)

print(input_csv)
csv_table = open(input_csv, 'r')
contents = list(csv.reader(csv_table, delimiter='\t'))

print(output_dict)

dictfile = open(output_dict, 'w')
dictfile.write(output_file + " = {\n")
for row in contents[:-1]:
  dictfile.write(str(row[2]) + ": \"" + str(row[3]) + "\",\n")
dictfile.write(str(contents[-1][2]) + ": \"" + str(row[3]) + "\"\n")
dictfile.write("}\n")
dictfile.close()    

csv_table.close()
