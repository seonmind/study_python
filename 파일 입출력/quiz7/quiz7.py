for i in range(1,51):
    with open(f'{i}주차.txt','w',encoding='utf8') as weekly_file:
        print(f'- {i}주차 주간보고 -\n부서 :\n이름 :\n업무 요약 :', file=weekly_file)
    