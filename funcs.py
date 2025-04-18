# Лимарев Степан ИУ7-21Б. Сокрытие информации в изображении методом наименее значащих битов.

# Импортирование модуля pillow для получения битовой карты изображения.
from PIL import Image

# Функция кодирования текста.
def encode_image(input_image_path, output_image_path, text):
    
    image = Image.open(input_image_path)
    
    # Преобразование текста.
    binary_text = ''.join(format(ord(char), '08b') for char in text) + '00000000'
    
    # Список пикселей изображения.
    pixels = list(image.getdata())
    
    # Проверка размера текста.
    if len(binary_text) > len(pixels) * 3:
        raise ValueError("Текст слишком длинный.")
    
    new_pixels = []
    binary_index = 0
    
    for pixel in pixels:
        new_pixel = list(pixel)
        
        for i in range(3):
            if binary_index < len(binary_text):
                new_pixel[i] = (new_pixel[i] & ~1) | int(binary_text[binary_index])
                binary_index += 1
        
        new_pixels.append(tuple(new_pixel))
    
    image.putdata(new_pixels)
    image.save(output_image_path)

# Функция декодирования текста из изображения.
def decode_image(image_path):
    image = Image.open(image_path)
    
    pixels = list(image.getdata())
    binary_text = ''
    
    for pixel in pixels:
        for i in range(3):
            binary_text += str(pixel[i] & 1)
    
    # Поиск маркера конца текста.
    end_index = binary_text.find("00000000")
    if end_index != -1:
        binary_text = binary_text[:end_index]
    else:
        raise ValueError("Маркер конца текста не найден.")
    
    chars = [binary_text[i:i+8] for i in range(0, len(binary_text), 8)]
    
    decoded_text = ''.join(chr(int(char, 2)) for char in chars)
    
    return decoded_text
