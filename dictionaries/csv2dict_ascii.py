#!/usr/bin/python3

import subprocess, sys, re, os, csv

input_csv = sys.argv[1]
output_csv = input_csv
output_dict = re.sub(r"_ascii.csv$", ".dict", output_csv)
output_file = re.sub(r"_ascii.csv$", "", output_csv)

print(input_csv)
csv_table = open(input_csv, 'r')
contents = list(csv.reader(csv_table, delimiter='\t'))

print(output_dict)

dictfile = open(output_dict, 'w')
dictfile.write(output_file + " = {\n")
for row in contents[:-1]:
  try:
    if str(row[4]) != "":
      dictfile.write(str(row[1]) + ": " + str(row[4]) + ",\n")
    else:
      dictfile.write(str(row[1]) + ": 0,\n")
  except:
    dictfile.write(str(row[1]) + ": 0,\n")

try:
  if contents[-1][4] != "":
    dictfile.write(str(contents[-1][1]) + ": " + str(ontents[-1][4]) + "\n")
  else:
    dictfile.write(str(contents[-1][1]) + ": 0\n")
except:
  dictfile.write(str(contents[-1][1]) + ": 0,\n")

dictfile.write("}\n")
dictfile.close()    

csv_table.close()
