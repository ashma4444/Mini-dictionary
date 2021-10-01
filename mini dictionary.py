my_dictionary = {'abandon': "cease to support or look after (someone)",
                'barren' : "(of land) too poor to produce much or any vegetation.",
                'consequence': "a result or effect, typically one that is unwelcome or unpleasant.",
                'detrimental': "tending to cause harm."}



while True:
    word_input = input("Enter the word/ 'E/e to exit': ")
    wordInput = word_input.lower()

    if wordInput in my_dictionary:
        print(my_dictionary[wordInput])
    
    elif wordInput == 'e':
        break

    else:
        print("Meaning not found")