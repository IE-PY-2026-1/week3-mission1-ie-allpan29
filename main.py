# 파일이름 :
# 작 성 자 : 강현민

# 미션 1
name5 = input('이름을 입력하시오: ')
writing5 = int(input('당신의 글쓰기 점수를 입력하시오: '))
python5 = int(input('당신의 파이썬 점수를 입력하시오: '))
last_avg5 = float(input('당신의 지난학기 평균을 입력하시오: '))

average5 = (writing5 + python5) / 2
gap5 = average5 - last_avg5

print(f'{name5} 학생의 글쓰기 점수는 {writing5}, 파이썬 점수는 {python5} 입니다.')
print(f'평균은 {average5} 이고, 지난 학기와 차이는 {gap5} 입니다.')
