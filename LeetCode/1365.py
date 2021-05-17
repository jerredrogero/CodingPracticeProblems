"""
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.
"""


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums, reverse=True)
        smaller_count = {}
        for i in range(len(sorted_nums)-1):
            curr_num = sorted_nums[i]
            next_num = sorted_nums[i+1]
            if next_num < curr_num:
                remaining_values = len(sorted_nums)-(i+1)
                smaller_count[curr_num] = remaining_values

        smaller_count[sorted_nums[-1]] = 0

        output = []
        for num in nums:
            output.append(smaller_count[num])

        return output
