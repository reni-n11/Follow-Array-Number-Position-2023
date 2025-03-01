import numpy as np
import random

def is_int_and_is_in_array(num, nums_arr):
  while True:
    num = input()
    try:
      int(num) #проверяваме дали числото е цяло
    except:
      print("Въведете цяло число!")
    try:
      int(num) in nums_arr #проверяваме дали числото се съдържа в масива
      return num
      break
    except:
      print("Това число не е в масива!")

nums_list = []
number = 0

print("Въведете цели числа, разделени със запетая и празно място:")
#съставяме масив от числата, разделени по запетая и празно място и обосноваваме, че типа на данните в масива е int
nums_arr = np.array(input().split(", "), dtype = int)

print("Изберете число:")
number = is_int_and_is_in_array(number, nums_arr) #проверяваме дали числото е цяло и се съдържа в списъка

nums_list = nums_arr.tolist() #записваме масива в списък
print(*nums_list, sep=", ")
print("Първоначална позиция на числото {}: {}".format(number, nums_list.index(int(number)) + 1))

random.shuffle(nums_arr) #разбъркваме масива

shuf_nums_list = nums_arr.tolist() #записваме разбъркания масив в списък
print(*shuf_nums_list, sep=", ")
print("Позиция на числото {} след разбъркване: {}".format(number, shuf_nums_list.index(int(number)) + 1))
