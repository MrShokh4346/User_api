from .models import User
from .serializers import UserSerializer
from django.http.response import JsonResponse
from rest_framework.decorators import api_view

#
@api_view(['GET', 'POST'])
def create_user(request):
    if request.method == 'POST':
        data = request.data
        print(data)

        user = User(
            f_name = data['f_name'],
            l_name = data['l_name'],
            email = data['email'],
            phone = data['phone'],
            photo = data['photo'],
            password = data['password']
        )
        user.save()
        data = UserSerializer(user)
        return JsonResponse(data.data)
    elif request.method == 'GET':
        users = User.objects.all()
        data = UserSerializer(users, many=True)
        return JsonResponse(data.data, safe=False)


@api_view(['GET', 'DELETE','PUT', 'PATCH'])
def user_detail(request, id):
    if request.method == 'PUT':
        data = request.data
        print(type(data['f_name']))
        user = User.objects.get(id=id)
        print(type(user.f_name))
        user.f_name = data["f_name"]
        user.l_name = data["l_name"]
        user.email = data["email"]
        user.phone = data["phone"]
        user.photo = data["photo"]
        user.password = data["password"]
        user.save()
        print(type(user.f_name))
        data = UserSerializer(user)
        return JsonResponse(data.data, safe=False)
    elif request.method == 'PATCH':
        data = request.data
        keys = data.keys()
        user = User.objects.get(id=id)
        user.f_name = request.data.get('f_name', user.f_name)
        user.l_name = request.data.get('l_name', user.l_name)
        user.email = request.data.get('email', user.email)
        user.phone = request.data.get('phone', user.phone)
        user.photo = request.data.get('photo', user.photo)
        user.password = request.data.get('password', user.password)
        user.save()
        data = UserSerializer(user)
        return JsonResponse(data.data, safe=False)
    elif request.method == 'GET':
        user = User.objects.get(id=id)
        data = UserSerializer(user)
        return JsonResponse(data.data, safe=False)
    elif request.method == 'DELETE':
        user = User.objects.get(id=id)
        id = user.id
        user.delete()
        return JsonResponse({'message':f"{id} - user deleted"})
