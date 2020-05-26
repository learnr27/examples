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
    Date = models.DateField(unique_for_date=True, auto_now=True)
    Date_time = models.DateTimeField(editable=False, unique_for_month=True, auto_now_add=True)
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
