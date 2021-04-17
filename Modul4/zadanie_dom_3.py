def biggest_div(a, b):
    if a == b:
        return a
    if a > b:
        a -= b
    else:
        b -= a
    return biggest_div(a, b)


if __name__ == '__main__':
    print(biggest_div(12, 18))
