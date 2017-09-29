def reverse(letter):
    reversedletter = ''
    for i in range(len(letter)-1,-1,-1):
        reversedletter += letter[i]
    return reversedletter



word = "Hello world!"
print(word)
print(str(reverse(word)))
