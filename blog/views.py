from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Post, Tag, Category
import markdown
from comments.forms import CommentForm
from comments.models import Comment
from pure_pagination import Paginator


def common():
    """公用的方法, 右侧四块"""
    # 最新的文章
    post_list = Post.objects.all().order_by('-created_time')

    # 月份归档, 拿到所有的月份的文章
    date_post = Post.objects.dates('created_time', 'month', 'DESC')
    dates_list = {}  # 月份文章
    for date in date_post:
        """遍历月份"""
        count = Post.objects.filter(created_time__month=date.month).count()  # 拿到每个月的个数
        dates_list[date] = count  # 将月份和个数以字典存储

    # 分类
    category_list = Category.objects.all()

    # 标签
    tag_list = Tag.objects.all()

    context = {'post_list': post_list, 'dates_list': dates_list, 'category_list': category_list, 'tag_list': tag_list}
    return context


def paging(request, post_list):
    """分页公用方法"""
    # 获取点击页面的数字
    current_page = request.GET.get('page', 1)
    # 将所有数据分为10页
    paginator = Paginator(post_list, 10)
    page_obj = paginator.page(current_page)
    return page_obj


# @login_required
def index(request):
    """主页"""
    # 调用公用方法获取所有文章
    context = common()
    # 获取当前进入的页面数
    user = request.user
    # 通过公用方法分页
    page_obj = paging(request, context['post_list'])
    context['page_obj'] = page_obj
    context['user'] = user.username
    print(user)
    return render(request, 'blog/index.html', context)


def detail(request, pk):
    """详情页 TODO 阅读数没添加"""
    context = common()  # 获取侧边栏的数据
    post = get_object_or_404(Post, pk=pk)
    # 前端得通过|safe显示, 同时还得引入css和js的库来让代码高亮
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',  # 基础拓展
        # 'markdown.extensions.codehilite',  # 代码高亮
        'markdown.extensions.toc',  # 生成目录
    ])
    post.body = md.convert(post.body)
    post.toc = md.toc  # 给文章添加一个toc属性, 专门用于创建目录
    context['post'] = post

    # 传递表单的字段, 展示评论区域
    form = CommentForm()
    context['form'] = form

    # 展示评论信息
    comment_list = Comment.objects.filter(post=pk).order_by('-created_time')
    context['comment_list'] = comment_list

    return render(request, 'blog/detail.html', context)


def archive(request, year, month):
    """日期归档"""
    context = common()
    # 获取日期归档的文章, 也用post_list来接收, 在模板当中用同一个变量名
    post_list = Post.objects.filter(created_time__year=year, created_time__month=month)
    # 调用分页
    page_obj = paging(request, post_list)
    context['post_list'] = post_list
    context['page_obj'] = page_obj
    return render(request, 'blog/index.html', context=context)


def category(request, pk):
    """分类归档"""
    context = common()
    post_list = Post.objects.filter(category=pk)
    page_obj = paging(request, post_list)
    context['post_list'] = post_list
    context['page_obj'] = page_obj
    return render(request, 'blog/index.html', context=context)


def tag(request, pk):
    """标签归档"""
    context = common()
    post_list = Post.objects.filter(tags=pk)
    page_obj = paging(request, post_list)
    context['post_list'] = post_list
    context['page_obj'] = page_obj
    return render(request, 'blog/index.html', context=context)


def test(request):
    post = Post.objects.order_by('?')
    print(post)
    return HttpResponse('1')
    #                    传递的数据          设置显示中文
    # return JsonResponse({'key':'value'}, json_dumps_params={'ensure_ascii':False})
