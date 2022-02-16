import pandas as pd
import numpy as np


def create_df():
    from landmarks_json_creator import landmarks
    df = pd.DataFrame(columns=['user_id']+landmarks)

    return df


def new_user(df, user_id):
    df.loc[len(df)] = 0
    df.iloc[-1, 0] = user_id

    return True


def new_landmark_for_user(df, user_id, landmark_name):
    df.loc[df.user_id == user_id, landmark_name] = 1

    return True


desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 30)

df = create_df()
new_user(df, '21312312')
new_user(df, '58')
new_user(df, 'fddsa')
new_landmark_for_user(df, '58', 'Москва-Сити')
new_landmark_for_user(df, '58', 'Парк «Зарядье»')
new_landmark_for_user(df, 'fddsa', 'Церковь Вознесения в Коломенском')
print(df)
