class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        freq = {}
        elements = []

        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        for n, f in freq.items():
            heapq.heappush(heap, (-f, n))
        
        while heap and k > 0:
            v = heapq.heappop(heap)[1]
            elements.append(v)
            k -= 1
        
        return elements
        
        