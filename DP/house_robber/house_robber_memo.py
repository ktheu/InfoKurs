def dp(i):
    # Base cases
    if i == 0:
        return nums[0]
    if i == 1:
        return max(nums[0], nums[1])
    if i not in memo:
        memo[i] = max(dp(i - 1), dp(i - 2) + nums[i])  # Recurrence relation
    return memo[i]


nums = [2, 7, 9, 3, 1]
memo = {}
print(dp(len(nums) - 1))
