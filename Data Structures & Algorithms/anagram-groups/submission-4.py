class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        groupedAnagrams = []

        for str in strs:
            ana = ''.join(sorted(str))

            if ana in anagrams:
                anagrams[ana].append(str)
            else:
                anagrams[ana] = [str]
        
        for groupings in anagrams.values():
            groupedAnagrams.append(groupings)
        
        return groupedAnagrams

        
        