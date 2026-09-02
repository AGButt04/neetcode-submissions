class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        visited = set()
        max_seq = 0

        for n in nums:
            visited.add(n)

        for n in visited:
            if n - 1 not in visited:
                curr_seq = 1

                while n + 1 in visited:
                    curr_seq += 1
                    n += 1
            
                max_seq = max(curr_seq, max_seq)
        
        return max_seq