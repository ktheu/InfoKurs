from functools import lru_cache

# If we cannot schedule at least one job per day,
# it is impossible to create a schedule


@lru_cache(None)
def dp(i, day):
    # Base case, it's the last day so we need to finish all the jobs
    if day == d:
        return hardest_job_remaining[i]

    best = float("inf")
    hardest = 0
    # Iterate through the options and choose the best
    for j in range(i, n - (d - day)):  # Leave at least 1 job per remaining day
        hardest = max(hardest, jobDifficulty[j])
        best = min(best, hardest + dp(j + 1, day + 1))  # Recurrence relation

    return best


# jobDifficulty = [6, 5, 4, 3, 2, 1]
# d = 2
# jobDifficulty = [1, 15, 10, 3, 2, 1]
# d = 3
# jobDifficulty = [7, 1, 7, 1, 7, 1]
# d = 3
# jobDifficulty = [11, 111, 22, 222, 33, 333, 44, 444]
# d = 6
jobDifficulty = [6, 5, 10, 3, 2, 1]
d = 3
n = len(jobDifficulty)
if n < d:
    print('unmöglich')

hardest_job_remaining = [0] * n
hardest_job = 0
for i in range(n - 1, -1, -1):
    hardest_job = max(hardest_job, jobDifficulty[i])
    hardest_job_remaining[i] = hardest_job

print(dp(0, 1))
