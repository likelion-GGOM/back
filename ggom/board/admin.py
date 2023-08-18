from django.contrib import admin
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['title', 'create_date']  # 목록에 표시될 필드
    search_fields = ['title', 'content']               # 검색할 수 있는 필드
    list_filter = ['create_date']            # 필터링할 수 있는 필드

admin.site.register(Question, QuestionAdmin)
