
while True:
    text = input("Enter your text: ")

    try:
        a = text[2]
        b = text[-2]
        c = text[:5]
        d = text[:-2]
        e = text[2::2]
        f = text[1::2]
        g = text[::-1]
        h = text[-1::-2]
        i = text[-2:0:-1]
        j = len(text)
    except IndexError:
        print("This word is too short!")
    else:
        print(a, b, c, d, e, f, g, h, i, j, sep='\n')
        break



