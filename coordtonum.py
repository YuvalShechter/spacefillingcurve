import numpy as np
from decimal import Decimal

def nuzzles_you_float(nums, cap):
  n_dec = 0
  for j in range(len(nums)):
    for i, num in enumerate(nums[j]):
      #If num is just an integer, no decimals to truncate
      if int(num) == num:
        continue
      #Truncate decimals
      n_dec_i = len(str(num).split(".")[-1])
      if n_dec_i <= cap:
        n_dec = n_dec if n_dec >= n_dec_i else n_dec_i
      else:
        n_dec = cap
        break

  for j in range(len(nums)):
    for i, num in enumerate(nums[j]):
      nums[j][i] = int(nums[j][i] * (10**n_dec))
  return nums

def convert_to_binary(data, cap):
  binary_data = []
  integer_data = nuzzles_you_float(data, cap)
  for arr in range(len(integer_data)):
    elements = []
    for i in range(len(integer_data[arr])):
      elements.append('{0:b}'.format(integer_data[arr][i]))
    binary_data.append(elements)
  return binary_data

def pad_binary(data):
  #Holds length of largest string in data
  max_len = len(data[0][0])
  for arr in range(len(data)):
    for i in range(len(data[arr])):
      max_len = max(max_len, len(data[arr][i]))
  
  #Pad data
  for arr in range(len(data)):
    for i in range(len(data[arr])):
      zero_len = max_len - len(data[arr][i])
      if (zero_len != 0):
        zeroString = ''.join(['0']*zero_len)
        data[arr][i] = zeroString + data[arr][i]
  return data

#Interleave an n-dimension vector of binary strings
def interleave(strings):
  acc = ''
  str_len = len(strings[0])
  for i in range(str_len):
    for j in range(len(strings)):
      acc = acc + strings[j][i] 
  return acc

def interleave_data(data):
  interleaved_data = []
  for arr in range(len(data)):
    interleaved_data.append(interleave(data[arr]))
  return interleaved_data

def convert_to_decimal(data):
  decimal_data = []
  dec_max = int(''.join(['1']*len(data[0])), 2)
  for i in range(len(data)):
    decimal_data.append(int(data[i], 2))
  #return normalized form of decimal_data (between 0 and 1)
  return [dec/dec_max for dec in decimal_data], dec_max

def coord_to_num(data, cap):
  binary_data = convert_to_binary(data, cap)
  padded_data = pad_binary(binary_data)
  interleaved_data = interleave_data(padded_data)
  return convert_to_decimal(interleaved_data)