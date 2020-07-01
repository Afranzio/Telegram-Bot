import requests
import json
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
chatbot=ChatBot('Tele_Bot')
trainer = ChatterBotCorpusTrainer(chatbot) 

trainer.train('chatterbot.corpus.english.greetings',
                    'chatterbot.corpus.english.conversations')

url = 'https://api.telegram.org/bot'
token = '937907176:AAGeNcK8MMG8MpzKTsaRvBz09dSGjsW9liY'
progress = '/getUpdates'

response = requests.get(url+token+progress)
get = json.loads(response.text)
all_msg = get['result']
messages = all_msg[-1]['message']['text']
Chat_Id = all_msg[-1]['message']['chat']['id']

bot = chatbot.get_response(messages)

response = url+token+'/sendMessage?chat_id={Chat_Id}&text={bot}'
if bot is not None:
    requests.get(response)
