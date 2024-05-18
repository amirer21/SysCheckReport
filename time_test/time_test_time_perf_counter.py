import time

def compute_something():
    # 여기에 측정하고자 하는 코드 작성
    result = 0
    for i in range(1000000):
        result += i
    return result

# 프로그램 실행 전 시간 측정
start_time = time.perf_counter()

# 실행할 코드
result = compute_something()

# 프로그램 실행 후 시간 측정
end_time = time.perf_counter()

# 실행 시간 계산
execution_time = end_time - start_time
print(f"실행 시간: {execution_time} 초")