#__*__coding:utf-8__*__
# 原始电量的dao操作

from userapp import models


# 根据传入的参数查询原始用电量
def select(userList, startTime=201101, endTime=201608):
    # 锁定错误,查询语句有错
    #originalElectricity_list = models.OriginalElectricity.objects.all().values_list('id', 'time', userList).filter(
    #    time__range=[startTime, endTime])

    # 临时测试使用，查询所有记录
    originalElectricity_list = models.OriginalElectricity.objects.all()

    print(len(originalElectricity_list))

    return originalElectricity_list

