def test(s:str):
    '自写'
    # list = []
    # nums = 0
    # num = 0
    # for item in s:
    #     if item not in list:
    #         list.append(item)
    #         nums = len(list)
    #     else:
    #         if nums > num:
    #             num =nums
    #         nums = 0
    #         list = list[list.index(item)+1:]
    #         list.append(item)
    # if num > nums:
    #     return num
    # else:
    #     return nums
    '答案,性能略差'
    length, j = 0, -1
    for i, x in enumerate(s):
        if x in s[j + 1:i]:
            length = max(length, i - j - 1)
            j = s[j + 1:i].index(x) + j + 1
    return max(length, len(s) - 1 - j)
result = test("abcabcbb")
print(result)