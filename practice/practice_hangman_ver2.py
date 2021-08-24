from random import*
words=["korea","america","space"]
word=choice(words)
letters=""
while True:
    status= True
    for w in word:
        if w in letters:
            print(w, end=" ")
        else:
            print("_", end=" ")
            status=False
    if status==True:
        print("\nSucced")
        break
    print()
    letter=input("Guess letter: ")
    if letter not in letters:
        letters+=letter
    if letter in word:
        print("Correct")
        print()
    else:
        print("Wrong")
        print()
