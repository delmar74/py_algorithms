##############################
# Read self code
##############################

import os

def self_read():
  file_name = os.path.basename(__file__)
  file = open(file_name,"r")
 
  print(file.read()) 

self_read()
