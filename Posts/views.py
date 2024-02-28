from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


posts = [
  {
    "id":1,
    "title":"django",
    "content":"we love django"
  },
   {
    "id":2,
    "title":"python",
    "content":"we love python django"
  }
]


@api_view(http_method_names=['GET','POST'])
def homePage(request:Request):
  if request.method =='POST':
    data = request.data
    response ={"message":"hello world","data":data}
    return Response(data = response,status=status.HTTP_201_CREATED)
  response ={'message':"hello world"}
  return Response(data = response,status=status.HTTP_200_OK)

@api_view(http_method_names=['GET','POST'])
def list_posts(request:Request):
  return Response(data=posts,status=status.HTTP_200_OK)


@api_view(http_method_names=['GET','POST'])
def post_detail(request:Request,index:int):
  post = posts[index]
  if post:
    return Response(data = post,status=status.HTTP_200_OK)
  return Response(data={'Error':"data not found"},status=status.HTTP_404_NOT_FOUND)