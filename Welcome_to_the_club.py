from rembg import remove
from PIL import Image
import os

# Удаление фона и сохранение изображения
input_path = 'try.jpg'  # название фото
output_path = 'output_test_photo.png'  # название нового фото с обрезанным фоном

input_image = Image.open(input_path)
output_image = remove(input_image)  # удаление фона
output_image.save(output_path)  # сохранение нового фото

# Загрузка обрезанного фото и создание по контуру чёрного прямоугольника
brain_black = Image.open("output_test_photo.png")
width = brain_black.width
height = brain_black.height
rectangle = Image.new("RGBA", (width, height), "white")
brain_black.paste(rectangle, mask=brain_black)

# Загрузка обрезанного фото и создание по контуру чёрного прямоугольника
brain_black = brain_black.resize((width + 200, height + 96))  # настройка увеличения контура

brain_regular = Image.open("output_test_photo.png")
brain_black.paste(brain_regular, (94, 54), mask=brain_regular)
brain_black.save("line_photo.png")

# Уменьшение обрезанного фото
img = Image.open('line_photo.png')  # открытие нового фото с обрезанным фоном
img.thumbnail(size=(512, 512))  # уменьшение фото
# img.show()
img.save('final_photo.png')  # сохранение нового фото

os.remove('line_photo.png')
os.remove('output_test_photo.png')
# os.remove('try.jpg')