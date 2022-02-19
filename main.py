import Constants as keys
from telegram.ext import *
import Responses as R
import cv2
from keras.models import load_model
import numpy as np
import json
from sql_db import CON, new_user, user_visits_landmark
from io import BytesIO


print('Bot started...')


def start_command(update, context):
    update.message.reply_text(f'Hello {update.message.from_user.first_name}!')
    new_user(update.message.from_user['id'])


def help_command(update, context):
    update.message.reply_text('Just send the image with the Landmark that you want to classify')


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)

    update.message.reply_text(response)


def get_image(update, context):
    photo = update.message.photo[-1].get_file()
    # photo.download('img.jpg')
    # https://stackoverflow.com/questions/59876271/how-to-process-images-from-telegram-bot-without-saving-to-file
    # img = cv2.imread(photo)
    # img = cv2.imdecode(np.fromstring(BytesIO(photo.download_as_bytearray()).getvalue(), np.uint8), 1)
    # frombuffer
    img = cv2.imdecode(np.frombuffer(BytesIO(photo.download_as_bytearray()).getvalue(), np.uint8), 1)
    img = cv2.resize(img, (299, 299))
    img = np.reshape(img, (1, 299, 299, 3))
    # img = cv2.resize(img, (384, 384))
    # img = np.reshape(img, (1, 384, 384, 3))

    pred = model.predict(img)
    print(pred)
    max_pred_value = np.max(pred)
    pred = np.argmax(pred) + 1
    print(pred)
    user_visits_landmark(update.message.from_user['id'], pred)
    with open('labels.json', 'r') as fp:
        labels = json.load(fp)
        pred = labels[str(pred)]

    print(pred)

    if max_pred_value <= 2.4:
        pred = 'Sorry our model is uncertain about this one :('

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
# model = load_model('models/effnet_b7')
main()

