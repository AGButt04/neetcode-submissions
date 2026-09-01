class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        
        for st in strs:
            string += str(len(st))
            string += "#"

            for ch in st:
                string += ch
        
        return string

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0

        while i < len(s):
            length = ""
            j = i

            while s[j] != '#':
                length += s[j]
                j += 1
            
            length = int(length)
            word = s[j + 1 : j + length + 1]
            strs.append(word)
            i = j + length + 1
        
        return strs






        return strs
    

