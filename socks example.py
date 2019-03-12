'''John works at a clothing store. He has a large pile of socks that he must pair by color for sale. 
Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.
For example, there are n =7 socks with colors ar=[1,1,1,2,3,2,2,1] There is two pairs of color 1 and one pair of color 2 so number of pairs 
of socks is 3. So result is number of pairs of socks is 3'''

###############CODE#################
###########using collections########

l=[1,1,1,2,3,2,2,1,3,3,3,1,1]
l1=[]
from collections import Counter
cnt=Counter(l)
l1 = [i for i in cnt.values() if i%2==0]
print("total number of pairs is ",sum(l1)/2)

###########without using collections########\
l=[1,1,1,2,3,2,2,1,3,3,3,1,1]
l1=[]
dic={}
for i in l:
    dic[i]=dic.get(i,0)+1
print(dic)
l1=[i for i in dic.values() if i%2==0] 
print("total number of pairs is ",sum(l1)/2)


