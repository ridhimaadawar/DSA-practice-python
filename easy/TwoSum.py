class Solution:
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]  
        return [] 

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    result = Solution().twoSum(nums, target)
    print(result)

