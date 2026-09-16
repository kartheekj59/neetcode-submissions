class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        globalMaxPrefix = ""

        template = strs[0]; n = len(strs)

        for index,letter in enumerate(template):

            i = 1

            while i < n:

                if len(strs[i])-1 < index or letter != strs[i][index]:
                    return globalMaxPrefix
                i+=1
            
            globalMaxPrefix+=letter
        return globalMaxPrefix
                


            
        