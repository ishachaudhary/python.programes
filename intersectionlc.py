class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
       
            d1,d2 = Counter(nums1), Counter(nums2)
            out = []
            for i in d1.keys():
                if i in d2.keys():
                    out.append(i)
            return out  