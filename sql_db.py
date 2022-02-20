import sqlite3 as sl


CON = sl.connect('users_landmarks.db', check_same_thread=False)


def create_db():
    from data.landmarks_json_creator import landmarks
    with CON:
        CON.execute('DROP TABLE IF EXISTS USERS;')
        CON.execute('CREATE TABLE USERS (user_id TEXT NOT NULL PRIMARY KEY, \
                    ' + '\n'.join(['landmark_'+str(i+1)+' BOOLEAN DEFAULT 0,' for i in range(len(landmarks))])[:-1]+');')


def new_user(user_id):
    with CON:
        sql_insert = f"INSERT INTO USERS (user_id) VALUES ('{user_id}');"
        CON.execute(sql_insert)


def user_visits_landmark(user_id, landmark_num):
    land_id = 'landmark_' + str(landmark_num)
    with CON:
        sql_update_land = f"UPDATE USERS \
                            SET {land_id} = 1 \
                            WHERE user_id = '{user_id}';"
        CON.execute(sql_update_land)


def select_landmarks(user_id):
    with CON:
        sql_select = f"SELECT * FROM USERS WHERE user_id = '{user_id}'"
        data = CON.execute(sql_select)
        dl = data.fetchall()[0]
        # for row in data:
        #     print(row)
        return dl


# create_db()
# new_user('f58')
# user_visits_landmark('f58', 4)
# dl = select_landmarks('f58')
# print(dl)
