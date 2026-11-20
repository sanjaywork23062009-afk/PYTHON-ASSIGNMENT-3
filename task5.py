import random
import time
import sys

def clean_readings_loop(readings):
    valid_celsius = []
    for r in readings:
        if -50 <= r <= 50:
            valid_celsius.append(r)
    valid_fahrenheit = [(c * 9/5) + 32 for c in valid_celsius]
    return valid_celsius, valid_fahrenheit

def clean_readings_comprehension(readings):
    valid_celsius = [r for r in readings if -50 <= r <= 50]
    valid_fahrenheit = [(c * 9/5) + 32 for c in valid_celsius]
    return valid_celsius, valid_fahrenheit

def clean_readings_map_filter(readings):
    valid_celsius = list(filter(lambda r: -50 <= r <= 50, readings))
    valid_fahrenheit = list(map(lambda c: (c * 9/5) + 32, valid_celsius))
    return valid_celsius, valid_fahrenheit

def get_alarm_minutes(readings):
    return [i for i, r in enumerate(readings) if not (2 <= r <= 8) and -50 <= r <= 50]

if __name__ == "__main__":
    for size in [10000, 100000, 1000000]:
        print(f"\n--- Testing with {size} readings ---")
        readings = [random.randint(-60, 60) for _ in range(size)]

        start = time.time()
        res1 = clean_readings_loop(readings)
        print(f"Loop time: {time.time() - start:.6f} s")

        start = time.time()
        res2 = clean_readings_comprehension(readings)
        print(f"Comprehension time: {time.time() - start:.6f} s")

        start = time.time()
        res3 = clean_readings_map_filter(readings)
        print(f"Map/Filter time: {time.time() - start:.6f} s")

        assert res1 == res2 == res3

    sample_readings = [0, 3, 50, 55, -55, 7, -2]
    print("\nAlarm minutes:", get_alarm_minutes(sample_readings))

    comp = [r for r in sample_readings if -50 <= r <= 50]
    gen = (r for r in sample_readings if -50 <= r <= 50)
    print("Size of list comprehension result:", sys.getsizeof(comp))
    print("Size of generator expression:", sys.getsizeof(gen))

    dict_comp = {i: r for i, r in enumerate(sample_readings) if -50 <= r <= 50}
    set_comp = {r for r in sample_readings if -50 <= r <= 50}
    print("Dictionary comprehension:", dict_comp)
    print("Set comprehension:", set_comp)
