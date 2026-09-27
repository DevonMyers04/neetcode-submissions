def add_two_numbers() -> int:
    n = input()
    nh = n.split(",")
    sun=0
    for nums in nh:
        sun+=int(nums)
    return sun



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())