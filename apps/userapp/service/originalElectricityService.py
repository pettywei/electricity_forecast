#__*__coding:utf-8__*__
from userapp.dao import originalElectricityDao
from userapp.util.getUserElectricity import getEveryUserElectricity
from userapp.chart_code.drawLineChart import lineChart


# 与用电量相关的业务逻辑
def originalElectricityService(userList, startTime, endTime):
    # 查询用电量
    originalElectricity_list = originalElectricityDao.select(userList, startTime, endTime)

    # 将查询结果封装成：{用户:[每个月用电量]} 的形式
    user_electricity = {}
    for user in userList:
        user_electricity = getEveryUserElectricity(user_electricity, originalElectricity_list, user)

    # 将时间封装成一个list
    time_list = []
    for x in originalElectricity_list:
        time_list.append(str(x.time))

    # 调用绘图函数
    svgUrl = lineChart(time_list, user_electricity)
    return svgUrl