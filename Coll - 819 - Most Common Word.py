"""
Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. 
It is guaranteed there is at least one word that is not banned, and that the answer is unique.

The words in paragraph are case-insensitive and the answer should be returned in lowercase.
"""

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        for i in ".,?!:;":  #Here i act as a symbol, so loop symbol by symbol
            paragraph = paragraph.replace(i, " ")  #Here we just replace all signs by "space"
        paragraph = paragraph.lower().split() #All words will written with lower letters and split parapraph will be split in words.
        check = {} #Dictionary
        for i in paragraph: #Here i already act as words because of previous spliting
            if i not in banned:
                if i in check: 
                    check[i] +=1 #Secondly if word will repeat its value will change by 1
                else:
                    check[i] = 1 #Firstly in epty check from else will be created keys with its values by default with value 1
        ans = "" 
        count = 0
        for i in check: 
            if count<check[i]:
                count = check[i]
                ans = i
        return ans
    
#Usage of Example!
solution = Solution()
paragraph = "Hello, nice to meet you today, because today weather is nice"
banned = "nice"
print(solution.mostCommonWord(paragraph, banned))

"""
Time Complexity - O(n)
Space Complecity - O(1)
"""