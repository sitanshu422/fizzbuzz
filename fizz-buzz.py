for i in range(1,5100):
    if(i%3==0 and i%5==0):
        print(str(i)+"=fizzbuzz")
    else:
        if(i%5==0):
            print(str(i)+"=buzz")
        else:
            if(i%3==0):
                print(str(i)+"=fizz")
            else:
                print(i)