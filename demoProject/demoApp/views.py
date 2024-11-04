# from django.shortcuts import render
from rest_framework.decorators import api_view , APIView
from rest_framework.response import Response
from demoApp.models import *
from demoApp.serializers import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.

# func based view 
# class based view

#first we will do func based view cuz its easier and we can learn it quick

#but afterwards class will be used 

# Person.object.all()
# [1, 2, 3 ,4] -> QuerySet

@api_view(['GET','POST','PUT'])
def students(request):
    info = {
            1 : 'Daniyal',
            2 : 'Ibrahim'
        }
        
    if request.method == 'GET':
        print(request.GET.get("search"))           #just getting a specidied data
        print("You Hit a GET method")
        return Response(info)
       
    
    elif request.method == 'POST':
        data = request.data
        print('******')
        print(data["age"])   #specific key
        print('******')
        print("You Hit a POST method")
        return Response(info)
    
    elif request.method == 'PUT':
        print("You Hit a PUT method")
        return Response(info)
        
@api_view(['GET','POST','PUT','PATCH', 'DELETE'])
def person(request):
    if request.method =='GET':
        objs = Person.objects.all()    #it returns a QuerySet
        serializer =  PeopleSerializers(objs , many = True)
        return Response(serializer.data)
    elif request.method == "POST":
        data = request.data
        serializer = PeopleSerializers(data = data)
        if serializer.is_valid():          # to check if data is in a json format to serialize
            serializer.save() 
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == "PUT":
        data = request.data
        serializer = PeopleSerializers(data = data)
        if serializer.is_valid():          # to check if data is in a json format to serialize
            serializer.save() 
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == "PATCH":
        data = request.data
        obj = Person.objects.get(id = data['id'])
        serializer = PeopleSerializers(obj, data = data , partial = True)
        if serializer.is_valid():          # to check if data is in a json format to serialize
            serializer.save() 
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method == "DELETE":
        data = request.data
        obj = Person.objects.get(id = data['id'])
        obj.delete()
        return Response({'messege' : 'person deleted'})


# @api_view(["GET","POST"])
# def employee(request, pk=None):
#     if request.method == "GET":
#         if pk:
#             obj=Employee.objects.get(id=pk)
#             info=EmployeeSerializer(obj)
#             return Response(info.data)
#         objects=Employee.objects.all()
#         info= EmployeeSerializer(objects, many=True)

#         print(info.data)
#         return Response(info.data)

@login_required
@api_view(["GET","POST",'PUT','PATCH', 'DELETE'])
def employee(request, pk=None):
    if request.method == "GET":
        if pk:
            obj = Employee.objects.get(id=pk)
            info = EmployeeSerializer(obj)
            return Response(info.data)
        objects = Employee.objects.all()
        info = EmployeeSerializer(objects, many=True)

        print(info.data)
        return Response(info.data)

    elif request.method == "POST":
        data = request.data
        serializer = EmployeeSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method == "PUT":
        data = request.data
        serializer = EmployeeSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == "PATCH":
        data = request.data
        obj = Employee.objects.get(id = data['id'])
        serializer = EmployeeSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == "DELETE":
        data = request.data
        obj = Employee.objects.get(id = data['id'])
        obj.delete()
        return Response({"Messege : Person deleted!"})


#USER             ------------->  AUTHENTICATIONNNN <--------------

@login_required
@api_view(["GET","POST"])
def user(request):
    if request.method == "GET":
        # data = request.data
        objects = User.objects.all()
        info = UserSerializer(objects, many=True)
        return Response(info.data)
    
    elif  request.method == "POST":
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            user=User.objects.create(first_name=data["first_name"],last_name=data["last_name"],username=data["username"])
            user.set_password(data["password"])
            user.save()
            return Response(serializer.data)
        return Response(serializer.errors)



@api_view(["POST"])        
def signin(request):
    data = request.data
    username = data['username']
    password = data['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return Response({"Messege : User logged in!"})
    else:
        return Response({"Messege : User not found!"})
    
@api_view(["POST"])
def signout(request):
    logout(request)
    return Response({"Messege : User logged out!"})

@api_view(["GET"])
def employee2(request):
        if request.method == "GET":
            #data = request.data
            objects = Employee_2.objects.all()
            info = EmployeeSerializer(objects, many=True)
            return Response(info.data)


@api_view(['GET','POST','DELETE'])
def customer(request):
    if request.method ==  "GET":
        objects = Customer.objects.all()
        info = CustomerSerializer(objects, many=True)
        return Response(info.data)

    elif  request.method == "POST":
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            user=User.objects.create(first_name=data["first_name"],last_name=data["last_name"],username=data["username"],email=data["email"])
            user.set_password(data["password"])
            user.save()

            customer = Customer.objects.create(
                user=user,
                contact=data["contact"],
                email=data["email"]  # Make sure to pass the email here
            )
            customer.save()

            return Response({
                "user": UserSerializer.data,
                "customer": CustomerSerializer(customer).data
            })
        return Response(serializer.errors)





# JWT Authenticaton
class LoginAPI(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = LoginSerializer(data=data)
            if serializer.is_valid():
                email = serializer.validated_data['email']
                password = serializer.validated_data['password']

                user = authenticate(email=email, password=password)

                if user is None:
                    return Response({
                        'status': 400,
                        'message': 'Invalid password',
                        'data': {}
                    }, status=400)

                refresh = RefreshToken.for_user(user)

                return Response({
                    'status': 200,
                    'message': 'Login successful',
                    'refresh': str(refresh),
                    'access': str(refresh.refresh),
                }, status=200)

            return Response({
                'status': 400,
                'message': 'Something went wrong',
                'data': serializer.errors
            }, status=400)
        except Exception as e:
            print(e)
            return Response({
                'status': 500,
                'message': 'Internal server error',
                'error': str(e)
            }, status=500)



