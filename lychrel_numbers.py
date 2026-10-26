def is_palindrome(num):
    s = str(num)
    if s[::-1] == s:
        return True
    return False
    
def is_lychrel(num):
    i = 0
    while i < 51:
        i += 1
        num = num + int(str(num)[::-1])
        if is_palindrome(num):
            return False
    return True
        
        
count = 0
for n in range(1, 10000):
    if is_lychrel(n):
        count += 1
        
print(count)
