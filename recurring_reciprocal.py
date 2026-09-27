def find_recursing_cycle(num: int, denom: int) -> str:
    sol=""
    rmd_ls=[]

    while num%denom == num:
        num = num*10
        if num%denom > 0:
            quo = num//denom
            if num%denom in rmd_ls :
                break
            rmd_ls.append(num%denom)
            sol = sol + str(quo)
            num = num - denom * quo

    return sol

tmp = 0
sol_fin = 0
for i in range(1,1000):
    sol_str = find_recursing_cycle(1, i)
    if tmp < len(sol_str):
        tmp = len(sol_str)
        sol_fin = i

#this one took forever holy. it takes a lot to undestand but now ive got it down, wow.
