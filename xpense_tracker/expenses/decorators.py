from functools import wraps
from django.shortcuts import redirect



# def login_required(view_func):
#     @wraps(view_func)
#     def wrapper(request, *args, **kwargs):
#         if 'user_id' in request.session:
#             return view_func(request, *args, **kwargs)
#         else:
#             return redirect("login_page")

#     return wrapper