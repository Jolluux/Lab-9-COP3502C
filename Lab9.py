def encoder(string):
    encoded_message = ''
    for i in range(len(string)):
        number = int(string[i])
        number += 3
        number = str(number)
        encoded_message += number
    return encoded_message

print(encoder('1234566'))
