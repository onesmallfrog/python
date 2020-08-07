def twoSum(nums:list, target):
    '自写'
    # nums = dict(enumerate(nums))
    # for key, value in nums.items():
    #     if (target - value) in nums.values():
    #          for i,j in nums.items():
    #              if (target - value) == j and i!=key:
    #                  return [key,i]
    '答案' \
    '因为字典重复键为覆盖，第二个for循环找到的是字典里面最后一个重复元素的位置(出现多个' \
    '重复元素时会取重复元素的最后一个)'
    hashmap = {}
    for ind, num in enumerate(nums):
        hashmap[num] = ind
    print(hashmap)
    print(dict(enumerate(nums)))
    for i, num in enumerate(nums):
        j = hashmap.get(target - num)
        if j is not None and i != j:
            return [i, j]
list = twoSum([3,2,4,5,5,5,5,4],10)
print(list)
