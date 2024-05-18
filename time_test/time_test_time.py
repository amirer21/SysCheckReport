import time

"""
time 모듈은 프로그램의 시작과 종료 시점에 시간을 기록함으로써 실행 시간을 측정할 수 있게 해줍니다.
이 방법은 매우 직관적이며 간단한 시간 측정에 적합합니다.
"""
start_time = time.time()  # 시작 시간 기록

# 실행할 코드
sum = 0
for i in range(1000000):
    sum += i

end_time = time.time()  # 종료 시간 기록
elapsed_time = end_time - start_time  # 경과 시간 계산
print(f"Execution time: {elapsed_time} seconds")
