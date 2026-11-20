import random
import time

def analyze_rainfall(readings):
    if not readings:
        print("Rainfall list is empty.")
        return
    
    dry_days = [i for i, val in enumerate(readings) if val == 0]
    print(f"Dry days indices: {dry_days}")
    
    if len(readings) < 7:
        print("List is shorter than 7 values. Weekly totals and moving averages cannot be fully computed.")
        return

    weekly_totals = []
    for i in range(0, len(readings) - 6, 7):
        week = readings[i:i+7]
        weekly_totals.append(sum(week))
        
    if weekly_totals:
        max_weekly = max(weekly_totals)
        min_weekly = min(weekly_totals)
        wettest_week_idx = weekly_totals.index(max_weekly)
        driest_week_idx = weekly_totals.index(min_weekly)
        print(f"Wettest week index: {wettest_week_idx}, Total: {max_weekly}")
        print(f"Driest week index: {driest_week_idx}, Total: {min_weekly}")

    def naive_moving_average(data):
        ma = []
        for i in range(len(data) - 6):
            window = data[i:i+7]
            ma.append(sum(window) / 7.0)
        return ma

    def running_sum_moving_average(data):
        ma = []
        current_sum = sum(data[:7])
        ma.append(current_sum / 7.0)
        for i in range(1, len(data) - 6):
            current_sum = current_sum - data[i-1] + data[i+6]
            ma.append(current_sum / 7.0)
        return ma

    start = time.time()
    naive_moving_average(readings)
    naive_time = time.time() - start

    start = time.time()
    running_sum_moving_average(readings)
    running_time = time.time() - start

    print(f"Naive Moving Average Time: {naive_time:.6f} seconds")
    print(f"Running-Sum Moving Average Time: {running_time:.6f} seconds")

if __name__ == "__main__":
    for size in [365, 36500, 365000]:
        print(f"\n--- Testing with {size} readings ---")
        readings = [random.choice([0, 1, 2, 5, 10, 20, 50]) for _ in range(size)]
        analyze_rainfall(readings)

    print("\n--- Testing empty list ---")
    analyze_rainfall([])

    print("\n--- Testing short list (< 7 values) ---")
    analyze_rainfall([0, 5, 2, 0])
