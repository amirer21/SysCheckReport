import psutil
import os
import time

def system_info():
    print("Gathering system information...")
    print(f"CPU cores: {psutil.cpu_count(logical=False)} (Physical), {psutil.cpu_count(logical=True)} (Logical)")
    print(f"Total RAM: {psutil.virtual_memory().total / (1024**3):.2f} GB")
    print(f"Disk Information: {psutil.disk_usage('/').total / (1024**3):.2f} GB Total")
    print(f"Operating System: {os.name}")

def stress_test(duration=10):
    print("\nStarting stress test...")
    start_time = time.time()
    end_time = start_time + duration
    load_percentage = 100

    try:
        while time.time() < end_time:
            # Stressing CPU
            [x**2 for x in range(10000000)]
            
            # Checking the current CPU and Memory usage
            cpu_usage = psutil.cpu_percent(interval=1)
            memory_usage = psutil.virtual_memory().percent
            print(f"CPU usage: {cpu_usage}%")
            print(f"Memory usage: {memory_usage}%")
    except KeyboardInterrupt:
        print("Stress test interrupted by user.")

def main():
    system_info()
    input("\nPress Enter to start the stress test...")
    stress_test()

if __name__ == "__main__":
    main()
