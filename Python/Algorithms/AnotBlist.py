'''
    Problem: get list C, that contains the items from A that are not in list B
'''

A = [2, 4, 8, 16, 32, 64, 128]
B = [1, 2, 3, 5, 8, 13, 21, 34]
C = [] #solution list
print('A= ', A)
print('B= ', B)

#   We will use two pointers in the list to compare, i and j
i = j = 0
a = len(A) 
b = len(B) 

while i < a and j < b:
    if A[i] == B[j]:
        i += 1
        j += 1
    elif A[i] < B[j]:
        C.append(A[i])
        i += 1
    else:
        j += 1
# When B is done but A is not completed yet, so we add all A elements to the solution list
if i < len(A):
    for k in range(i, len(A)):
        C.append(A[k])    

print('The solution is: ',C)