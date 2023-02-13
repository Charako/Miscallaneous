narcissistic_numbers = []
def isNarcissistic():
    for i in range(1,1000000):
        length = len(str(i))
        digits = [int(x)**int(length) for x in str(i)]
        total = sum(digits)
        if total == i:
            print(i)
            narcissistic_numbers.append(i)
    return narcissistic_numbers
isNarcissistic()