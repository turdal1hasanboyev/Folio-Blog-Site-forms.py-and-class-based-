from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from .models import User, Category, Contact, Portfolio, Comment, Article


admin.site.site_header = "Folio Admin Panel"
admin.site.site_title = "Folio Admin Panel"
admin.site.index_title = "Welcome to the Folio Administration Panel!"


# Register your models here


class UserAdmin(UserAdmin):
    ordering = ('id',)
    list_display = [
        'id',
        'get_full_name',
        'first_name',
        'last_name',
        'username',
        'email',
        'image',
        'video',
        'birthday',
        'age',
        'is_active',
        'is_staff',
        'is_superuser',
        'date_joined',
        'last_login',   
    ]
    readonly_fields = (
        'id',
        'age',
        'last_login',
        "date_joined",
    )
    list_filter = (
        'first_name',
        'last_name',
        'username',
        'email',
        'birthday',
        'is_active',
        'is_staff',
        'is_superuser',
        'date_joined',
        'last_login',
    )
    search_fields = (
        'first_name',
        'last_name',
        'username',
        'email',
    )
    fieldsets = (
        # Ma'lumotlarni tartiblash uchun
        (None, {
            'fields': ('username', 'email', 'password',)
        }),
        ('Personal Info', {
            'fields': ('first_name', 'last_name', 'bio', 'bio_1', 'image', 'video',)
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser')
        }),
        ('Important Dates', {
        'fields': ("date_joined", 'last_login', 'birthday', 'age',)
        }),
    )
    add_fieldsets = (
        # admin interfeys dan turib superuser yaratish uchun
        ('Create Super User', {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser',)}
        ),
    )


admin.site.register(User, UserAdmin)
# model, admin_class


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'created_at',
        'updated_at',
    )
    ordering = ('-created_at',)
    list_filter = ('name', 'created_at', 'updated_at',)
    search_fields = ('name',)
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'email',
        'subject',
        'created_at',
        'updated_at',
    )
    ordering = ('-id',)
    list_filter = ('name', 'email', 'subject', 'created_at', 'updated_at',)
    search_fields = ('name', 'email', 'subject',)
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'category__name', # ichma ich kirib korsatish
        'image',
        'created_at',
        'updated_at',
    )
    ordering = ('id',)
    list_filter = ('category__name', 'created_at', 'updated_at',)
    # foreign key bog'lanishda ichma ich kirish
    search_fields = ('category__name',)
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )
    

# admin.site.register(Comment)
# admin.site.register(Article)

# default admin interface register


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    ordering = ('-id',)
    list_display = (
        'id',
        'name',
        'image',
        'category',
        # category o'zidan name qaytaradi
        'author',
        # bu ham o'zidan str qiymat qaytaradi ichma ich kirish ham shart emas
        'views_count',
        'created_at',
        'updated_at',
    )

    # Admin sahifada faqat foreign key qism bilan ish qilish mumkin

    prepopulated_fields = {
        'slug': ('name',),
    }
    list_filter = (
        'name',
        'category__name', # foreign keyda ichma ich kirish ham kirmaslik ham mumkin
        # list_filter va search_fields da ichma ich kirish shart
        'author',
        'views_count',
        'created_at',
        'updated_at',
    )
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )
    search_fields = (
        # faqat search fields uchun ichma ich kirish shart
        # ichma ich kirish shart
        # __ ichma ich kirish usuli
        'name',
        'category__name',
        'author__first_name',
        'author__last_name',
    )


class CommentAdmin(admin.ModelAdmin):
    # agar to'g'ridan-to'g'ri bu usulda class bilan yozilsa eng tagidan
    # admin.site.register(Model, ModelAdmin) qilish shart

    ordering = ('-id',)
    list_display = (
        'id',
        'article',
        'user',
        'name',
        'email',
        'web_site',
    )
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'article__name',
        'user__first_name',
        'user__last_name',
        'name',
        'email',
        'web_site',
    )
    list_filter = (
        'article__name',
        'user__first_name',
        'user__last_name',
        'name',
        'email',
        'web_site',
        "created_at",
        "updated_at",
    )

admin.site.register(Comment, CommentAdmin)

# admin.site.register(Article, ArticleAdmin) # (model, modeladmin)
