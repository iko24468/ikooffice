class MyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # This code is executed before before the
        # next middleware or view is called
        request.META['CUSTOM_KEY'] = "Nige"
        request.META['CRIB_POL'] = "Nige was here"

        response = self.get_response(request)

        # This code is executed after the view is called
        # I.e. on the "return journey"
        assert False
        return response


# def my_middleware(get_response):
#     def middleware(request):
#         request.META['CUSTOM_KEY'] = "Nige was here"
#         response = get_response(request)
#         assert False
#         return response
#     return middleware
