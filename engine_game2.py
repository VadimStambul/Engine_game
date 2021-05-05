import random


print("\n Let`s Game beggin! ")

def guess_number():
    my_number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(my_number)
    return my_number[0:4]

def check_number():
    while True:
        try:
            in_number = [int(x) for x in input("Enter 4-digit number: ")]
            if len(in_number) == 4:
                break
            else:
                print("You entered an invalid value. Four number only! ")
        except ValueError:
            print('Enter only number! Try again, please!')
    print('in_number:', in_number)
    return in_number[0:4]

def count_cow():
    cow = 0
    bull = 0
    list_rand = guess_number()
    # print('my_number', list_rand)
    while True:
        indx_rand = 0
        if bull == 4:
            print("Greetings! You are win!")
            print("      GAME OVER ")
            break

        list_usr = check_number()
        print()
        cow = 0
        bull = 0
        for m_rand in list_rand:
            indx_rand += 1
            indx_usr = 0
            for m_usr in list_usr:
                indx_usr += 1
                if m_rand == m_usr:
                    if indx_rand == indx_usr:
                        bull += 1
                        break
                    else:
                        cow += 1
                        break
        print('cows:', cow)
        print('bulls', bull, '\n')
    print('   Have a good day!')


count_cow()