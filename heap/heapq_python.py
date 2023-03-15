#%%
# note: use with tuples with first element being the priority 
import heapq
mylist = [1,8,9,7,5,-2,0]
heapq.heapify(mylist) # creates a min heap
print(mylist) # [-2, 5, 0, 7, 8, 9, 1], smallest on the left 
heapq.heappop(mylist) # -2
print(mylist) # [0, 5, 1, 7, 8, 9]
heapq.heappush(mylist, 1)
print(mylist) # [0, 5, 1, 7, 8, 9, 1]

heapq.nlargest(4, mylist) # [9, 8, 7, 5]
heapq.nsmallest(4, mylist) # [0, 1, 1, 5]

# heappushpop = push then pop (more efficient)
# heapreplace = pop then push more efficient

#%%
def strStr( haystack: str, needle: str) -> int:    
    
    j = 0
    while j <= len(haystack)-1:
        while haystack[j] != needle[0]:
            j = j + 1
            if j == len(haystack):
                return -1

        begin = j
        while haystack[j] == needle[j - begin]:
            if j - begin == len(needle) - 1:
                return begin
            j = j + 1

    return -1

print(strStr( "mississippi", "issip")) 

