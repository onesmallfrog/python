def test(s:str):
    '自写，我写一堆，人家写一行，还没看懂，我可真是太棒了'
    # nums = 0
    # nums += s.count('IV')*4
    # s =s.replace('IV','')
    # nums += s.count('IX') * 9
    # s = s.replace('IX','')
    # nums += s.count('XL') * 40
    # s = s.replace('XL','')
    # nums += s.count('XC') * 90
    # s = s.replace('XC','')
    # nums += s.count('CD') * 400
    # s = s.replace('CD','')
    # nums += s.count('CM') * 900
    # s = s.replace('CM','')
    # for item in s:
    #     if item =='I':    #         nums +=1
    #     if item == 'V':
    #         nums +=5
    #     if item == 'X':
    #         nums += 10
    #     if item == 'L':
    #         nums +=50
    #     if item == 'C':
    #         nums += 100
    #     if item == 'D':
    #         nums +=500
    #     if item == 'M':
    #         nums +=1000
    # return nums
    '''
    答案 
    构建一个字典记录所有罗马数字子串，注
    意长度为2的子串记录的值是（实际值 - 
    子串内左边罗马数字代表的数值）

    这样一来，遍历整个 ss 的时候判断当前位置
    和前一个位置的两个字符组成的字符串是否在字典内，如
    果在就记录值，不在就说明当前位置不存在小数字在前面的情况，直接记录当前位置字符对应值

    举个例子，遍历经过 IVIV 的时候先记录 II 的
    对应值 11 再往前移动一步记录 IVIV 的值 33，
    加起来正好是 IVIV 的真实值 44。max 函数在这里
    是为了防止遍历第一个字符的时候出现 [-1:0][−1:0] 的情况
    '''
    d = {'I': 1, 'IV': 3, 'V': 5, 'IX': 8, 'X': 10, 'XL': 30, 'L': 50, 'XC': 80, 'C': 100, 'CD': 300, 'D': 500,
         'CM': 800, 'M': 1000}
    return sum(d.get(s[max(i - 1, 0):i + 1], d[n]) for i, n in enumerate(s))
result = test("MCMXCIV")
print(result)