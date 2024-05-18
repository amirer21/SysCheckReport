import time

# 코드 실행 전 시간 기록
start_time = time.time()

# 실행할 코드
numbers = [i for i in range(1000000)] # 0부터 999999까지의 숫자를 numbers 리스트에 저장
# ...999988, 999989, 999990, 999991, 999992, 999993, 999994, 999995, 999996, 999997, 999998, 999999]
#print(numbers)  # numbers 리스트 출력

# 코드 실행 후 시간 기록
end_time = time.time()

# 실행 시간 계산
elapsed_time = end_time - start_time
print(f"Execution time: {elapsed_time} seconds")
