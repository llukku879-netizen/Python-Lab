def modifyvalue(a)
    print(:value recieved in function:",a)
    a=10
    print("value inside function after change:",a)
    a=5
    modifyvalue(a)
    print("value outside function:",a)      
