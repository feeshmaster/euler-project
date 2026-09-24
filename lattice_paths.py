gridsz = 20

def progress(x, y):
    i = 0;
    if i % 100 == 0:
        print(i)
    if y < gridsz:
        i += progress(x, y+1)
    if x < gridsz:
        i += progress(x+1, y)
    if x == gridsz and y == gridsz:
        return 1
    return i
print(progress(0, 0))