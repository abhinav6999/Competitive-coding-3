n = int(input())
arr = map(int, input().split())
my_arr=list(arr)
my_arr.sort()
l1=my_arr
l1.reverse()
l2=l1
print(l2)
for i in range(n):
    if(l2[i]>l2[i+1]):
        print(l2[i+1])
        break