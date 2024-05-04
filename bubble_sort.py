nums=[3,4,1,2,5]
for i in range(len(nums)):
    for j in range(0,len(nums)-1):
        if nums[j]>nums[i]:
            nums[i],nums[j]=nums[j],nums[i]
print(nums)
            