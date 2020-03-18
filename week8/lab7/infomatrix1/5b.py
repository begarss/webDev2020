def power(a, n):
    return a ** n
nums = list(map(float, input().split()))
print(power(nums[0], nums[1]))