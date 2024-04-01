"""
You are given an array of strings words and a string chars.
A string is good if it can be formed by characters from chars (each character can only be used once).
Return the sum of lengths of all good strings in words.
"""

class Solution(object):
    def countCharacters(self, words, chars):
        result = 0
        d={chr(i+96):0 for i in range(1,27)}
        for i in chars:
            d[i]+=1
        for i in words:
            for j in i:
                if  d[j]< i.count(j):
                    break
            else:
                result+=len(i)
        return result
    
#Example of Usage!
solution = Solution()
words = ["cat","bt","hat","tree"]
chars = "atach"
print(solution.countCharacters(words, chars))

"""
Time Complexity - O(n^2)
Space Complexity - O(1)
"""        