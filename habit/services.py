import requests

from django.conf import settings


def send_tg_bot_massage(habit):
    url = settings.TG_BOT_URL
    token = settings.TG_BOT_TOKEN
    chat_id = settings.TG_CHAT_ID
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
