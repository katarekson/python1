def hello(**kwargs):
    print("Hello",end=" ")
    for key,value in kwargs.items():
        print(value,end=" ")
    
hello(title="Mr.",first="mirek", middle="wlodzimierz", last="klaus")