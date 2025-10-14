class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap= {}
        for i in range(len(nums)):
            hashmap[nums[i]]=i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i,hashmap[complement]]       
        return [] 

# optimal solution, compared to the brute force method, try the one pass method next time, as it is still optimal but it is more robust
