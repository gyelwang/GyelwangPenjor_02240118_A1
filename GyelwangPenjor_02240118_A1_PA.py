def prime_number(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def Sum_of_prime_number():

        first_number = int(input(" Number starting from: "))
        second_number = int(input("Number ending at : "))
        sum = 0
        for i in range(first_number, second_number + 1):
            if prime_number(i):
                sum += i
        print(f"Sum of all prime numbers in the above listed range [{first_number} - {second_number}] are: ", sum)
    

def unit_converter():
    
        print("1. Meter")
        print("2. Feet")
        player = int(input("Enter 1 for meter to feet or 2 for feet to meter: "))
        num = float(input("Enter a value: "))
        if player== 1:
            meter = num * 3.2804
            print(f'Your unit in feet is: {meter}')
        elif player == 2:
            feet = num * 0.3048
            print(f'Your unit in meter is: {feet}')
        else:
            print("Invalid choice. Please enter 1 or 2.")
  

def consonant_counter():
    word = input("Enter a word: ")
    count = 0
    vowels = "AEIOUaeiou"
    for char in word:
        if char.isalpha() and char not in vowels:
            count += 1
    print("Number of consonants: ", count)




list_number= []
def minimum_maximum():
        list_number.clear()
        player_input = int(input("How many numbers are there in total: "))
        for i in range(player_input):
            num = int(input(f" value {i + 1}: "))
            list_number.append(num)

        print("Numbers: ", list_number)
        print("Minimum Value: ", min(list_number))
        print("Maximum Value: ", max(list_number))
       

def palindrome_checker():
    player = input("Enter a Word: ")
    player1 = player[::-1]
    if player == player1:
        print(f'{player1} is a Palindrome')
    else:
        print(f"{player} is not a Palindrome")

def word_counter():
    word_list = ["the","was","and"]
    count = {"the":0,"and":0,"was":0}
    file=input("Enter file name: ")
    with open(file, 'r') as f:
        file1=f.read()
        file1=file1.lower()
        words=file1.split()

        for word in words:
            if word=="the":
                count["the"]+=1
            elif word=="and":
                count["and"]+=1
            elif word=="was":
                count["was"]+=1
      
    print(f"word count for 'the' is:{count['the']}")
    print(f"word count for 'was' is:{count['was']}")
    print(f"word count for 'and' is:{count['and']}")


while True:
    print("Menu: ")
    print("1. Prime number sum calculator ")
    print("2. Convert length between meters and feet")
    print("3. Count consonants in a string")
    print("4. Min and Max number finder")
    print("5. Palindrome checker")
    print("6. Word Counter")
    print("7. Exit")

    player_input = int(input("Please pick one function : "))
    if player_input == 1:
        Sum_of_prime_number()
    elif player_input == 2:
        unit_converter()
    elif player_input == 3:
        consonant_counter()
    elif player_input == 4:
        minimum_maximum()
    elif player_input == 5:
        palindrome_checker()
    elif player_input == 6:
        word_counter()
    elif player_input == 7:
         print("Program Exited!")
         break
    else:
        print("Invalid choice")
    player_input = input("Do you want to continue? (yes/no): ")
    if player_input.lower() != 'y':
        print("Program Exited!")
        break

   