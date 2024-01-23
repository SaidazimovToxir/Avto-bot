import requests
import json

BASE_URL = 'http://127.0.0.1:8000/api/v1'

def create_user(username, name, user_id, phone_number):
    url = f"{BASE_URL}/bot-users"
    
    response = requests.get(url=url).json()
    user_exist = any(i['user_id'] == str(user_id) for i in response)
    response = requests.get(url=url)
    
    if not user_exist:
        requests.post(url=url, json={
            'username': username,
            'name': name,
            'phone_number': phone_number,
            'user_id': user_id
        })
        return 'Foydalanuvchi yaratildi.'
    else: return "Foydalanuvchi mavjud."
    
    
# print(create_user('DEV','Ali','12345678','+998941234567'))

def create_feedback(name, user_id, body):
    url = f"{BASE_URL}/feedbacks"
    
    if name and body and user_id:
        post ={
            'name': name,
            'user_id': user_id,
            'body': body
        }
        
        response = requests.post(url=url, json=post)
        if response.status_code == 201:
            return "Adminga yuborildi, Fikringiz uchun raxmat"
        else: return "Xatolik yuz berdi"
        
    else: return "Amal oxiriga yetmadi"
    
# print(create_feedback('Vali','987654321','Zor'))