import datetime
x= datetime.datetime.now()
try:
    print(x)
    print(x.year)
    print(x.strftime("%A"))

    x = datetime.datetime(2020, 5, 17)
except NameError:
    print("You didn't define datetime")
finally:
    print("try/except is finished")

#print(x)
#x = datetime.datetime(2018, 6, 1)

#print(x.strftime("%B"))
