a = input("Enter text or number or alphanumeric IDC I'll tell you the type: ")

try:
    int(a)
    print(f"{a} is an integer")
except:
    for i in a:
        try:
            int(i)
            print(f"{a} is alphaneumeric")
            break
        except:
            continue
    else:
        print(a+" is a string for sure")