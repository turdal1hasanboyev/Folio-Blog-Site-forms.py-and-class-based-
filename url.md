```python
Hozirgi sahifani qaytaradi

url = request.path # faqat yo'l (for education)
url = request.build_absolute_uri() # to'lliq domen va yo'l (for production)

Hozirgidan 1 ta oldingi sahifani qaytaradi

url = request.META.get('HTTP_REFERER') # 1ta oldingi sahifani qaytaradi
```

```python
    url = request.path # hozirgi sahifani oddiy usulda qaytaradi for education
    url_1 = request.get_full_path() # to'lliq qaytarish for education
    url_2 = request.get_raw_uri() # to'lliq qaytarish for production
    url_3 = request.META.get("HTTP_REFERER") # bitta oldingi sahifani qaytarish for production
    url_4 = request.build_absolute_uri() # mutlaq url qaytarish for production
    get = request.GET # GET request qaytarish for production
    post = request.POST # POST request qaytarish for production
    get_get = request.GET.get('') # GET dan get olish
    post_post = request.POST.get('') # POST dan get olish
```
