class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        for i in nums1:
            if i not in dic.keys(): dic[i] = 1
        
        for i in nums2:
            if i in dic.keys(): dic[i] +=1
        
        res = []
        for i in dic.items():
            if i[1] > 1: res.append(i[0])
                
        return res