import timeit

"""
timeit 모듈은 주어진 코드를 여러 번 실행하여 코드의 평균 실행 시간을 측정합니다. 
이 방법은 반복 실행을 통해 더 정확한 측정 결과를 제공하며,
일반적으로 짧은 코드 조각의 성능 테스트에 사용됩니다.
"""

# 실행할 코드
code_to_test = """
sum = 0
for i in range(100000):
    sum += i
"""

# code_to_test를 100번 실행하고 평균 시간을 출력
execution_time = timeit.timeit(stmt=code_to_test, number=100) / 100
print(f"Average execution time: {execution_time} seconds")
