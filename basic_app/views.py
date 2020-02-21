from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView
from basic_app.models import UserProfile, Questions


class Signup(APIView):
    def get(self, request):
        # This will show the signup page by the get request of user,
        # for testing post request check send data by postman
        all_user = UserProfile.objects.all()

        list_of_user = []   
        for user in all_user:
            dict_of_user = {
                'name': user.name,
                'age': user.age,
                'phone': user.phone
            }
            list_of_user.append(dict_of_user)

        return Response(list_of_user)

    def post(self, request):    
        received_json_data = json.loads(request.body.decode("utf-8"))   
        phone = received_json_data['phone']
        name = received_json_data['name']
        age = received_json_data['age']

        user_prof = UserProfile(name=name, age=age, phone=phone)
        user_prof.save()

        dic = {
            "name": name,
            "phone": phone,
            "age": age
        }
        return JsonResponse(dic, status=201)


class Question(APIView):
    def get(self, request):
        all_questions = Questions.objects.all()
        list_of_question = []

        for que in all_questions:
            dict_of_questions = {
                'title': que.title,
                'text': que.text,
                'accuracy': que.accuracy
            }
            list_of_question.append(dict_of_questions)

        return Response(list_of_question)

    def post(self, request):
        received_json_data = json.loads(request.body.decode("utf-8"))
        title = received_json_data['title']
        text = received_json_data['text']
        accuracy = received_json_data['accuracy']

        que = Questions(title=title, text=text, accuracy=accuracy)
        que.save()

        dic = {
            "title": title,
            "text": text,
            "accuracy": accuracy
        }

        return JsonResponse(dic, status=201)
