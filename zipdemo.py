def demo():
    names = ("first", "second", "third")
    files = ("demo", "test", "main")

    zipped1 = zip(names, files)
    for (a,b) in zipped1:
        print(a,b)

    zipped2 = list(zip(names,files))
    print(zipped2)

    zipped3 = dict(zip(names,files))
    print(zipped3)


demo()
