from django.contrib import admin

# Register your models here.

from catalog.models import Author, Genre, Book, BookInstance

#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Genre)
#admin.site.register(BookInstance)

class BookAuthors(admin.TabularInline):
    model = Book

# Define the admin class

class AuthorAdmin(admin.ModelAdmin):
    list_display=('last_name','first_name','date_of_birth')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

    inlines = [BookAuthors]


# Register the admin class with the associado model
admin.site.register(Author, AuthorAdmin)


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BoookAdmin(admin.ModelAdmin):
    list_display=('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]




#Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookIstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back', 'language')
    list_display = ('status','borrower', 'due_back', 'id', 'language', 'book')
    


    fieldsets =(
        (None, {
           'fields': ('book', 'imprint', 'id')
        }),
        ('Availability',{
           'fields': ('status', 'due_back', 'borrower', 'language')
        }),
    )
