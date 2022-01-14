number =  int(input("Введите число: "))


def get_numbers_count(number):
    count = 0
    while number:
        count += 1
        number = number // 10
    return count


def get_automorphic_numbers(max_number):
    for x in range(1, max_number + 1):
        square = x * x
        length_of_x = get_numbers_count(x)

        num_divider = 10 ** length_of_x
        num = square % num_divider

        if num == x:
            yield num


for x in get_automorphic_numbers(number):
    print(x, "*", x, "=", x * x)

# [print(f'{x} * {x} = {x * x}')
#  for x in filter((lambda n: str(n * n).endswith(str(n))),
#                  range(1, int(input("Введите число: ")) + 1))]
