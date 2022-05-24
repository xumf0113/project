from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # path('test', views.test, name='test'),  #
    path('', views.index, name='index'),  # 首页
    path('posts/<int:pk>', views.detail, name='detail'),  # 详情页
    path('archive/<int:year>/<int:month>', views.archive, name='archive'),  # 日期归档
    path('category/<int:pk>', views.category, name='category'),  # 分类
    path('tag/<int:pk>', views.tag, name='tag'),  # 标签
]
