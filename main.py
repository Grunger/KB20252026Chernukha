# Random Task Generator (Генератор случайных задач)
# Создать GUI-приложение «Random Task Generator» с использованием библиотеки random, сохранением истории и Git.

import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import random

def load_notes():
    """Загрузка задач из файла"""
    try:
        with open("notes.json", "r", encoding="utf-8") as file:
            notes_list.extend(json.load(file))
            update_listbox()
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_notes():
    """Сохранение задач в файл"""
    try:
        with open('notes.json', 'w', encoding='utf-8') as f:
            json.dump(notes_list, f, ensure_ascii=False, indent=4)
    except (FileNotFoundError, json.JSONDecodeError):
        print('Error Write File')
  
def add_note():
    """Добавление задачи"""
    title_note = entry_title_note.get().strip()
    text_note = entry_note.get().strip()
    if title_note != '' and text_note != '':
        note = f'{title_note}: {text_note}'
        notes_list.append(note)
        update_listbox()
        save_notes()
    else:
        messagebox.showwarning("Предупреждение", "Введите текст задачи.")

def edit_note():
    """Редактирование задачи"""
    selected = note_listbox.curselection()
    if selected:
        new_text = simpledialog.askstring("Редактирование", "Новый текст задачи")
        notes_list[selected[0]] = new_text
        update_listbox()
        save_notes()
    else:
        messagebox.showwarning("Предупреждение", "Выберите задачу для редактирования")

def remove_note():
    """Удаление задачи"""
    selected = note_listbox.curselection()

    if selected:
       note = selected[0]
       notes_list.pop(note)
       update_listbox()
       save_notes()
    else:
       messagebox.showwarning("Предупреждение", "Выберите задачу для удаления")


def update_listbox():
    note_listbox.delete(0, tk.END)
    for note in notes_list:
       note_listbox.insert(tk.END, note)

random_notes = ['Прочитать статью', 'Сделать зарядку', 'Написать программу', 'Окончить Код будущего']
notes_list = []  # Список задач
for i in range(random.randint(1, len(random_notes))):
    notes_list.append(random.choice(random_notes))


window = tk.Tk()
window.title("Список задач")
window.geometry("400x400")
window.resizable(False, False)  # Отключаем изменение размера окна


#  Listbox для отображения заметок
note_listbox = tk.Listbox(window, height=10, width=50, selectmode=tk.SINGLE)
note_listbox.pack(pady=5)
update_listbox()

# Поле ввода (Entry) для заголовка заметки
entry_title_note = tk.Entry(window, width=10)
entry_title_note.pack()

# Поле ввода (Entry) для новой заметки
entry_note = tk.Entry(window, width=10)
entry_note.pack()

# Кнопка "Добавить заметку"
tk.Button(window, text="Добавить задачу", command=add_note, bg="#4CAF50", fg="white").pack(pady=5)
# Кнопка "Редактировать заметку"
tk.Button(window, text="Редактировать задачу", command=edit_note, bg="#C9FF41", fg="white").pack(pady=5)
# Кнопка "Удалить заметку"
tk.Button(window, text="Удалить выбранную задачу", command=remove_note, bg="#F2AF50", fg="white").pack(pady=5)

# Загрузка заметок из файла
load_notes()

window.mainloop()
