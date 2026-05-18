nums = [10, 9, 2, 5, 3, 7, 101, 18, 1]

n = len(nums)
dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if nums[j] < nums[i]:
            if dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1

print(max(dp))