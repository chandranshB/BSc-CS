import list1, set2, dict3

if __name__ == '__main__':
    l = [1,2]
    list1.append1(l, 3)
    list1.extend1(l, [4,5])
    print(l)
    print(list1.pop1(l))

    s = {1,2}
    print(set2.slen2(s))
    set2.adds2(s,3)
    print(s)

    d = {'a':1}
    print(dict3.len3(d))
    dict3.add3(d,'b',2)
    print(list(dict3.keys3(d)), list(dict3.values3(d)))