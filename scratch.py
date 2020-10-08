arr = [1,0,2,3,0,4,5,0]

i = 0
while i < len(arr): 
    if arr[i] == 0:
        temp_prev = 0
        for j in range(i+1, len(arr)):
            if j < len(arr):
                temp = arr[j]
                arr[j] = temp_prev
                temp_prev = temp
        i+=1
    i+=1
print(arr)