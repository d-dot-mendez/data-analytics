doubler = lambda n: n * 2

print(doubler(8))
print(doubler(-4))
print(doubler('banana'))

#tripler lambda
tripler = lambda n: n * 3
print(tripler(8))
print(tripler(-4))
print(tripler('banana'))

#multiplier function
def multiplier(num):
    return lambda n:n*num

#variables
times4 = multiplier(4)
times5  = multiplier(5)
times6 = multiplier(6)
times7 = multiplier(7)
times8 = multiplier(8)
times9 = multiplier(9)
times10 = multiplier(10)

#times4
print(times4(8))
print(times4(-4))
print(times4('banana'))

#times5
print(times5(8))
print(times5(-4))
print(times5('banana'))

#times6
print(times6(8))
print(times6(-4))
print(times6('banana'))

#times7
print(times7(8))
print(times7(-4))
print(times7('banana'))

#times8
print(times8(8))
print(times8(-4))
print(times8('banana'))

#times9
print(times9(8))
print(times9(-4))
print(times9('banana'))

#times10
print(times10(8))
print(times10(-4))
print(times10('banana'))