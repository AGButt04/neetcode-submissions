class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        frequencies = defaultdict(list)
        groupedAnagrams = []

        for str in strs:
            freq = [0] * 26
            
            for char in str:
                idx = ord(char) - ord('a')
                freq[idx] += 1
            
            freq = tuple(freq)
            frequencies[freq].append(str)
        
        return list(frequencies.values())

        
        