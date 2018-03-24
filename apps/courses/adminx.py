#_*_coding:utf-8_*_

import xadmin

from .models import Course, Lesson, Video, CourseResource, BannerCourse


class LessonInline(object):
    model = Lesson
    extra = 0


class CourseResourceInline(object):
    model = CourseResource
    extra = 0


class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree',
                    'learn_times', 'students', 'fav_nums', 'get_zj_nums']
    search_fields = ['name', 'desc', 'detail',
                     'degree', 'students', 'fav_nums']
    list_filter = ['name', 'desc', 'detail', 'degree',
                   'learn_times', 'students', 'fav_nums']
    # 将有外键的表嵌入
    inlines = [LessonInline, CourseResourceInline]
    # 列表页直接修改字段
    list_editable = ['degree', 'desc']


class BannerCourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree',
                    'learn_times', 'students', 'fav_nums']
    search_fields = ['name', 'desc', 'detail',
                     'degree', 'students', 'fav_nums']
    list_filter = ['name', 'desc', 'detail', 'degree',
                   'learn_times', 'students', 'fav_nums']
    inlines = [LessonInline, CourseResourceInline]

    # 只显示轮播课程
    def queryset(self):
        qs = super(BannerCourseAdmin, self).queryset()
        qs = qs.filter(is_banner=True)
        return qs

class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name', 'add_time']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson__name', 'name', 'add_time']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    search_fields = ['course', 'name', 'download']
    list_filter = ['course', 'name', 'download', 'add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(BannerCourse, BannerCourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
