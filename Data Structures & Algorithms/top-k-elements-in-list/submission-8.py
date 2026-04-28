class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)
        most_occurences = []
        for num in nums:
            res[num] += 1

        sorted_res = sorted(res.items(), key=lambda x: x[1], reverse=True)
        for i in range(k):
            most_occurences.append(sorted_res[i][0])
        return most_occurences
        