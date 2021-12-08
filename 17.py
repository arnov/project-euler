nums = ["", "one", "two", "three", "four",  "five",
        "six", "seven", "eight", "nine"]
teens = ["", "eleven", "twelve", "thirteen",  "fourteen",
         "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "ten", "twenty", "thirty", "forty",
        "fifty", "sixty", "seventy", "eighty", "ninety"]


def convert(n):
    assert n <= 1000

    if n < 10:
        return nums[n]
    elif n == 10:
        return 'ten'
    elif n < 20:
        return teens[n % 10]
    elif n < 100:
        return tens[int(n/10)] + convert(n % 10)
    elif n < 1000:
        if convert(n % 100):
            connector = 'hundredand'
        else:
            connector = 'hundred'
        return nums[int(n/100)] + connector + convert(n % 100)

    return 'onethousand'


print(sum(len(convert(n)) for n in range(1, 1001)))
