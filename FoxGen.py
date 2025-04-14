import tkinter as tk
from tkinter import ttk
import requests
from PIL import Image, ImageTk
from io import BytesIO

# Функция для загрузки изображения с API
def fetch_fox_image():
    response = requests.get("https://randomfox.ca/floof/")
    if response.status_code == 200:
        data = response.json()
        image_url = data['image']
        return image_url
    else:
        print("Ошибка при загрузке изображения")
        return None


def update_image():
    global photo  
    image_url = fetch_fox_image()
    if image_url:
        response = requests.get(image_url)
        image_data = response.content
        image = Image.open(BytesIO(image_data))
        image = image.resize((400, 400), Image.Resampling.LANCZOS)  
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.image = photo  

# Создаем главное окно
root = tk.Tk()
root.title("Генератор лис")
root.geometry("450x500")  # Размер окна


image_label = ttk.Label(root)
image_label.pack(pady=20)

# Создаем кнопку для обновления изображения
update_button = ttk.Button(root, text="Новая лиса", command=update_image)
update_button.pack(pady=10)

# Загружаем первое изображение
update_image()

# Запускаем главный цикл обработки событий
root.mainloop()