class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + '#' + s
        
        return res
        
        
        
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res   

        
        '''
        
        for i in range(len(strs)):
            strs[i] = len(strs[i]) + '#' + str[i] + "##"

        return "".join(strs)
    def decode(self, s: str) -> List[str]:
        is_valid = True
        
        for i in range(len(s)):
            num = 0

            if is_valid:
                num = s[i]
'''

