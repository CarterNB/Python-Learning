
nums=[2,6,4,5,7,2,3]

def pivotIndex(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    sum_left = 0
    sum_right = sum(nums)
    for i in range(nums.__len__()):
        sum_right -= nums[i]
        if sum_right == sum_left:
            return i
        sum_left += nums[i]
    return -1

print(pivotIndex(nums))