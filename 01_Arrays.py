from numpy.random import randint    
# Q1-- Write a program that generate 20 random numbers and save in an array , after that find the highest and the lowest number 
# and avg of the array
arr = randint(0,100,20)
high = arr[0]
low = arr[0]
sum = 0
print(arr)
print()
for i in arr:
    if i > high: 
        high = i
print("HIGHEST NUMBER : ",high)
for i in arr:
    if i < low:
        low = i
print("LOWEST NUMBER : ",low)
for i in range(len(arr)):
    sum += arr[i]
average = sum/len(arr)
print("AVERAGE OF ARRAY : ",average)

# Q2-- Write a program to fing the second smallest element in an array 
import math
print()
arr2 = randint(0,100,20)
first = math.inf
second = math.inf

for i in range(0, len(arr2)):
  if arr2[i] < first:
    second = first
    first = arr2[i]

  elif (arr2[i] < second and arr2[i] != first):
    second = arr2[i]
print(arr2)
print("SECOND SMALLEST NUMBER IN ARRAY IS : ",second)