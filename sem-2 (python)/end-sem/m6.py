from mypackage.list1 import append1, extend1, pop1, remove1
from mypackage.set2 import slen2, adds2, remove2
from mypackage.dict3 import len3, add3, keys3, values3

if __name__ == '__main__':
    l = []
    append1(l, 10)
    extend1(l, [20,30])
    print(l, pop1(l))

    s = {1}
    print(slen2(s))
    adds2(s,2)
    print(s)

    d = {}
    add3(d,'x',100)
    print(len3(d), list(keys3(d)), list(values3(d)))