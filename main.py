import pytesseract.pytesseract
import telebot
from PIL import Image
from pytesseract import image_to_string

bot = telebot.TeleBot("7033254554:AAGSmt6TbgrKjsWvcnO4QRlyk0XayqM8cSw")
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract\tesseract.exe'
tessdata_dir_config = r'--tessdata-dir "C:\Program Files (x86)\Tesseract\tessdata"'


@bot.message_handler(content_types=['photo'])
def handle_image(message):
    file_id = message.photo[-1].file_id
    file_info = bot.get_file(file_id)
    download_file = bot.download_file(file_info.file_path)

    with open('image.jpg', 'wb') as image_file:
        image_file.write(download_file)

    image = Image.open('image.jpg')
    text = image_to_string(image, 'eng', config=tessdata_dir_config)

    bot.send_message(message.chat.id, text='текст : {}'.format(text), parse_mode='HTML')


bot.polling()
