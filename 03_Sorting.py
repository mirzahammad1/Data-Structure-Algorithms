import numpy as np
def bubbleSort(arr):
    count = 0 
    for i in range (len(arr)-1):
        for j in range (len(arr)-i-1):
            if arr[j] > arr[j+1]:
                count += 1
                arr[j],arr[j+1] = arr[j+1],arr[j]
    print(count)
                
def selection_sorting(arr):
    count=0
    for i in range(len(arr)-1):
        index=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[index]:
                index=j
        temp=arr[i]
        arr[i]=arr[index]
        arr[index]=temp
        count+=1
    print(count)

def InsertionSort(arr):
    count =0 
    for i in range(1,len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1],j = arr[j],j-1
        arr[j+1] = key
        count += 1
    print(count)

def Q4(number):
    odd = []
    even = []
    for i in range (len(number)):
        if number[i] % 2 == 0:
            even.append(number[i])
            for i in range (len(even)-1):
                for j in range (len(even)-i-1):
                    if even[j] > even[j+1]:
                        even[j],even[j+1] = even[j+1],even[j]
        else:
            odd.append(number[i])
            for i in range (len(odd)-1):
                for j in range (len(odd)-i-1):
                    if odd[j] > odd[j+1]:
                        odd[j],odd[j+1] = odd[j+1],odd[j]

    print(even)
    print(odd)

    for i in odd:
        even.append(i)
    print(even)
        

if __name__ == "__main__":
    arr = np.array([4,3,9,3,1])
    number = np.array([2,5,1,0,4,7,9,3,-2,10,20,15])
    bubbleSort(arr)
    print(arr)
    selection_sorting(arr)
    print(arr)
    InsertionSort(arr)
    print(arr)
    Q4(number)
    