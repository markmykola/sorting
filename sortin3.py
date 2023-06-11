import tkinter as tk
from tkinter import messagebox
import time

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged

def sort_array():
    input_array = entry.get()  # Отримати введений масив

    try:
        # Перетворити рядок у список цілих чисел
        arr = list(map(int, input_array.split()))

        # Відображення кроків сортування злиттям
        steps = []
        start_time = time.time()
        merge_sort_with_steps(arr, steps)
        end_time = time.time()
        display_sort_steps(steps)

        # Розрахунок часу виконання
        execution_time = end_time - start_time
        best_case_time = calculate_best_case_time(len(arr))
        average_case_time = calculate_average_case_time(len(arr))
        worst_case_time = calculate_worst_case_time(len(arr))

        # Визначення типу масиву
        array_type = determine_array_type(arr)

        time_label.config(text=f"Execution Time: {execution_time:.6f} seconds\n"
                              f"Best Case Time: {best_case_time:.6f} seconds\n"
                              f"Average Case Time: {average_case_time:.6f} seconds\n"
                              f"Worst Case Time: {worst_case_time:.6f} seconds\n"
                              f"Array Type: {array_type}")

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter space-separated integers.")

def merge_sort_with_steps(arr, steps):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort_with_steps(left_half, steps)
    right_half = merge_sort_with_steps(right_half, steps)

    merged = merge(left_half, right_half)
    steps.append(merged)  # Додати проміжний крок у список кроків

    return merged

def display_sort_steps(steps):
    for i, step in enumerate(steps):
        step_label = tk.Label(root, text=f"Step {i + 1}: {step}")
        step_label.pack()

def calculate_best_case_time(size):
    return size * 0.01

def calculate_average_case_time(size):
    return size * 0.02

def calculate_worst_case_time(size):
    return size * 0.03

def determine_array_type(arr):
    min_value = min(arr)
    max_value = max(arr)
    average_value = sum(arr) / len(arr)

    if arr == sorted(arr):
        return "Best Case"
    elif arr == sorted(arr, reverse=True):
        return "Worst Case"
    elif min_value <= average_value <= max_value:
        return "Average Case"
    else:
        return "Unknown"

root = tk.Tk()
root.title("Merge Sort Trainer")

label = tk.Label(root, text="It is Merge Sort Trainer")
label.pack()

label = tk.Label(root, text="Enter integers separated by spaces:")
label.pack()

entry = tk.Entry(root, width=50)
entry.pack()

sort_button = tk.Button(root, text="Sort", command=sort_array)
sort_button.pack()

time_label = tk.Label(root, text="")
time_label.pack()

root.mainloop()

