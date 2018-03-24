#_*_coding:utf-8_*_

import xadmin

from .models import CityDict, CourseOrg, Teacher


class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']


class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'category', 'click_nums',
                    'fav_nums', 'image', 'address', 'city', 'add_time']
    search_fields = ['name', 'desc', 'category',
                     'click_nums', 'fav_nums', 'image', 'address', 'city']
    list_filter = ['name', 'desc', 'category', 'click_nums',
                   'fav_nums', 'image', 'address', 'city', 'add_time']
    # 外键以搜索形式查询
    relfieeld_style = 'fk_ajax'
    # 排序
    ordering = ['-click_nums']
    # 只读
    readonly_fields = ['click_nums']
    # 不显示 readonly_fields与exclude是有冲突
    exclude = ['fav_nums']


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_years', 'work_company',
                    'work_position', 'points', 'click_nums', 'fav_nums', 'add_time']
    search_fields = ['org', 'name', 'work_years', 'work_company',
                     'work_position', 'points', 'click_nums', 'fav_nums']
    list_filter = ['org', 'name', 'work_years', 'work_company',
                   'work_position', 'points', 'click_nums', 'fav_nums', 'add_time']

xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
