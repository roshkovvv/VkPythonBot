
import vk_api

from vk_api.longpoll import VkLongPoll, VkEventType



token="токен" # Paste you token

bh = vk_api.VkApi(token = token)
give = bh.get_api()
longpoll = VkLongPoll(bh)

def answer(id, text):
    bh.method('messages.send', {'user_id' : id, 'message' : text, 'random_id': 0})

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
       if event.to_me:

     
          message = event.text.lower()
         
          id = event.user_id
    
   

          if message == 'hello':
            answer(id, 'Hello! I am VK bot on python.')

          elif message == 'How are you?':
              answer(id, 'I am fine, thanks.' )

          else:
             answer(id, 'What did you say?')
