def std_weight(height, gender):
    if gender=='남자':
        return (height*height)*22
    else:
        return (height*height)*21
height=float(input("키를 입력하시오: "))
gender=input("성별을 입력하시오: ") 
print(f"키 {round(height*100)}cm {gender}의 표준 체중은 {round(std_weight(height, gender),2)}kg 입니다.")


