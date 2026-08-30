class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        frequencies = {}
        groupedAnagrams = []

        for str in strs:
            freq = [0] * 26
            
            for char in str:
                idx = ord(char) - ord('a')
                freq[idx] += 1
            
            freq = tuple(freq)
            if freq in frequencies.keys():
                frequencies[freq].append(str)
            else:
                frequencies[freq] = [str]
        
        for anas in frequencies.values():
            groupedAnagrams.append(anas)
        
        return groupedAnagrams

        
        