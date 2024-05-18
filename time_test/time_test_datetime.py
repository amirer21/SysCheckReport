from datetime import datetime

"""
datetime 모듈은 time 모듈과 비슷하지만,
날짜와 시간을 다루는 데 더 풍부한 기능을 제공합니다. 이를 통해 보다 세밀한 시간 단위로 측정할 수 있습니다.
"""

start_time = datetime.now()

# 실행할 코드
sum = 0
for i in range(1000000):
    sum += i

end_time = datetime.now()
elapsed_time = end_time - start_time
print(f"Execution time: {elapsed_time}")
