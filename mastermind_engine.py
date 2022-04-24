from random import randint

_magic_number = None

def randpop(max_num=4):
    list_of_nums = list(range(0,10))
    while True:
        list_len = len(list_of_nums)
        if list_len == 10:
            yield list_of_nums.pop(randint(1,list_len-1))
            list_len = len(list_of_nums)
        if not list_len or 10-list_len == max_num:
            return
        yield list_of_nums.pop(randint(0,list_len-1))

def make_number():
    global _magic_number
    _magic_number = list(randpop())

def check_number(nums):
    global _magic_number
    nums = list(str(nums))
    cows_bulls = {'cows': 0, 'bulls': 0}
    for i, number in enumerate(nums):
        if int(number) in _magic_number and int(nums[i]) == _magic_number[i]:
            cows_bulls['bulls'] += 1
        elif int(number) in _magic_number:
            cows_bulls['cows'] += 1
    return cows_bulls

make_number()
