import json

from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


# Create your models here.


# def validate_answer(answer):
#     answer = json.loads(answer)
#     if type(answer) is not list:
#         raise ValidationError(
#             _('%(answer)s is not an even number list'),
#             params={'Answer': answer},
#         )
#     for item in answer:
#         if item is None or item < 1 or item > 7:
#             raise ValidationError(
#                 _('%(answer)s ，问卷未填写完毕，或提交值非法'),
#                 params={'Answer': answer},
#             )


# 提交信息表
class SpecialSubmit(models.Model):
    WjId = models.IntegerField(verbose_name='关联问卷id')
    Number = models.IntegerField(verbose_name='第number位提交的人')
    Data = models.DateField(default=timezone.now().date(), verbose_name='提交日期')
    Time = models.TimeField(default=timezone.now().time(), verbose_name='提交时间')
    SubmitIp = models.CharField(max_length=15, verbose_name='提交ip')
    UseTime = models.IntegerField(verbose_name='填写用时')  # 单位：秒
    Agent = models.CharField(max_length=300, verbose_name='提交客户端')
    Answer = models.CharField(max_length=50, verbose_name='提交的答案', null=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['WjId', 'Agent'], name='unique_WjId_Agent')
        ]

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s, %s' % (self.Agent, self.Answer)

    def save(self, *args, **kwargs):
        answer = json.loads(self.Answer)
        if type(answer) is not list:
            return
        for item in answer:
            if item is None or item < 1 or item > 7:
                return
        else:
            super().save(*args, **kwargs)
