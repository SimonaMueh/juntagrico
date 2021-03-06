# -*- coding: utf-8 -*-

from juntagrico.models import *


class JobTypeDao:

    @staticmethod
    def types_by_coordinator(member):
        return JobType.objects.filter(activityarea__coordinator=member)

    @staticmethod
    def types_by_area(area_id):
        return JobType.objects.all().filter(activityarea=area_id)
