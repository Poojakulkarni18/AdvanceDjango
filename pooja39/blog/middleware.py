#def my_middleware(get_response):
#     print("One Time Initialization")
#     def my_function(request):
#       print("This is before view")
#       response = get_response(request)
#       print("This is after view")
#       return response
#     return my_function    
class BrotherMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print("One Time Brother Initialization")
    def __call__(self,request):
        print("Brother Before View")
        response = self.get_response(request)
        print("Brother After View")
        return response

class FatherMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print("One Time Father Initialization")
    def __call__(self,request):
        print("Father Before View")
        response = self.get_response(request)
        print("Father After View")
        return response

class MotherMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print("One Time Mother Initialization")
    def __call__(self,request):
        print("Mother Before View")
        response = self.get_response(request)
        print("Mother After View")
        return response

