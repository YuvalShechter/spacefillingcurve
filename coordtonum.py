import numpy as np
from decimal import Decimal

pad = "35"
str1 = '{0:0' + pad + 'b}'
newstr = str1.format(6)
#str = '{0:04b}'.format(6)
print(type(newstr))
print(newstr)

def rawr(str1, str2, acc, index1=0, index2=0):
  if ((index1 + index2) == len(str1 + str2)):
    return acc
  return rawr(str2, str1, acc + str1[index1], index2, index1+1)

#print(rawr('00000', '11111', ''))

def exdee(strings):
  acc = ''
  str_len = len(strings[0])
  for i in range(str_len):
    for j in range(len(strings)):
      acc = acc + strings[j][i] 
  return acc

exdee(['00', '11', '22'])

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
  print(max_len)
  
  #Pad data
  for arr in range(len(data)):
    for i in range(len(data[arr])):
      zero_len = max_len - len(data[arr][i])
      if (zero_len != 0):
        zeroString = ''.join(['0']*zero_len)
        data[arr][i] = zeroString + data[arr][i]
  return data