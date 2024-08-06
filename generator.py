def items():
    names = ['いちご', 'りんご', 'もも']
    for i in names:
        yield "□" + i


for x in items():
    print(x)


# def primenumber():

#     yield 2 + 1
#     yield '□'
#     yield 5
#     yield 7


# for i in primenumber():
#     print(i)
