
nums = [2,8,11,15,1]
target = 9

for x in range(0, len(nums)-1):
	for y in range(x+1, len(nums)):
		if( nums[x] + nums[y] == target):
			ans = [x,y]

print ans