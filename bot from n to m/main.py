from datetime import datetime
from notat import from_n_to_10, from_10_to_n, if_a_bigger_b, abcerror, bc

import vk_api
from vk_api.longpoll import VkEventType, VkLongPoll
import random
import time

token = "тут должен быть ваш токен"
vk_session = vk_api.VkApi(token=token)

session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)



while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print(str(event.text))
            response = str(event.text)
            response = event.text.lower()
            response = response.split(' ')
            arr1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
            arr2 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            ls=[]
            
            if event.from_user and not (event.from_me):
                    if response[0] == "инфо" or response[0] == "начать":
                        res = 'Привет, я могу перевести число из одной системы исчисления в другую. Для этого ты должен через пробел написать 3 числа: первое - это число, которое нужно перевести, второе - это система исчисления, в которой это число находится и третье - система исчисления, в которую нужно перевести. Пример: 46458 10 2 или HRT29 35 16'
                    else:
                        if len(response) != 3:
                            res = 'Что-то не так? Напиши "Инфо"'
                        else:
                            a = response[0]
                            b = response[1]
                            c = response[2]
                            array = [a, b, c]
                            lg = 0
                            
                            if abcerror(a, arr1) == 1:
                                res = "Используй только арабские цифры и латиницу"
                            
                            elif abcerror(b, arr2) == 1:
                                res = "Система может быть только числом от 2 до 36"
                                
                            elif abcerror(c, arr2) == 1:
                                res = "Система может быть только числом от 2 до 36"
                                    
                            elif bc(int(b)) == 1:
                                res = 'Ошибка системы исчисления (система не может быть меньше 2)'
                                
                            elif bc(int(c)) == 1:
                                res = 'Ошибка системы исчисления (система не может быть меньше 2)'
                                            
                            elif if_a_bigger_b(a, int(b)) == 1:
                                res = 'Ошибка системы исчисления'
                                                
                            elif a == '0':
                                res = a

                            else:
                                ans = from_n_to_10(a, int(b))
                                ans1 = from_10_to_n(ans, int(c))
                                res = str(ans1)
            
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': res, 'random_id': 0})
