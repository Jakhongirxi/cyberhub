from django.contrib import admin

from news.models import News, Comment

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_field', 'content_field', 'pub_date', 'pub_time', 'updated_date', 'updated_time')
    fields = ('title', 'content', 'pub_date', 'image')
    search_fields = ('title',)


    def title_field(self, obj):
        return self.short_text(obj.title)

    def content_field(self, obj):
        return self.short_text(obj.content)

    def short_text(self, text, max_len=10):
        if len(text) > max_len:
            return f"{text[:max_len]}..."
        return text

    def pub_date(self, obj):
        return obj.pub_date.strftime('%Y.%m.%d')

    def pub_time(self, obj):
        return obj.pub_date.strftime('%H:%M')

    def updated_date(self, obj):
        return obj.pub_date.strftime('%Y.%m.%d')

    def updated_time(self, obj):
        return obj.pub_date.strftime('%H:%M')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'news', 'message', 'created', 'updated')

    def username(self, obj):
        return obj.user.username
    username.short_description = 'Username'
