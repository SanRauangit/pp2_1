def spy_game(nums):
    for i in range(len(nums)-1):
        if nums[i]==0 and nums[i+1]==0 and nums[i+2]==7:
            return True
    return False

print(spy_game([1,3,0,1,4]))
print(spy_game([1,0,9,3,0,0,7,2]))