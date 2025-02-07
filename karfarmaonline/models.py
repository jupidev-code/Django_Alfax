from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.utils import timezone
from extensions.utils import jalali_converter
from datetime import datetime, timedelta

class expenceManager(models.Manager):
    def total(self, project):
        total = expence.objects.filter(project=project).aggregate(Sum('amount'))['amount__sum']
        if total is None : total = 0
        return total

    def total_project(self, project):
        total = expence.objects.filter(project=project)
        return total
    def total_project_user(self, user,project):
        total = expence.objects.filter(user=user,project=project)
        return total
        
    def total_per_user(self, user):
        total = expence.objects.filter(user=user).aggregate(Sum('amount'))['amount__sum']
        if total is None : total = 0
        return total
    def total_per_user_project(self, user, project):
        total = expence.objects.filter(user=user, project=project).aggregate(Sum('amount'))['amount__sum']
        if total is None : total = 0
        return total
    def total_last_7_days(self, user):
        total = expence.objects.filter(user=user, pub_date= datetime.now()-timedelta(days=7)).aggregate(Sum('amount'))['amount__sum']
        if total is None : total = 0
        return total
    def Category_expence(self, project):
        a = expence.objects.filter(project=project, category_pay='a').aggregate(Sum('amount'))['amount__sum']
        b = expence.objects.filter(project=project, category_pay='b').aggregate(Sum('amount'))['amount__sum']
        c = expence.objects.filter(project=project, category_pay='c').aggregate(Sum('amount'))['amount__sum']
        d = expence.objects.filter(project=project, category_pay='d').aggregate(Sum('amount'))['amount__sum']
        e = expence.objects.filter(project=project, category_pay='e').aggregate(Sum('amount'))['amount__sum']
        f = expence.objects.filter(project=project, category_pay='f').aggregate(Sum('amount'))['amount__sum']
        g = expence.objects.filter(project=project, category_pay='g').aggregate(Sum('amount'))['amount__sum']
        i = expence.objects.filter(project=project, category_pay='i').aggregate(Sum('amount'))['amount__sum']
        j = expence.objects.filter(project=project, category_pay='j').aggregate(Sum('amount'))['amount__sum']
        k = expence.objects.filter(project=project, category_pay='k').aggregate(Sum('amount'))['amount__sum']
        l = expence.objects.filter(project=project, category_pay='l').aggregate(Sum('amount'))['amount__sum']
        m = expence.objects.filter(project=project, category_pay='m').aggregate(Sum('amount'))['amount__sum']
        if a is None : a= 0
        if b is None : b= 0
        if c is None : c= 0
        if d is None : d= 0
        if e is None : e= 0
        if f is None : f= 0
        if g is None : g= 0
        if k is None : k= 0
        if i is None : i= 0
        if j is None : j= 0
        if l is None : l= 0
        if m is None : m= 0


        return j , a+b ,g+i,f, c+d, e, k, m+l

        
class incomeManager(models.Manager):
    def total(self, project):
        total = income.objects.filter(project=project).aggregate(Sum('amount'))['amount__sum']
        if total is None : total = 0
        return total
    def total_per_user(self, user):
        total = income.objects.filter(user=user).aggregate(Sum('amount'))['amount__sum']
        if total is None : total = 0
        return total
    def total_per_user_project(self, user, project):
        total = income.objects.filter(user=user, project=project).aggregate(Sum('amount'))['amount__sum']
        if total is None : total = 0
        return total

class Managera(models.Manager):

    def is_member_of(self, user):
        is_member = ProjectModel.objects.filter(Members=user)
        if is_member.count() != 0:
            return True
        else:
            return False

    def is_member_of_project(self, user , id):
        is_member = ProjectModel.objects.filter(Members=user ,id = id)
        if is_member.count() != 0:
            return True
        else:
            return False

    def is_manager(self, user):
        is_manager =ProjectModel.objects.filter(Manager=user)
        if is_manager.count() != 0:
            return True
        else:
            return False
            
    def is_manager_project(self, user, id):
        is_managera =ProjectModel.objects.filter(Manager=user, id = id)
        if is_managera.count() != 0:
            return True
        else:
            return False

    def is_user(self, number):
        is_user = User.objects.filter(username=number)
        print(is_user)

        if is_user.count() != 0 :
            return True
        else :
            return False
    def project_count(self, user):
        proj_count = ProjectModel.objects.filter(Manager=user).count()+ProjectModel.objects.filter(Members=user).count()
        return proj_count
    




class ProjectModel(models.Model):
    METHOD_CHOICE = (
        ('a','در حال انجام'),
        ('b','پایان یافته'),
    )

    name= models.CharField(max_length=100,verbose_name="نام پروژه") 
    zirbana = models.IntegerField(verbose_name="مساحت زیر بنا متر مربع")
    tedad_tabaqat = models.IntegerField(verbose_name="تعداد طبقات پروژه")
    address = models.CharField(max_length=150 ,blank=True, null=True , verbose_name="آددرس پروژه")
    Members = models.ManyToManyField(User, related_name='member',verbose_name="انتخاب شرکا", blank=True)
    Manager = models.ForeignKey(User,related_name='manager' ,on_delete=models.CASCADE, verbose_name="مدیر پروژه")
    description = models.TextField(max_length=400 , verbose_name="توضیحات پروژه",blank=True)
    project_status = models.CharField(max_length=1,choices=METHOD_CHOICE, verbose_name="وضعیت پروژه" )
    created_date = models.DateField(auto_now_add=True, verbose_name= "تاریخ ایجاد پروژه")
    
    objects = Managera()

    class Meta :
        verbose_name = "پروژه عمرانی"
        verbose_name_plural= "پروژه های عمرانی"
        
    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name
    def jpub_date(self):
        return jalali_converter(self.created_date)

class income(models.Model):
    METHOD_CHOICES = (
        ('n', 'نقد'),
        ('c','چک'),
    )
    CATEGORY_CHOICES = (
        ('a','تامین مالی از مالک'),
        ('b','فروش آهن آلات'),
        ('c','فروش ملک'),
        ('d','سایر'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, verbose_name="هزینه شده توسط ")
    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE, verbose_name="پروژه مربوطه")
    title = models.CharField(max_length=200,verbose_name="عنوان هزینه کرد")
    amount = models.BigIntegerField(verbose_name="مقدار هزینه")
    description = models.TextField(max_length=200, blank=True, null=True,verbose_name="توضیحات")
    pay_mehod = models.CharField(max_length=1, choices=METHOD_CHOICES,verbose_name="شیوه پرداخت")
    category_pay = models.CharField(max_length=1, choices=CATEGORY_CHOICES, verbose_name="از کدام منبع درآمد داشتید")
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ انتشار")

    objects = incomeManager()

    class Meta :
        verbose_name = "درآمد"
        verbose_name_plural= "درآمد ها"
        
    def __str__(self):
        return "{} - {}".format(self.title,self.amount)
    def __unicode__(self):
        return "{} - {}".format(self.title,self.amount)

    def jpub_date(self):
        return jalali_converter(self.pub_date)


class expence(models.Model):
    METHOD_CHOICES = (
        ('n', 'نقد'),
        ('c','چک'),
    )
    CATEGORY_CHOICE = (
        ('a','صدور پروانه'),
        ('b','شهرداری'),
        ('c','آرماتور بند'),
        ('d','شرکت بتن'),
        ('e','آهن آلات'),
        ('f','تاسیسات'),
        ('g','مصالح'),
        ('i','دستمزد کارگر بنا'),
        ('j','تخریب'),
        ('k','آب و برق و گاز'),
        ('l','کرایه تجهیزات'),
        ('m','متفرقه'),

    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, verbose_name="هزینه شده توسط ")
    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE, verbose_name="پروژه مربوطه")
    title = models.CharField(max_length=200,verbose_name="عنوان")
    amount = models.BigIntegerField(verbose_name="مقدار هزینه کرد به تومان")
    description = models.TextField(max_length=200, blank=True, null=True,verbose_name="توضیحات")
    pay_mehod = models.CharField(max_length=1, choices=METHOD_CHOICES,verbose_name="شیوه پرداخت")
    category_pay = models.CharField(max_length=1, choices=CATEGORY_CHOICE, verbose_name="در کدام شاخه هزینه کردید")
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ انتشار")

    objects = expenceManager()

    class Meta :
        verbose_name = "هزینه کرد"
        verbose_name_plural= " هزینه کرد ها"
    

    def __str__(self):
        return "{} - {}".format(self.title,self.amount)


    def __unicode__(self):
        return "{} - {}".format(self.title,self.amount)

    def jpub_date(self):
        return jalali_converter(self.pub_date)
