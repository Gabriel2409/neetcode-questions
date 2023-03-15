# A string s is called happy if it satisfies the following conditions:

#     s only contains the letters 'a', 'b', and 'c'.
#     s does not contain any of "aaa", "bbb", or "ccc" as a substring.
#     s contains at most a occurrences of the letter 'a'.
#     s contains at most b occurrences of the letter 'b'.
#     s contains at most c occurrences of the letter 'c'.

# Given three integers a, b, and c, return the longest possible happy string. 
# If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".

# A substring is a contiguous sequence of characters within a string.
# Example 1:

# Input: a = 1, b = 1, c = 7
# Output: "ccaccbcc"
# Explanation: "ccbccacc" would also be a correct answer.
import heapq
def longest_diverse_string( a: int, b: int, c: int) -> str:
    # arr = []
    
    # for i in range(a):
    #     heapq.heappush(arr,(-1 * (a-i), "a"))
    # for i in range(b):
    #     heapq.heappush(arr,(-1 * (b-i),"b"))
    # for i in range(c):
    #     heapq.heappush(arr,(-1 * (c-i), "c"))

    # cur = 0
    # final = []
    # while arr:
    #     el = heapq.heappop(arr)


    #     if final and final[0] == el[1]:
    #         cur = cur + 1
    #         if cur < 3:
    #             final.append(el[1])
    #         else:
    #             torepop = [el]
    #             while arr:
    #                 el = heapq.heappop(arr)
    #                 if torepop[-1][1] != el[1]:
    #                     final.append(el[1])
    #                     cur = 1
    #                     for ee in torepop:
    #                         heapq.heappush(arr, ee)
    #                     break
    #                 else:
    #                     torepop.append(el)
       
    #     else:
    #         cur = 1
    #         final.append(el[1])
    # return "".join(final)

print(longest_diverse_string(1,1,7))