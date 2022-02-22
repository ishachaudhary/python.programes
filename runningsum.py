class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        p =[]
        q=0
        for x in nums:
            q += x
            p.append(q)
        return 