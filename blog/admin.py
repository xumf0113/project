from django.contrib import admin
from .models import Post, Category, Tag


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']
    # 后台添加文章的时候可以只添加这些信息, 因为有些信息有默认值, 可以不用写, 作者默认为管理员, 可以通过下面save_model方法来自动添加作者
    fields = ['title', 'body', 'excerpt', 'category', 'tags', 'created_time']
    ordering = ['id']

    def save_model(self, request, obj, form, change):
        """调用ModelAdmin里面保存数据的方法, 在每次"""
        obj.author = request.user
        super(PostAdmin, self).save_model(request, obj, form, change)



admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
