
from django.contrib import admin

from mezzanine.core.admin import TabularDynamicInlineAdmin
from mezzanine.pages.admin import PageAdmin

from models import (HomePage, Slide, IconBox, Client,
                    Portfolio, PortfolioItem, PortfolioItemImage,
                    PortfolioItemCategory)


class SlideInline(TabularDynamicInlineAdmin):
    model = Slide


class IconInline(TabularDynamicInlineAdmin):
    model = IconBox


class ClientInline(TabularDynamicInlineAdmin):
    model = Client


class HomePageAdmin(PageAdmin):
    inlines = (SlideInline, IconInline, ClientInline)


class PortfolioItemImageInline(TabularDynamicInlineAdmin):
    model = PortfolioItemImage


class PortfolioItemAdmin(PageAdmin):
    inlines = (PortfolioItemImageInline,)


admin.site.register(HomePage, HomePageAdmin)
admin.site.register(Portfolio, PageAdmin)
admin.site.register(PortfolioItem, PortfolioItemAdmin)
admin.site.register(PortfolioItemCategory)
