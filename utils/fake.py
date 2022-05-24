import os
import pathlib
import random
import sys
from datetime import timedelta

import django
import faker
from django.utils import timezone
from pathlib import Path

# 将项目根目录添加到 Python 的模块搜索路径中
BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)
sys.path.append(BASE_DIR)

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
    django.setup()

    # from blog.models import Category, Post, Tag
    # from comments.models import Comment
    # from django.contrib.auth.models import User

    # # 创建超级用户, 名字, 邮箱, 密码
    # user = User.objects.all().first()
    #
    # category_list = ['Python学习笔记', '开源项目', '工具资源', '程序员生活感情', 'test category']
    # tag_list = ['Django', 'Python', 'Pipenv', 'Docker', 'Nginx', 'Elasticsearch', 'Gunicorn', 'Supervisor', 'test tag']
    # a_year_go = timezone.now() - timedelta(days=365)
    #
    # for cate in category_list:
    #     Category.objects.create(name=cate)
    #
    # for tag in tag_list:
    #     Tag.objects.create(name=tag)
    #
    # # 创建测试文件
    # Post.objects.create(
    #     title='Markdown 与代码高度测试',
    #     body=pathlib.Path(BASE_DIR).joinpath('utils', 'md.sample').read_text(encoding='utf-8'),
    #     category=Category.objects.create(name='Markdown测试'),
    #     author=user
    # )
    # # 创建英文的随机文章
    # fake = faker.Faker()
    # for i in range(100):
    #     # 随机获取两个标签
    #     tags = Tag.objects.order_by('?')
    #     tag1 = tags.first()
    #     tag2 = tags.last()
    #     # 随机获取一个分类
    #     cate = Category.objects.order_by('?').first()
    #     # 随机获取一个时间
    #     created_time = fake.date_time_between(start_date='-1y', end_date='now', tzinfo=timezone.get_current_timezone())
    #     # 创建文章
    #     post = Post.objects.create(
    #         title=fake.sentence().rstrip('.'),
    #         body='\n\n'.join(fake.paragraphs(10)),
    #         created_time=created_time,
    #         category=cate,
    #         author=user,
    #     )
    #     post.tags.add(tag1, tag2)
    #     post.save()
    # # 创建中文的随便文章
    # fake = faker.Faker('zh-CN')
    # for i in range(100):
    #     # 随机获取两个标签
    #     tags = Tag.objects.order_by('?')
    #     tag1 = tags.first()
    #     tag2 = tags.last()
    #     # 随机获取一个分类
    #     cate = Category.objects.order_by('?').first()
    #     # 随机获取一个时间
    #     created_time = fake.date_time_between(start_date='-1y', end_date='now',
    #                                           tzinfo=timezone.get_current_timezone())
    #     # 创建文章
    #     post = Post.objects.create(
    #         title=fake.sentence().rstrip('.'),
    #         body='\n\n'.join(fake.paragraphs(10)),
    #         created_time=created_time,
    #         category=cate,
    #         author=user,
    #     )
    #     post.tags.add(tag1, tag2)
    #     post.save()
    #
    # # 创建评论
    # for post in Post.objects.all():
    #     # 获取文章的创建时间
    #     post_created_time = post.created_time
    #     delta_in_days = '-' + str((timezone.now() - post_created_time).days) + 'd'
    #     for i in range(random.randrange(3, 10)):
    #         Comment.objects.create(
    #             name=fake.name(),
    #             email=fake.email(),
    #             url=fake.uri(),
    #             text=fake.paragraph(),
    #             created_time=fake.date_time_between(start_date=delta_in_days, end_date='now',
    #                                                 tzinfo=timezone.get_current_timezone()),
    #             post=post
    #         )
