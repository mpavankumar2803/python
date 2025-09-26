print("hello world")

'''
/////// program to print sum of squares of n numbers //////////
n=int(input("n="))
num=0;

for i in range(1,n+1,1):
    num=num+(i*i)
print("sum of squares is:",num)

////////// pattern printing  /////////////

#box star pattern
for i in range(1,5):
    for j in range(1,5):
        print("*",end=" ")
    print()


for i in range(4,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()

for i in range(4,0,-1):
    for j in range(4,0,-1):
        print(j,end=" ")
    print()

for i in range(1,6,1):
    for j in range(i):
        print(i,end=" ")
    print()

# took some time to solve this pattern
for i in range(1,5,1):
    for j in range(i):
        print(j+1,end=" ")
    print()

for i in range(5,0,-1):
    for j in range(i):
        print(j+1,end=" ")
    print()


#pattern to print:
----1
---12
--123
-1234
12345
for i in range(1,6,1):
    for j in range(5,i,-1):
        print("-",end=" ")
    for k in range(i):
        print(k+1,end=" ")
    print()


# squre box pattern
-----
|   |
|   |
|   |
-----
for i in range(1,6,1):
    for j in range(1,6,1):
        if(i==1 or i==5):
            print("-",end=" ")
        elif(j==1 or j==5):
                print("|",end=" ")
        else:
            print(" ",end=" ")
    print()


/////////////////////  bubble sorr  ///////////////////////
#below pattern will be followed for buble sort
# for i in range(5,0,-1):
#         for j in range(i):
#               print(i,end=" ")
#         print()


def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if(nums[j]>nums[j+1]):
                temp=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp


nums=[5,3,8,6,7,2]
sort(nums)

print(nums)


/////////////  linear search algorithm  /////////////
#funtion find takes nums list and n value as input and returns the n value index as output

def find(nums,n):
    for i in range(0,len(nums),1):
        if(nums[i]==n):
            print(f"element found at index {i}")
            break
    else:
        print("not found")



nums=[5,3,8,6,7,2]
n=7
find(nums,n) 

////////////// Binary search using while loop ////////////

pos=-1;
def find(list,n):
    l=0
    u=len(list)-1;
    while(l<=u):
        mid=(l+u)//2
        if list[mid]==n:
            globals()["pos"]=mid
            return True
        else:
            if(list[mid]<n):
                l=mid;
            else:
                u=mid;


list=[4,7,8,12,45,99]
n=45

if find(list,n):
    print("found at position : ",pos+1)
else:
    print("not found")




#binary search using for loop
pos=0;
def find(list,n):
    l=0
    u=len(list)-1
    for i in range(len(list)):
        m=(l+u)//2
        if(list[m]==n):
            globals()['pos']=m
            return m
        else:
            if(n<list[m]):
                u=m
            else:
                l=m

list = [4, 7, 8, 12,32,33,39, 45, 99]

if(find(list,33)):
    print("found at index",pos)
'''

# # given an number n of each integer i in range from 1 to n inclusive print one value per line as follows:
# * if i is a multiple of both 3 and 5 print fizzBuzz.
# * if i is a multiple of  3 (but not 5) print fizz.
# * if i is a multiple of  5 (but not 3) print Buzz.
# * if i is a multiple of 3 or 5 print the value of i.

def fizzBuzz(n):
    for i in range(1,n+1):
        if(i%3==0 and i%5==0):
            print("FizzBuzz")
        elif(i%3==0 and i%5!=0):
            print("Fizz")
        elif(i%5==0 and i%3!=3):
            print("Buzz")
        else:
            print(i)

print(fizzBuzz(15))