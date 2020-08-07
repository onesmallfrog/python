def test(x:int):
    new = str(x)[::-1]
    if new == str(x):
        return True
    else:
        return False
result = test(-454)
print(result)
