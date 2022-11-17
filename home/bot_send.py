import requests

from home.models import IncomingMessages
token='5787008554:AAFRcFiz8vbHsaShhfk85DFqm7mLhaOqLe4'
chat_id='-1001890361218'

def bot_send(text,img=None):
    if img:
        resp = requests.post(f'https://api.telegram.org/bot{token}/sendPhoto?chat_id={chat_id}&caption={text}&parse_mode=html',files=img)
    else: resp = requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}&parse_mode=html')
    return resp
def get_mess(id):
    m = IncomingMessages.objects.filter(id=id).first()
    if m:
        data = ""
        data+=f'#xabar\n\n'
        data+=f'<b>Saytdan kelgan xabar</b>\n\n'
        data+=f'<b>FIO</b>: {m.fullname}\n'
        data+=f'<b>Fakultet</b>: {m.faculty}\n'
        data+=f'<b>Yo\'nalish</b>: {m.direction}\n'
        data+=f'<b>Telefon raqam</b>: {m.phone}\n'
        data+=f'<b>Xabar</b>: {m.content}\n'
        return str(data)