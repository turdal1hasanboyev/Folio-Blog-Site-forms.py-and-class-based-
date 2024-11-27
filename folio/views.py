from django.shortcuts import render, redirect, get_object_or_404

from django.views import View
from django.views.generic import ListView
from django.contrib import messages

from .models import User, Portfolio, Article, Comment
from .forms import ContactForm


# Create your views here.


'''
Hozirgi sahifani qaytaradi

url = request.path # faqat yo'l (for education)
url = request.build_absolute_uri() # to'lliq domen va yo'l (for production)

Hozirgidan 1ta oldingi sahifani qaytaradi

url = request.META.get('HTTP_REFERER') # 1ta oldingi sahifani qaytaradi
'''


class HomePageView(View):
    template_name = 'index.html'

    def get_context_data(self, request, *args, **kwargs):
        # Contextni tayyorlash

        context = {}

        context['user'] = User.objects.get(id=1)
        context['portfolios'] = Portfolio.objects.all().order_by('-id')[:6]
        context['articles'] = Article.objects.all().order_by('-created_at')[:3]

        context['form'] = ContactForm()  # ContactForm-ni qo'shish

        return context

    def get(self, request, *args, **kwargs):
        # GET so'rovi uchun contextni render qilish

        context = self.get_context_data(**kwargs)

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        url = request.build_absolute_uri()

        # POST so'rovi orqali ma'lumotlarni qabul qilish va saqlash

        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, 'Your message has been sent. Thank you!')

        else:
            messages.error(request, 'There was an error in your form. Please correct it.')

        return redirect(url)


"""
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.contrib import messages


class HomePageView(TemplateView):
    template_name = 'index.html'  # Shablon fayli nomi

    def get_context_data(self, **kwargs):
        # Asosiy contextni tayyorlash

        context = super().get_context_data(**kwargs)

        # Qo'shimcha ma'lumotlarni qo'shish

        context['user'] = User.objects.get(id=1)
        context['portfolios'] = Portfolio.objects.all().order_by('-id')[:6]
        context['articles'] = Article.objects.all().order_by('-created_at')[:3]

        context['form'] = ContactForm()  # ContactForm-ni qo'shish

        return context

    def post(self, request, *args, **kwargs):
        # POST so'rovini ishlash

        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, 'Your message has been sent. Thank you!')

        else:
            messages.error(request, 'There was an error in your form. Please correct it.')

        return redirect(request.build_absolute_uri())

"""


class BlogsGridPageView(ListView):
    model = Article
    template_name = 'blog-grid.html'  # Shablon fayli
    context_object_name = 'articles'  # Shablonda foydalanadigan kontekst nomi
    queryset = Article.objects.all().order_by('-id')[:6]  # 6 ta oxirgi maqolani olish


"""
from django.shortcuts import render
from django.views import View
from .models import Article


class BlogsGridPageView(View):
    template_name = 'blog-grid.html'  # Shablon fayli

    def get(self, request, *args, **kwargs):
        # Maqolalarni olish

        articles = Article.objects.all().order_by('-id')[:6]

        # Shablon bilan kontekstni render qilish

        return render(request, self.template_name, {'articles': articles})

"""


'''
def article_detail_page_view(request, slug):
    url = request.path # hozirgi sahifani oddiy usulda qaytaradi for education
    url_1 = request.get_full_path() # to'lliq qaytarish for education
    url_2 = request.get_raw_uri() # to'lliq qaytarish for production
    url_3 = request.META.get("HTTP_REFERER") # bitta oldingi sahifani qaytarish for production
    url_4 = request.build_absolute_uri() # mutlaq url qaytarish for production
    get = request.GET # GET request qaytarish for production
    post = request.POST # POST request qaytarish for production
    get_get = request.GET.get('') # GET dan get olish
    post_post = request.POST.get('') # POST dan get olish

    article = get_object_or_404(Article, slug__iexact=slug)

    comments = Comment.objects.filter(article_id=article.id).order_by('-id')

    if request.method == 'POST':
        comment = Comment()

        comment.article.id = article.id
        comment.user.id = request.user.id
        comment.name = request.POST.get('name')
        comment.email = request.POST.get('email')
        comment.web_site = request.POST.get('web_site')
        comment.comment = request.POST.get('comment')

        comment.save()

        return redirect(article.get_absolute_url())

    context = {
        'article': article,
        'comments': comments,
    }

    return render(request, 'blog-single.html', context)
'''


class ArticleDetailPageView(View):
    template_name = 'blog-single.html'

    def get(self, request, slug, *args, **kwargs):
        article = get_object_or_404(Article, slug__iexact=slug)

        comments = Comment.objects.filter(article_id=article.id).order_by('-id')

        context = {}

        context['article'] = article
        context['comments'] = comments
        # context ni avval bo'sh yaratib keyin qiymat berish

        return render(request, self.template_name, context)
    
    def post(self, request, slug, *args, **kwargs):
        article = get_object_or_404(Article, slug__iexact=slug)

        comment = Comment()

        comment.article.id = article.id
        comment.user.id = request.user.id
        comment.name = request.POST.get('name')
        comment.email = request.POST.get('email')
        comment.web_site = request.POST.get('web_site')
        comment.comment = request.POST.get('comment')

        comment.save()

        return redirect(article.get_absolute_url())
    

# def get_context_data bilan ishlash
'''
class ArticleDetailPageView(View):
    template_name = 'blog-single.html'

    def get_context_data(self, slug, **kwargs):
        article = get_object_or_404(Article, slug__iexact=slug)

        comments = Comment.objects.filter(article_id=article.id).order_by('-id')

        context = {}

        context['article'] = article
        context['comments'] = comments

        return context
    
    def get(self, request, slug, *args, **kwargs):
        context = self.get_context_data(slug, **kwargs)

        return render(request, self.template_name, context)
    
    def post(self, request, slug, *args, **kwargs):
        article = get_object_or_404(Article, slug__iexact=slug)

        comment = Comment()

        comment.article.id = article.id
        comment.user.id = request.user.id
        comment.name = request.POST.get('name')
        comment.email = request.POST.get('email')
        comment.web_site = request.POST.get('web_site')
        comment.comment = request.POST.get('comment')

        comment.save()

        return redirect(article.get_absolute_url())
'''
