import json
import pandas as pd


def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ('hello', 'hi', 'sup', 'привет', 'здравствуй'):
        return "Привет! Просто скинь мне фото достопримечательности, а я расскажу тебе про нее поподробнее"

    if user_message in ('who are you', 'who are you?', 'кто ты', 'кто ты?'):
        return 'Я BuildYourTripBot, помогаю с определением достопримечательности и краткой историей'

    return "Я не понимаю тебя :("


def photo_response(pred):
    df = pd.read_csv('data/Описание достопримечательностей.csv')
    with open('data/labels.json', 'r') as fp:
        labels = json.load(fp)
        pred = labels[str(pred)]
        out = df[df['GroupName'] == pred]['Description'].values[0]

    output = pred + '\n' + out

    return output


# print(photo_response(1))



