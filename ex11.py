n = 10 #정수지정. 자유입력은 n = int(input("정수 입력:")) 하면 아무수나 입력가능
fact = 1 #변수 하나 지정
for i in range(1,n+1): #이건 n이 지정되지 않았을떄, n을 지정 해놨다면 지정된 수보다 +1해서 적어놓으면 된다.
    fact = fact * i #팩토리얼 구하는 식
print(n,"!은",fact) #출력