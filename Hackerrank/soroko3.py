def maximum_cookies(jars):
    include = 0
    exclude = 0

    for i in jars:
        new_exclude = exclude if exclude > include else include

        include = exclude + i
        exclude = new_exclude

        print(include, exclude)

    return (exclude if exclude > include else include)

if __name__ == "__main__":

    jars = [12, 27, 19, 13, 11]
    #jars = [10, 20, 30, 10]
    #jars = [1,2]
    #jars = [1]
    r = maximum_cookies(jars)
    print(r)

