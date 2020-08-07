def reverse(x: int) -> int:
    new =str(x).replace('-','')[::-1]
    if int(new)>=2**31:
        return 0
    if -2**31<int(new) <0:
        return (-int(new))
    if 0<=int(new)<2**31:
        return int(new)



result = reverse(1563847412)
print(result)
