import customtkinter
from customtkinter import *
from PIL import Image
import tkinter as tk
from tkinter import messagebox, scrolledtext


window = customtkinter.CTk()
window.title("ALGORITHMS")
window.geometry("720x540")
window.resizable(False, False)

class BinarySearch():
    pass

class BitMap():
    pass

class SelectionSort():
    pass

class InsertionSort():
    pass

class BubbleSort():
    pass

class MergeSort():
    pass


try:
    bg_image = CTkImage(Image.open("assets/bg.jpg"), size=(720, 540))
    bg_label = CTkLabel(window, image=bg_image, text="")
    bg_label.place(x=0, y=0)
except FileNotFoundError:
    print("Ошибка: bg.jpg не найден. Используется запасной цвет.")
    window.config(background="#3498db")

title_label = CTkLabel(window, text="Выберите задачу!", font=CTkFont(size=30, weight="bold"), text_color="BLACK",fg_color="red")
title_label.place(relx=0.5, rely=0.2, anchor="center")



def open_binary_search():
    binary_search_window = CTkToplevel(window)
    binary_search_window.title("Бинарный поиск")
    binary_search_window.geometry("700x500")
    binary_search_window.attributes("-topmost",True)

    array_label = CTkLabel(binary_search_window, text="Введите отсортированный массив (через запятую):")
    array_label.pack(pady=(10, 0))
    array_entry = CTkEntry(binary_search_window)
    array_entry.pack()

    target_label = CTkLabel(binary_search_window, text="Введите искомое значение:")
    target_label.pack(pady=(10, 0))
    target_entry = CTkEntry(binary_search_window)
    target_entry.pack()

    result_text = scrolledtext.ScrolledText(binary_search_window, wrap=tk.WORD, height=10)
    result_text.pack(pady=(10, 0))
    result_text.config(state=tk.DISABLED)

    

    search_button = CTkButton(binary_search_window, text="Поиск") 
    search_button.pack(pady=20)

def open_bitmap_set():
    window = CTkToplevel(window)
    window.title("Bitmap Set")
    label = CTkLabel(window, text="Реализация Bitmap Set будет добавлена позже")
    label.pack(padx=20, pady=20)

def open_selection_sort():
    window = CTkToplevel(window)
    window.title("Selection Sort")
    label = CTkLabel(window, text="Реализация Selection Sort будет добавлена позже")
    label.pack(padx=20, pady=20)

def open_insertion_sort():
    window = CTkToplevel(window)
    window.title("Insertion Sort")
    label = CTkLabel(window, text="Реализация Insertion Sort будет добавлена позже")
    label.pack(padx=20, pady=20)

def open_bubble_sort():
    window = CTkToplevel(window)
    window.title("Bubble Sort")
    label = CTkLabel(window, text="Реализация Bubble Sort будет добавлена позже")
    label.pack(padx=20, pady=20)

def open_merge_sort():
    window = CTkToplevel(window)
    window.title("Merge Sort")
    label = CTkLabel(window, text="Реализация Merge Sort будет добавлена позже")
    label.pack(padx=20, pady=20)

def open_quick_sort():
    window = CTkToplevel(window)
    window.title("Quick Sort")
    label = CTkLabel(window, text="Реализация Quick Sort будет добавлена позже")
    label.pack(padx=20, pady=20)


def open_task(task_name):
    if task_name == "Binary Search":
        open_binary_search()
    elif task_name == "Bitmap Set":
        open_bitmap_set()
    elif task_name == "Selection Sort":
        open_selection_sort()
    elif task_name == "Insertion Sort":
        open_insertion_sort()
    elif task_name == "Bubble Sort":
        open_bubble_sort()
    elif task_name == "Merge Sort":
        open_merge_sort()
    elif task_name == "Quick Sort":
        open_quick_sort()


button_width = 200
button_height = 40
button_y_start = 200
button_y_offset = 60

tasks = ["Binary Search", "Bitmap Set", "Selection Sort", "Insertion Sort", "Bubble Sort", "Merge Sort", "Quick Sort"]
for i, task in enumerate(tasks):
    button = CTkButton(window, text=task, width=button_width, height=button_height,
                       command=lambda t=task: open_task(t),
                       font=CTkFont(size=16), corner_radius=0)
    button.place(relx=0.5, y=button_y_start + i * button_y_offset, anchor="center")

window.mainloop()