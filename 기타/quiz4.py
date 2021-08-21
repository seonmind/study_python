from random import*
users=range(1,21)
users=list(users)
shuffle(users)
winners=sample(users, 4)
print(f"--당첨자 발표--\n커피 당첨자 : {winners[0]}\n커피 당첨자 : {winners[1:]}\n--축하합니다")