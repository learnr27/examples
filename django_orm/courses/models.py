from django.db import models


# Create your models here.
class Test(models.Model):
    # 自增长字段
    Auto = models.AutoField()
    BigAuto = models.BigAutoField()

    # 二进制数据
    Binary = models.BinaryField()

    # 布尔值
    Boolean = models.BooleanField()
    NullBoolean = models.NullBooleanField()

    # 整形
    PositiveSmallInteger = models.PositiveSmallIntegerField(db_column='age')  # 5个字节
    SmallInteger = models.SmallIntegerField(primary_key=False)  # 6个字节
    PositiveInteger = models.PositiveIntegerField()  # 10个字节
    Integer = models.IntegerField(verbose_name='11个字节大小')  # 11个字节
    BigInteger = models.BigIntegerField(unique=True)  # 20个字节

    # 字符串类型
    Char = models.CharField(max_length=100, null=True, blank=True, db_index=True)  # varchar
    Text = models.TextField(help_text='这个是longtext')  # longtext

    # 时间日期类型
    Date = models.DateField(unique_for_date=True, auto_now=True)  # auto_now自动更新时间
    Date_time = models.DateTimeField(editable=False, unique_for_month=True, auto_now_add=True)  # auto_now_add 自动添加插入时间
    Duration = models.DurationField()  # int, Python timedelta实现

    # 浮点型
    Flot = models.FloatField()
    Decimal = models.DecimalField(max_digits=4, decimal_places=2)  # 88.66 99.88

    # 其它字段
    Email = models.EmailField()  # 邮箱
    Image = models.ImageField()
    File = models.FileField()
    FilePath = models.FilePathField()
    URL = models.URLField()
    UUID = models.UUIDField()
    GenericIPAddress = models.GenericIPAddressField()


class A(models.Model):
    onetoone = models.OneToOneField(Test, related_name='one')


class B(models.Model):
    foreign = models.ForeignKey(A)
    foreign = models.ForeignKey(A, on_delete=models.CASCADE)  # 删除级联
    foreign = models.ForeignKey(A, on_delete=models.PROTECT)
    foreign = models.ForeignKey(A, on_delete=models.SET_NULL, null=True, blank=True)  # 删除置空
    foreign = models.ForeignKey(A, on_delete=models.SET_DEFAULT, default=0)
    foreign = models.ForeignKey(A, on_delete=models.DO_NOTHING)
    foreign = models.ForeignKey(A, on_delete=models.SET)


class C(models.Model):
    manytomany = models.ManyToManyField(B)


# 1.所有字段都有的参数
# 2.个别字段才有的参数
# 3.关系型字段的参数

"""
on_delete 当一个被外键关联的对象被删除时，Django将模仿on_delete参数定义的SQL约束执行相应操作
	如下6种操作
	CASCADE：模拟SQL语言中的ON DELETE CASCADE约束，将定义有外键的模型对象同时删除！（该操作为当前Django版本的默认操作！）
	PROTECT:阻止上面的删除操作，但是弹出ProtectedError异常
	SET_NULL：将外键字段设为null，只有当字段设置了null=True时，方可使用该值。
	SET_DEFAULT:将外键字段设为默认值。只有当字段设置了default参数时，方可使用。
	DO_NOTHING：什么也不做。
	SET()：设置为一个传递给SET()的值或者一个回调函数的返回值。注意大小写。
"""
