from random import*
words=["apple","banana","watermelon","strawberry"]
word=choice(words)
wordlength=len(word)
guessword=[]
# 추측들을 집어넣는 리스트
for i in range(0,wordlength):
    guessword.append("_")

while True:
    mes=""
    for i in range(0,wordlength):
        mes+=guessword[i]    
    guessletter=input(f"{mes}: ") #글자 1개를 받음
    for i in range(0,wordlength):
        if guessletter==word[i] and guessword[i]=="_":
            guessword[i]=guessletter
            break
    if "_" not in guessword:
        print("success")
        break





