def main(a,b,c):
    if a>b:
        if a>c:
            return a
        return c
    else:
        if b>c:
            return b
        return c
print(main(6,12,2))
