#!/usr/bin/python3

meinrad_string = r"1234567890-=!@#$%^&*()_+qwertyuiop[]\QWERTYUIOP{}|asdfghjkl;'ASDFGHJKL:\"zxcvbnm,./ZXCVBNM<>?"

for i in range(len(meinrad_string)):
  char = meinrad_string[i]
  ascii = ord(char)
  print(char + "\t" + str(ascii))
