from mastermind_engine import *
from mastermind_engine import _magic_number

def main():
    global _magic_number
    print('New game started: ',end='\n\n')
    while True:
        try:
            num = int(input('Input int number: '))
        except ValueError:
            print('Invalid number')
            continue
        if num < 1000 or num > 10000 or len(set(str(num))) < 4:
            print('Enter number in range from 1000 to 9999 where every number unique')
            continue
        check_dict = check_number(num)
        if check_dict['bulls'] == 4:
            print(f'You\'ve got it, the number was {num}.')
            input_str = input('Do you want to play another game ? (yes/no) ')
            if input_str == 'yes' or input_str == 'y':
                make_number()
                print('New game started: ',end='\n\n')
                continue
            elif input_str == 'no' or input_str == 'n':
                print('Bye bye')
                return
        print(f'Bulls = {check_dict["bulls"]} ; Cows = {check_dict["cows"]}')




if __name__ == "__main__":
    # print(_magic_number)
    main()
