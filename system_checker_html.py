import psutil
import os
import time
from datetime import datetime

def system_info_to_html():
    html_content = "<html><head><title>System Information Report</title></head><body>"
    html_content += "<h1>System Information:</h1>"
    html_content += f"<p>CPU cores: {psutil.cpu_count(logical=False)} (Physical), {psutil.cpu_count(logical=True)} (Logical)</p>"
    html_content += f"<p>Total RAM: {psutil.virtual_memory().total / (1024**3):.2f} GB</p>"
    html_content += f"<p>Disk Information: {psutil.disk_usage('/').total / (1024**3):.2f} GB Total</p>"
    html_content += f"<p>Operating System: {os.name}</p>"
    return html_content

def stress_test_to_html(duration=10):
    html_content = "<h1>Stress Test Results:</h1>"
    results = []
    start_time = time.time()
    end_time = start_time + duration

    try:
        while time.time() < end_time:
            # Stressing CPU
            [x**2 for x in range(10000000)]
            
            # Checking the current CPU and Memory usage
            cpu_usage = psutil.cpu_percent(interval=1)
            memory_usage = psutil.virtual_memory().percent
            results.append((cpu_usage, memory_usage))
    except KeyboardInterrupt:
        html_content += "<p>Stress test interrupted by user.</p>"
    
    for i, (cpu, mem) in enumerate(results, start=1):
        html_content += f"<h2>Measurement {i}</h2>"
        html_content += f"<p>CPU usage: {cpu}% - Indicates how much CPU was utilized during this point of the test.</p>"
        html_content += f"<p>Memory usage: {mem}% - Indicates the percentage of total memory that was in use.</p>"
    
    return html_content

def generate_report():
    html_report = system_info_to_html()
    html_report += stress_test_to_html()
    # Adding a GitHub link at the bottom of the report
    github_link = "https://github.com/amirer/SysCheckReport"
    html_report += f"<p>View this project on <a href='{github_link}'>GitHub</a>.</p>"
    html_report += "</body></html>"
    with open(f"system_report_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.html", "w") as file:
        file.write(html_report)
    print(f"Report has been saved as 'system_report_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.html'.")

def main():
    print("Gathering system information...")
    input("\nPress Enter to start the stress test...")
    generate_report()

if __name__ == "__main__":
    main()
