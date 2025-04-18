# Лимарев Степан ИУ7-21Б. Сокрытие информации в изображении меотодом наименее значащих битов.

# Импортирование модуля tkinter для реализации графического интерфейса.
import tkinter as tk
from tkinter import filedialog, END, Tk, Button, Label, Text

# Импортирование функций из модуля.
from funcs import encode_image, decode_image

# Функция выбора изображения.
def select_image():
    return filedialog.askopenfilename(filetypes=[("BMP files", "*.bmp")])

# Функция сохранения изображения.
def save_image():
    return filedialog.asksaveasfilename(defaultextension=".bmp", filetypes=[("BMP files", "*.bmp")])

# Функция скрытия текста.
def hide_text():
    input_image = select_image()
    if not input_image:
        return
    
    output_image = save_image()
    if not output_image:
        return
    
    text = text_entry.get("1.0", END).strip()
    
    try:
        encode_image(input_image, output_image, text)
        status_label.config(text="Текст скрыт.")
    except ValueError as e:
        status_label.config(text=str(e))

# Функция извлечения текста.
def extract_text():
    input_image = select_image()
    if not input_image:
        return
    
    try:
        extracted_text = decode_image(input_image)
        text_entry.delete("1.0", END)
        text_entry.insert(END, extracted_text)
        status_label.config(text="Текст извлечен.")
    except ValueError as e:
        status_label.config(text=str(e))

# Графический интерфейс.
root = Tk()
root.title("Стеганография")

Label(root, text="Введите текст для скрытия:").pack()

text_entry = Text(root, height=5, width=50)
text_entry.pack()

Button(root, text="Скрыть текст", command=hide_text).pack()
Button(root, text="Извлечь текст", command=extract_text).pack()

status_label = Label(root, text="")
status_label.pack()

root.mainloop()
