from django.shortcuts import render

# Create your views here.


'''
Hozirgi sahifani qaytaradi

url = request.path # faqat yo'l (for education)
url = request.build_absolute_uri() # to'lliq domen va yo'l (for production)

Hozirgidan 1ta oldingi sahifani qaytaradi

url = request.META.get('HTTP_REFERER') # 1ta oldingi sahifani qaytaradi
'''
