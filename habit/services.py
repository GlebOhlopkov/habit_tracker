import requests

from config.settings import TG_BOT_URL, TG_BOT_TOKEN, TG_CHAT_ID


def send_tg_bot_massage(habit):
    url = TG_BOT_URL
    token = TG_BOT_TOKEN
    chat_id = TG_CHAT_ID
    if habit.reward:
        massage = (f'Hey! Start time to ACTION!\n'
                   f'You must {habit.action} at {habit.time} in {habit.place}\n'
                   f'After you can get: {habit.reward}')
        requests.post(
            url=f'{url}{token}/sendMassage',
            data={
                'chat_id': chat_id,
                'text': massage,
            }
        )
    elif habit.nice_habit:
        massage = (f'Hey! Start time to ACTION!\n'
                   f'You must {habit.action} at {habit.time} in {habit.place}\n'
                   f'After you can get: {habit.nice_habit.action}')
        requests.post(
            url=f'{url}{token}/sendMassage',
            data={
                'chat_id': chat_id,
                'text': massage,
            }
        )
