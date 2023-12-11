
import re

def shorthand_utility():
    path_to_image = input("Укажите путь до изображения: ")
    mode = input("укажите режим работы - hide или unhide: ")
    secret = input("Укажите секрет: ")

    if  mode == 'unhide':
        with open(path_to_image, 'rb') as image:
            decode_utf16  = str(image.read().decode('utf-16').encode('utf-8'))
            init_get_secret = re.compile(r"\w{3}\\").split(decode_utf16)[-1]
            secret = ''.join(list(init_get_secret)[1:-1])
            return print(secret)
    
    if mode == 'hide':
        with open(path_to_image, 'ab') as image:
            image.write(bytes( '\\' + secret,'utf-16',''))
            print(f'Данные скрыты в изображении - {path_to_image}')
        return 

shorthand_utility()




