from django.contrib import admin

from .models import Choice, Question

admin.site.site_header = "Poll Admin"
admin.site.site_title = "Polls Admin Area"
admin.site.index_title = "Welcome to the Polls Admin Area"



class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):

    list_display = ('question_text', 'pub_date',
                    'was_published_recently')
    list_filter = ['pub_date']

    search_fields = ['question_text']
    # fieldsets = [
    #     (None,               {'fields': ['question_text']}),
    #     ('Date information', {'fields': ['pub_date'], 'classes':['collapse']}),
    # ]
    # inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)

admin.site.register(Choice)