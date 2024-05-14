import psutil
import platform
import multiprocessing
from tqdm import tqdm
from datetime import datetime
import os
import time

def get_pc_info():
    pc_info = f"<h2>PC 정보</h2>"
    pc_info += "<ul>"
    uname = platform.uname()
    pc_info += f"<li>시스템: {uname.system}</li>"
    pc_info += f"<li>노드 이름: {uname.node}</li>"
    pc_info += f"<li>릴리즈: {uname.release}</li>"
    pc_info += f"<li>버전: {uname.version}</li>"
    pc_info += f"<li>머신: {uname.machine}</li>"
    pc_info += f"<li>프로세서: {uname.processor}</li>"
    pc_info += "</ul>"
    return pc_info

def get_cpu_info():
    cpu_info = "<h2>CPU 정보</h2>"
    cpu_info += "<ul>"
    cpu_info += f"<li>물리적 코어: {psutil.cpu_count(logical=False)}</li>"
    cpu_info += f"<li>논리적 코어: {psutil.cpu_count(logical=True)}</li>"
    cpufreq = psutil.cpu_freq()
    cpu_info += f"<li>최대 주파수: {cpufreq.max:.2f} MHz</li>"
    cpu_info += "</ul>"
    return cpu_info

def get_ram_info():
    ram_info = "<h2>RAM 정보</h2>"
    ram = psutil.virtual_memory()
    ram_info += f"<p>총 램: {ram.total/1024**3:.2f} GB</p>"
    return ram_info

def stress_cpu(iterations):
    start_time = time.time()
    result = 0
    for i in range(iterations):
        result += 1
    end_time = time.time()
    return end_time - start_time

def stress_ram(chunk_size):
    ram_data = b"x" * chunk_size
    ram_data = list(ram_data)
    return ram_data

def test_performance():
    performance_result = "<h2>성능 테스트 결과</h2>"

    # CPU 테스트
    performance_result += "<h3>CPU 테스트</h3>"
    performance_result += "<p>CPU에 과부하를 걸어 테스트합니다.</p>"

    cpus = multiprocessing.cpu_count()
    cpu_times = multiprocessing.Pool(cpus).map(stress_cpu, [10**8]*cpus)
    performance_result += f"<p>CPU 테스트 완료 (총 시간: {sum(cpu_times):.2f}초)</p>"

    # RAM 테스트
    performance_result += "<h3>RAM 테스트</h3>"
    performance_result += "<p>RAM에 과부하를 걸어 테스트합니다.</p>"

    ram_total = psutil.virtual_memory().total
    chunk_size = 10**8  # 100 MB 단위
    chunks = [chunk_size] * (int(ram_total // chunk_size) // 2)
    for chunk in tqdm(chunks, unit="MB"):
        stress_ram(chunk)
    performance_result += "<p>RAM 테스트 완료</p>"

    return performance_result, cpu_times

def analyze_results(pc_info, cpu_info, ram_info, performance_result, cpu_times):
    analysis = "<h2>결과 분석</h2>"
    analysis += "<p>PC 정보와 성능 테스트 결과를 종합해보면...</p>"
    
    # CPU 분석
    analysis += "<h3>CPU 분석</h3>"
    analysis += f"<p>전체 CPU 코어 수: {multiprocessing.cpu_count()}</p>"
    analysis += f"<p>총 테스트 시간: {sum(cpu_times):.2f}초</p>"
    analysis += f"<p>평균 코어 당 시간: {sum(cpu_times)/len(cpu_times):.2f}초</p>"
    if sum(cpu_times) < 10:
        analysis += "<p>CPU 성능이 좋은 편입니다.</p>"
    elif sum(cpu_times) < 20:
        analysis += "<p>CPU 성능이 보통 수준입니다.</p>"
    else:
        analysis += "<p>CPU 성능이 낮은 편입니다. 업그레이드를 고려해보세요.</p>"
    
    # RAM 분석
    analysis += "<h3>RAM 분석</h3>"
    ram = psutil.virtual_memory()
    analysis += f"<p>총 RAM: {ram.total/1024**3:.2f} GB</p>"
    if ram.total/1024**3 < 8:
        analysis += "<p>RAM 용량이 부족합니다. 업그레이드를 고려해보세요.</p>"
    else:
        analysis += "<p>RAM 용량은 적절한 편입니다.</p>"
    
    return analysis

def save_to_html(pc_info, cpu_info, ram_info, performance_result, analysis):
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"pc_performance_{now}.html"
    
    html_content = f"""
    <html>
    <head>
        <title>PC 성능 테스트 결과</title>
    </head>
    <body>
        {pc_info}
        {cpu_info}
        {ram_info}
        {performance_result}
        {analysis}
    </body>
    </html>
    """

    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"결과가 '{filename}' 파일로 저장되었습니다.")

if __name__ == '__main__':
    multiprocessing.freeze_support()

    pc_info = get_pc_info()
    cpu_info = get_cpu_info()
    ram_info = get_ram_info()
    performance_result, cpu_times = test_performance()
    analysis = analyze_results(pc_info, cpu_info, ram_info, performance_result, cpu_times)

    save_to_html(pc_info, cpu_info, ram_info, performance_result, analysis)