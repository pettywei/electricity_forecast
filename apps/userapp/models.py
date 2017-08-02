#__*__coding:utf-8__*__
from __future__ import unicode_literals

from django.db import models


# Create your models here.

# 原始用电量
class OriginalElectricity(models.Model):
    # id = models.IntegerField(primary_key=True,verbose_name=u"主键")
    time = models.IntegerField(max_length=6, verbose_name=u"时间")
    all = models.DecimalField(max_digits=20, decimal_places=2, verbose_name=u"总用电量")
    UserA = models.DecimalField(max_digits=20, decimal_places=2, verbose_name=u"用户A")
    UserB = models.DecimalField(max_digits=20, decimal_places=2, verbose_name=u"用户B")
    UserC = models.DecimalField(max_digits=20, decimal_places=2, verbose_name=u"用户C")
    UserD = models.DecimalField(max_digits=20, decimal_places=2, verbose_name=u"用户D")
    # UserE = models.DecimalField(max_digits=20, decimal_places=2, verbose_name=u"用户E")
    UserF = models.DecimalField(max_digits=20, decimal_places=2, verbose_name=u"用户F")
    UserG = models.DecimalField(max_digits=20, decimal_places=2, verbose_name=u"用户G")
    UserH = models.DecimalField(max_digits=20, decimal_places=2, verbose_name=u"用户H")
    UserI = models.DecimalField(max_digits=20, decimal_places=2, verbose_name=u"用户I")
    UserJ = models.DecimalField(max_digits=20, decimal_places=2, verbose_name=u"用户J")
    UserK = models.DecimalField(max_digits=20, decimal_places=2, verbose_name=u"用户K")
    UserL = models.DecimalField(max_digits=20, decimal_places=2, verbose_name=u"用户L")
    UserM = models.DecimalField(max_digits=20, decimal_places=2, verbose_name=u"用户M")
    UserN = models.DecimalField(max_digits=20, decimal_places=2, verbose_name=u"用户N")
    UserO = models.DecimalField(max_digits=20, decimal_places=2, verbose_name=u"用户O")
    UserP = models.DecimalField(max_digits=20, decimal_places=2, verbose_name=u"用户P")
    UserQ = models.DecimalField(max_digits=20, decimal_places=2, verbose_name=u"用户Q")
    UserR = models.DecimalField(max_digits=20, decimal_places=2, verbose_name=u"用户R")
    UserS = models.DecimalField(max_digits=20, decimal_places=2, verbose_name=u"用户S")
    UserT = models.DecimalField(max_digits=20, decimal_places=2, verbose_name=u"用户T")

    class Meta:
        verbose_name = u"原始用电量"
        verbose_name_plural = verbose_name
