import numpy as np

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