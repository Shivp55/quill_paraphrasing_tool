for i in range(1,8):
    try:
        if(i!= 3):
            print(i,end="\n")
        else:
            i=i/0
    except:
        print("error")
        continue

    print("hiiii")