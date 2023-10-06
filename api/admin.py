from django.contrib import admin
from .models import Slide, TextBlock, Photo, Contact, Header, Footer, SiteIcon, Card


# @admin.register(Slide)
# class SlideAdmin(admin.ModelAdmin):
#     list_display = ('title', 'slide_order')
#     search_fields = ('title',)

class TextBlockInline(admin.TabularInline):
    model = TextBlock
    extra = 1  # Количество пустых форм для добавления текстовых блоков


class CardBlockInline(admin.TabularInline):
    model = Card
    extra = 1  # Количество пустых форм для добавления текстовых блоков


class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1  # Количество пустых форм для добавления фотографий


@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'slide_order')
    list_filter = ('slide_order',)
    search_fields = ('title', 'sub_title')
    inlines = [TextBlockInline, PhotoInline, CardBlockInline]


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'location', 'phone', 'email')


@admin.register(Header)
class HeaderAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'email', 'phone_number')
    list_filter = ('company_name', 'email')
    search_fields = ('company_name', 'email')


@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'user_agreement', 'company_description')
    list_filter = ('company_name',)
    search_fields = ('company_name',)


@admin.register(SiteIcon)
class SiteIconAdmin(admin.ModelAdmin):
    list_display = ('image', 'link')
