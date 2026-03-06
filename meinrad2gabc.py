#!/usr/bin/python3

#import re, subprocess, io
#import bs4, lxml
#import xml.etree.ElementTree as ET
#import pandas as pd
import sys, docx, csv, re
import dictfile

inputdoc = sys.argv[1]

meinrad2021_csv = open("dictionaries/Meinrad2021.csv", 'r')
meinrad2021_contents = list(csv.reader(meinrad2021_csv, delimiter='\t'))
meinrada_csv = open("dictionaries/MeinradA_ascii.csv", 'r')
meinrada_contents = list(csv.reader(meinrada_csv, delimiter='\t'))

#TODO If character returns empty, add to list,
#Print "The following characters came up empty" + sorted list
#TODO instead of $$ codes, use $hex$
#Then produce, eg porrectus is ec7 + e[ad to b2] + Y
#TODO: List of signs and composition (see nabc doc)
#pu, vi, to, po, sa, cl, etc
#TODO Font dictionary should be value: [hex code, gabc value]
#Join codes by checking hex codes. If hexcode[0:2] in list then output hexcode[0:2] + "_" + gabcvalue
#Else output gabc_value
#Construct neumes with ruleset for connecting, eg porrectus is ec7 + ead + Y
#Create list of rules for this
#     
#TODO Standard CSV file format: Image, hex value, dec value, gabc, mapped value
#M2021: filename, hex value, dec value, gabc
#Others: hex value, dec value, char, M2021 map hex, M2021 map dec
#:nmap m $byw:let @a = printf("%d", eval(@"))<cr>$a<tab><esc>"ap


def m2gabc(mr_font, mr_text):
  meinrad_font = mr_font
  meinrad_string = mr_text
  meinrad_values = [ord(char) for char in meinrad_string]
  gabc_values = ""
  #TODO Output list
  #For i in list: if hex value in <punctum, etc> ouput gabc value + /
  #Tree of if statements, eg if i == ec7: if i+1 == ead then output porrectus, (gabc of i+1) + (gabc of i+2) + "/"
  for i in meinrad_values:
    if mr_font == "Meinrada":
      try:
        gabc_values = gabc_values + dictfile.Meinrad2021[dictfile.MeinradA[i]]
      except:
        print(str(i) + " not in dictionary")

    if mr_font == "Meinrad2021":
      try:
        gabc_values = gabc_values + dictfile.MeinradA[i]
      except:
        print(str(i) + " not in dictionary")

  print(gabc_values)
  return gabc_values

f = open(inputdoc, 'rb')
document = docx.Document(f)
f.close()

font_table = []

#Parse the text into rows and their font
for line in document.paragraphs:
  font_table.append([line.style.font.name, line.text])

#Convert text if it's a Meinrad font
for i in range(len(font_table)):
  font = font_table[i][0]
  text = font_table[i][1]
  if "Meinrad" in font:
    gabc_text = m2gabc(font, text)
    gabc_text = re.sub(r"\/{3,}"," ", gabc_text)
    print(gabc_text)
  else:
    print(font_table[i][1])

meinrad2021_csv.close()
meinrada_csv.close()
