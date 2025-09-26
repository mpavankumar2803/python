
'''/////////////////////  bubble sorr  ///////////////////////
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

if(find(list,31)):
    print("found at index",pos)
else:
    print("numb not found")

'''
