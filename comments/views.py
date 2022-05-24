from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.contrib import messages

from .models import Comment
from .forms import CommentForm
from blog.models import Post


@require_POST
def comment(request, post_pk):
    """评论提交的处理, TODO 可以异步提交"""
    post = get_object_or_404(Post, pk=post_pk)

    # 生成评论的表单模型
    form = CommentForm(request.POST)
    if form.is_valid():  # 通过django的校验
        # 成功后将数据保存来生成评论模型
        comment = form.save(commit=False)
        comment.post = post  # 添加评论对应的文章
        comment.save()  # 保存评论
        messages.add_message(request, messages.SUCCESS, '评论成功', extra_tags='success')
        return redirect(reverse('blog:detail', kwargs={'pk': post_pk}))
    # 失败则回到原本页面, 将错误的信息展现页面上
    context = {'form': form, 'post': post}
    messages.add_message(request, messages.ERROR, '评论失败', extra_tags='error')
    return render(request, 'blog/detail.html', context=context)
