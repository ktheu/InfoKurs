
def rob(nums):
    if len(nums) == 1:
        return nums[0]

    dp = [0] * len(nums)

    # Base cases
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])  # Recurrence relation

    return dp[-1]


nums = [2, 7, 9, 3, 1]
memo = {}
print(rob(nums))
