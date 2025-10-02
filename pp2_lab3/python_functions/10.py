def unique(nums):
    uni=[]
    for i in nums:
        if i not in uni:
            uni.append(i)
    return uni
numbers = [1, 2, 2, 3, 4, 4, 5, 1, 6]
result=unique(numbers)
print (result)