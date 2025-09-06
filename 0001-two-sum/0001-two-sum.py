class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        for i in range(len(nums)): # 2, 5, 5, 11
            i_val = nums[i]
            for j in range(1, len(nums)): # 5, 5, 11
                j_val = nums[j]
                if i == j:
                    break # 숫자가 같을 경우 예외처리
                if i_val + j_val == target:
                    output.append(i)
                    output.append(j)
                    return output
                    