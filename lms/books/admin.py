from django.contrib import admin

# Register your models here.
from .models import Book




# @admin.register(Student)
class BookAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "author", "price", "publish", "stock"]


admin.site.register(Book, BookAdmin)