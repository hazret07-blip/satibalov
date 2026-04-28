import tkinter as tk
from tkinter import ttk, messagebox
import random
import json
import os

# 1. Список предопределённых цитат
quotes = [
    {"text": "Жизнь — это то, что с нами случается, пока мы строим планы.", "author": "Джон Леннон", "theme": "Жизнь"},
    {"text": "Код — это просто.", "author": "Неизвестный разработчик", "theme": "Разработка"},
    {"text": "Учиться никогда не поздно.", "author": "Цицерон", "theme": "Мотивация"},
    {"text": "Будьте собой; все остальные роли уже заняты.", "author": "Оскар Уайльд", "theme": "Личность"},
    {"text": "Python — отличный язык.", "author": "Гвидо ван Россум", "theme": "Разработка"}
]

HISTORY_FILE = "history.json"


class QuoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Генератор случайных цитат")
        self.root.geometry("500x500")

        self.history = self.load_history()

        # UI Элементы
        self.label_quote = tk.Label(root, text="Нажмите кнопку, чтобы получить цитату", wraplength=400,
                                    font=("Arial", 12), height=4)
        self.label_quote.pack(pady=20)

        self.label_author = tk.Label(root, text="", font=("Arial", 10, "italic"))
        self.label_author.pack(pady=5)

        # 2. Кнопка «Сгенерировать цитату»
        self.btn_gen = tk.Button(root, text="Сгенерировать цитату", command=self.generate_quote)
        self.btn_gen.pack(pady=10)

        # 4. Фильтрация
        frame_filter = tk.Frame(root)
        frame_filter.pack(pady=10)
        tk.Label(frame_filter, text="Фильтр по автору:").pack(side=tk.LEFT)
        self.entry_filter = tk.Entry(frame_filter)
        self.entry_filter.pack(side=tk.LEFT, padx=5)
        self.btn_filter = tk.Button(frame_filter, text="Фильтр", command=self.show_history)
        self.btn_filter.pack(side=tk.LEFT)

        # 3. История цитат
        tk.Label(root, text="История:").pack()
        self.history_listbox = tk.Listbox(root, width=60, height=10)
        self.history_listbox.pack(pady=10)

        self.show_history()

    def generate_quote(self):
        quote = random.choice(quotes)
        self.label_quote.config(text=f"\"{quote['text']}\"")
        self.label_author.config(text=f"— {quote['author']} ({quote['theme']})")

        # Сохранение в историю
        self.history.append(quote)
        self.save_history()
        self.show_history()

    def save_history(self):
        with open(HISTORY_FILE, "w", encoding="utf-8") as f:
            json.dump(self.history, f, ensure_ascii=False, indent=4)

    def load_history(self):
        if os.path.exists(HISTORY_FILE):
            with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        return []

    def show_history(self):
        self.history_listbox.delete(0, tk.END)
        filter_text = self.entry_filter.get().lower()

        # Фильтрация истории
        for q in reversed(self.history):
            if not filter_text or filter_text in q['author'].lower():
                self.history_listbox.insert(tk.END, f"{q['author']}: {q['text'][:30]}...")


if __name__ == "__main__":
    root = tk.Tk()
    app = QuoteApp(root)
    root.mainloop()
