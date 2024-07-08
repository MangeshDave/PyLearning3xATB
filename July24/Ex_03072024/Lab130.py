class abc:
    def f1(self):
        try:
            a = int(input("Enter a number "))
        except Exception as e:
            print("Enter only integer value")
        else:
            print(a)
        finally:
            print("I will be always executed")


x = abc()
x.f1()
