def encoder(string):
    encoded_message = ''
    for i in range(len(string)):
        number = int(string[i])
        number += 3
        number = str(number)
        encoded_message += number
    return encoded_message

if __name__ == '__main__':
    string = ''
    while True:
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit\n')
        menu_selection = int(input('Please enter an option: '))
        if menu_selection == 3:
            break
        elif menu_selection == 1:
            string = input('Please enter your password to encode:')
            string = encoder(string)
            print('Your password has been encoded and stored!')
        elif menu_selection == 2:
            pass
            # string = encoder(string)
            # decoded = decoder(string)
            # print(f'The encoded passcode is {string}, and the original password is {decoded}')

