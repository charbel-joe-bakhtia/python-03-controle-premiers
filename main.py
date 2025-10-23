from math import sqrt

#### Fonction secondaire


def isprime(p):
    premier = True
    for i in range(2,p):
        if p%i  == 0 :
            premier = False
    return premier
print("Nombres Premiers ; \n")
print(f"722 est-il un nombre premier ? \n {isprime(722)}")
print(f"17 est-il un nombre premier ? \n {isprime(17)}")
print(f"3 est-il un nombre premier ? \n {isprime(3)}")
print(f"2 est-il un nombre premier ? \n {isprime(2)}")
print(f"15 est-il un nombre premier ? \n {isprime(15)}")


def main():

    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
