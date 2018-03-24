# _*_coding:utf-8_*_

from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.views.static import serve

import xadmin

from users.views import LoginView, RegisterView, ActiveView, ForgetPwdView
from users.views import ResetView, ModifyPwdView, LogoutView, IndexView
from organization.views import OrgView
from Gmooc.settings import MEDIA_ROOT
# from maxone.settings import STATIC_ROOT

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    # url(r'^$', TemplateView.as_view(template_name="index.html"), name="index"),
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^login/$', LoginView.as_view(), name="login"),
    url(r'^logout/$', LogoutView.as_view(), name="logout"),
    url(r'^register/$', RegisterView.as_view(), name="register"),
    # 验证码
    url(r'^captcha/', include('captcha.urls')),
    url(r'^active/(?P<active_code>.*)/$', ActiveView.as_view(), name="user_active"),
    url(r'^forget/$', ForgetPwdView.as_view(), name="forget_pwd"),
    url(r'^reset/(?P<active_code>.*)/$', ResetView.as_view(), name="reset_pwd"),
    url(r'^modify/$', ModifyPwdView.as_view(), name="modify_pwd"),

    # 课程机构
    url(r'^org/', include('organization.urls', namespace="org")),
    # 配置上传文件的访问处理函数
    url(r'^media/(?P<path>.*)$', serve, {"document_root":MEDIA_ROOT}),
    # 课程相关
    url(r'^course/', include('courses.urls', namespace="course")),
    # user
    url(r'^users/', include('users.urls', namespace="users")),
    # 配置404,500
    # url(r'^static/(?P<path>.*)$', serve, {"document_root":STATIC_ROOT}),
]

# 404
handler404 = 'users.views.page_not_found'
# 500
handler500 = 'users.views.page_error'
