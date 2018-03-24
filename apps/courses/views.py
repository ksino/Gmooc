# _*_coding:utf-8_*_

from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.db.models import Q

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import Course, CourseResource, Video
from operation.models import UserFavorite, CourseComments, UserCourse
from utils.mixin_utils import LoginRequiredMixin

class CourseListView(View):
    def get(self, request):
        all_courses = Course.objects.all()
        hot_courses = Course.objects.all().order_by("-click_num")[:3]

        # seacrch key word
        search_keyword = request.GET.get('keywords',"")
        if search_keyword:
            all_courses = all_courses.filter(Q(name__icontains=search_keyword)|Q(desc__icontains=search_keyword)|Q(detail__icontains=search_keyword))

        # 排序
        sort = request.GET.get('sort', "")
        if sort:
            if sort == "students":
                all_courses = all_courses.order_by("-students")
            elif sort == "hot":
                all_courses = all_courses.order_by("-click_num")

        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_courses, 6, request=request)
        courses = p.page(page)
        return render(request, 'course-list.html', {
            'all_courses': courses,
            'sort': sort,
            'hot_courses': hot_courses,
            })


class VideoPlayView(View):
    def get(self, request, video_id):
        video = Video.objects.get(id=int(video_id))
        course = video.lesson.course

        user_courses = UserCourse.objects.filter(user=request.user, course=course)
        if not user_courses:
            user_course = UserCourse(user=request.user, course=course)
            user_course.save()
         # 学习当前课程的所有用户
        user_courses =UserCourse.objects.filter(course=course)
        # 遍历用户id
        user_ids = [user_couser.user.id for user_couser in user_courses]
        # 用户的所有课程
        all_user_courses = UserCourse.objects.filter(user_id__in=user_ids)
        # 课程所有id
        course_ids = [all_user_course.course.id for all_user_course in all_user_courses]

        relate_courses = Course.objects.filter(id__in=course_ids).order_by("-click_num")[:5]

        all_resources = CourseResource.objects.filter(course=course)

        return render(request, 'course-play.html', {
            'course': course,
            'all_resources': all_resources,
            'relate_courses': relate_courses,
            'video': video,
            })



class CourseDetailView(View):
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))

        #点击数
        course.click_num += 1
        course.save()

        # 收藏
        has_fav_course = False
        has_fav_org = False

        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course.id, fav_type=1):
                has_fav_course = True

            if UserFavorite.objects.filter(user=request.user, fav_id=course.course_org.id, fav_type=2):
                has_fav_org = True


        tag = course.tag
        if tag:
            relate_courses = Course.objects.filter(tag=tag)[:3]
        else:
            relate_courses = []

        return render(request, 'course-detail.html', {
            'course': course,
            'relate_courses': relate_courses,
            'has_fav_course': has_fav_course,
            'has_fav_org': has_fav_org,

            })


class CourseInfoView(LoginRequiredMixin, View):
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        course.students += 1
        course.save()

        user_courses = UserCourse.objects.filter(user=request.user, course=course)
        if not user_courses:
            user_course = UserCourse(user=request.user, course=course)
            user_course.save()
         # 学习当前课程的所有用户
        user_courses =UserCourse.objects.filter(course=course)
        # 遍历用户id
        user_ids = [user_couser.user.id for user_couser in user_courses]
        # 用户的所有课程
        all_user_courses = UserCourse.objects.filter(user_id__in=user_ids)
        # 课程所有id
        course_ids = [all_user_course.course.id for all_user_course in all_user_courses]

        relate_courses = Course.objects.filter(id__in=course_ids).order_by("-click_num")[:5]

        all_resources = CourseResource.objects.filter(course=course)

        return render(request, 'course-video.html', {
            'course': course,
            'all_resources': all_resources,
            'relate_courses': relate_courses,
            })


class CommentView(LoginRequiredMixin, View):
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        all_resources = CourseResource.objects.filter(course=course)
        all_comments = CourseComments.objects.all()

        return render(request, 'course-comment.html', {
            'course': course,
            'all_resources': all_resources,
            'all_comments': all_comments,
            })


class AddCommentView(View):
    """用户课程评论
    """
    def post(self, request):
        if not request.user.is_authenticated():
            return HttpResponse('{"status": "fail", "msg": "用户未登录"}', content_type="application/json")
        course_id = request.POST.get("course_id", 0)
        comments = request.POST.get("comments", "")
        if course_id > 0 and comments:
            course_comments = CourseComments()
            course = Course.objects.get(id=int(course_id))
            course_comments.course = course
            course_comments.comments = comments
            course_comments.user = request.user
            course_comments.save()
            return HttpResponse('{"status": "success", "msg": "添加成功"}', content_type="application/json")
        else:
            return HttpResponse('{"status": "fail", "msg": "添加失败"}', content_type="application/json")





