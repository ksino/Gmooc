# _*_coding:utf-8_*_

from django.conf.urls import url, include


from .views import UsersInfoView, UpLoadImageView, UpdatePwdView
from .views import SendEmailCodeView, UpdateEmailView, MyCourseView, MyFavOrgView
from .views import MyFavTeacherView, MyFavCourseView, MyMessageView

# http://127.0.0.1:8000/users/
urlpatterns = [
    url(r'^info/$', UsersInfoView.as_view(), name="info"),
    # 修改头像
    url(r'^image/upload/$', UpLoadImageView.as_view(), name="image_upload"),
    # 个人中心修改密码
    url(r'^update/pwd/$', UpdatePwdView.as_view(), name="update_pwd"),
    # 发送邮箱验证码
    url(r'^sendemail_code/$', SendEmailCodeView.as_view(), name="sendemail_code"),
    # 修改邮箱
    url(r'^update_email/$', UpdateEmailView.as_view(), name="update_email"),
    # 我的课程
    url(r'^mycourse/$', MyCourseView.as_view(), name="mycourse"),
    # 收藏的机构
    url(r'^myfav/org/$', MyFavOrgView.as_view(), name="myfav_org"),
    # 收藏的讲师
    url(r'^myfav/teacher/$', MyFavTeacherView.as_view(), name="myfav_teacher"),
    # 收藏的课程
    url(r'^myfav/course/$', MyFavCourseView.as_view(), name="myfav_course"),
    # 我的消息
    url(r'^mymessage/$', MyMessageView.as_view(), name="mymessage"),
]
