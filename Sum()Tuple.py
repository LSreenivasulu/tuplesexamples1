***
Write a program to get tuple elements in a single line separated by spaces and print the sum of the elements without using sum() method.
Sample Input:
10 20 30
Sample Output:
60
***
a=map(int,input().split())
b=tuple(a)
c=sum(b)
print(c)
