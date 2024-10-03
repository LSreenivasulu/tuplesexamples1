***
Write a program to get the tuple values in a single line separated by space and count the nuber of times the given x value is present in the given tuple.
Sample Input:
1 2 3 1 2 3 4 1 2 1
1
Sample Output:
4
***
a=map(int,input().split())
b=list(a)
n=int(input())
t=0
z=len(b)
for i in range(0,z):
    if(n==b[i]):
        t=t+1
print(t)
