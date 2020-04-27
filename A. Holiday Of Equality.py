n = int(input())
nums = list(map(int,input().split()))

nums.sort()
total = 0
for i in nums:
	total += nums[len(nums)-1] - i
print(total)
