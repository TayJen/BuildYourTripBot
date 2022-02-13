import Constants as keys
from telegram.ext import *
import Responses as R
import cv2
from keras.models import load_model
import numpy as np
import json


print('Bot started...')


def start_command(update, context):
    update.message.reply_text('Type something random to get started!')


def help_command(update, context):
    update.message.reply_text('Just send the image with the Landmark that you want to classify')


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)

    update.message.reply_text(response)


def get_image(update, context):
    photo = update.message.photo[-1].get_file()
    photo.download('img.jpg')

    img = cv2.imread('img.jpg')
    img = cv2.resize(img, (299, 299))
    img = np.reshape(img, (1, 299, 299, 3))

    pred = model.predict(img)
    pred = np.argmax(pred)
    # print(pred)
    with open('labels.json', 'r') as fp:
        labels = json.load(fp)
        pred = labels[str(pred)]

    print(pred)
    update.message.reply_text(pred)


def error(update, context):
    print(f'Update {update} caused error: {context.error}')


def main():

    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('help', help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_handler(MessageHandler(Filters.photo, get_image))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


model = load_model('models/landscape_hEfficientNet.h5')
main()

