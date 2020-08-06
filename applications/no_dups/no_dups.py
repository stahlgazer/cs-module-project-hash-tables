def no_dups(s):
    # Your code here
    # turn string into array, use sorted set
    splitted = s.split(' ')
    # print(splitted)
    no_dupes = ' '.join(sorted(set(splitted), key=splitted.index))
    # print(no_dupes)
    return no_dupes


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))