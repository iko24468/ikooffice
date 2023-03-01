from django.db import models
from django.utils import timezone
import datetime

from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name

class Author(models.Model):
    salutation = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    headshot = models.ImageField(upload_to='author_headshots')

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField('Author')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField()

class PhonePrefix(models.Model):
    phone_prefix = models.CharField('ccccccc', max_length=10)

    class Meta:
        verbose_name = 'קידומת'
        verbose_name_plural = 'קידומות'

    def __str__(self):
        return self.phone_prefix + self.id


class MyClient(models.Model):
    PHONE_PREFIX = (
        (None, "קידומת"),
        ("050", "050"),
        ("051", "051"),
        ("052", "052"),
        ("053", "053"),
        ("054", "054"),
        ("055", "055"),
        ("056", "056"),
        ("058", "058"),
        ("059", "059"),
        ("02", "02"),
        ("03", "03"),
        ("04", "04"),
        ("08", "08"),
        ("09", "09")
    )

    GENDER_CHOICES = (
        ("זכר", "זכר"),
        ("נקבה", "נקבה"),
        ("אחר", "אחר")
    )

    KUPA_CHOICES = (
        ("כללית", "כללית"),
        ("מכבי", "מכבי"),
        ("מאוחדת", "מאוחדת"),
        ("לאומית", "לאומית"),
        ("צה\"ל", "צה\"ל"),
    )

    # default_birth_date = (datetime.date.today() - datetime.timedelta(30 * 360)).strftime('%Y-%m-%d')

    id_number = models.CharField('תעודת זהות', max_length=10, unique=True)
    first_name = models.CharField('שם משפחה', max_length=20)
    last_name = models.CharField('שם פרטי', max_length=20)
    # birth_date = models.DateField('תאריך לידה', default=default_birth_date)
    birth_date = models.DateField('תאריך לידה')
    gender = models.CharField(
        'מין',
        max_length=10,
        choices=GENDER_CHOICES,
        default='זכר'
    )
    phone1_prefix = models.CharField('', max_length=3, choices=PHONE_PREFIX, default="050")
    phone1 = models.CharField('טלפון 1', max_length=7)
    phone2_prefix = models.CharField('', max_length=3, choices=PHONE_PREFIX, default="", blank=True)
    phone2 = models.CharField('טלפון 2', max_length=7, default="", blank=True)
    address_city = models.CharField('ישוב', max_length=20, default="")
    address_street = models.CharField('רחוב', max_length=20, default="")
    address_number = models.CharField('מספר', max_length=3, default="")
    address_pob = models.CharField('תא דואר', max_length=7, default="", blank=True)
    address_zip = models.CharField('מיקוד', max_length=7, default="", blank=True)
    mail = models.EmailField('דואר אלקטרוני', default="", blank=True)
    kupa = models.CharField(
        'קופת חולים',
        max_length=10,
        choices=KUPA_CHOICES,
        default='כללית'
        )
    occupation = models.CharField('עיסוק', max_length=20, default="", blank=True)

    class Meta:
        verbose_name = 'לקוח'
        verbose_name_plural = 'לקוחות'

    def __str__(self):
        return self.first_name + " " + self.last_name


class ClientFiles(models.Model):
    FILE_TYPES = (
        (None, "סוג התיק"),
        ("תאונת דרכים", "תאונת דרכים"),
        ("מלל בלבד", "מלל בלבד"),
        ("חבויות", "חבויות"),
        ("פוליסה", "פוליסה"),
        ("רשלנות רפואית", "רשלנות רפואית"),
        ("תלמידים", "תלמידים"),
        ("תעבורה", "תעבורה"),
        ("פלילי", "פלילי"),
        ("פלילי", "פנסיה"),
        ("הגנה", "הגנה"),
        ("אחר", "אחר"),
    )

    FILE_STATUS = (
        (None, "מצב התיק"),
        ("פעיל", "פעיל"),
        ("לא פעיל", "לא פעיל"),
        ("סגור", "סגור"),
    )

    FAKE_USERS = (
        (None, "מטפל"),
        ("נאורי", "נאורי"),
        ("ארז", "ארז"),
        ("מיכאל", "מיכאל"),
        ("מזכירות1", "מזכירות1"),
        ("מזכירות2", "מזכירות2"),
        ("מתמחה", "מתמחה"),
    )

    file_owner = models.ForeignKey(MyClient, on_delete=models.CASCADE)
    file_type = models.CharField(
        'סוג תיק',
        max_length=50,
        choices=FILE_TYPES,
        default='אחר'
    )
    status = models.CharField(
        'מצב התיק',
        max_length=10,
        choices=FILE_STATUS,
        default='פעיל'
    )
    # open_date = models.DateField('תאריך פתיחה', default = datetime.date.today().strftime('YYYY-MM-DD'))
    open_date = models.DateField('תאריך פתיחה', default=timezone.now)
    # interview_date = models.DateField('תאריך ראיון', default=open_date)
    close_date = models.DateField('תאריך סגירה', blank=True, null=True)
    # phase
    superior = models.CharField(
        'מטפל',
        max_length=10,
        choices=FAKE_USERS,
        default='נאורי'
    )
    work_accident = models.BooleanField('תאונת עבודה')

    class Meta:
        verbose_name = 'סוג תיק'
        verbose_name_plural = 'סוגי תיקים'

    def __str__(self):
        return self.file_type


# class TadFile(models.Model):
#     INVOLVMENT = (
#         (None, "מעורבות"),
#         ("נהג", "נהג"),
#         ("נוסע", "נוסע"),
#         ("הולך רגל", "הולך רגל"),
#     )
#
#     file_header = models.CharField('סוג התיק', max_length=50, default="תאונת דרכים")
#     file_owner = models.ForeignKey(MyClient, on_delete=models.CASCADE, null=True)
#     # default_event_date = (datetime.date.today() - datetime.timedelta(360)).strftime('%Y-%m-%d')
#     # event_date = models.DateField('תאריך תאונה', default=default_event_date)
#     event_date = models.DateField('תאריך תאונה')
#     event_place = models.CharField('מקום התאונה', max_length=50)
#     car_number = models.CharField('מספר רכב', max_length=11)
#     insurance_company = models.CharField('מבטחת', max_length=50)
#     # phase
#     evacuation = models.BooleanField('אמבולנס')
#     involvment = models.CharField('מעורבות', max_length=10,  choices=INVOLVMENT, default='מעורבות')
#     circumstances = models.TextField('נסיבות')
#     first_aid = models.TextField('טיפול ראשוני')
#     complaints_and_findings = models.TextField(' תלונות וממצאים')
#     follow_up = models.TextField('המשך טיפול')
#     sick_leave = models.CharField('חופשת מחלה', max_length=20)
#     damage = models.CharField('אסמכתא לנזק', max_length=20)
#     missing_documents = models.TextField('מסמכים חסרים')
#
#     class Meta:
#         verbose_name = 'תיק תד'
#         verbose_name_plural = 'תיקי תד'
#
#     def __str__(self):
#         return self.file_header

class NewTadFile(models.Model):
    FILE_TYPES = (
        (None, "סוג התיק"),
        ("תאונת דרכים", "תאונת דרכים"),
        ("מלל בלבד", "מלל בלבד"),
        ("חבויות", "חבויות"),
        ("פוליסה", "פוליסה"),
        ("רשלנות רפואית", "רשלנות רפואית"),
        ("תלמידים", "תלמידים"),
        ("תעבורה", "תעבורה"),
        ("פלילי", "פלילי"),
        ("פלילי", "פנסיה"),
        ("הגנה", "הגנה"),
        ("אחר", "אחר"),
    )

    FAKE_USERS = (
        (None, "מטפל"),
        ("נאורי", "נאורי"),
        ("ארז", "ארז"),
        ("מיכאל", "מיכאל"),
        ("מזכירות1", "מזכירות1"),
        ("מזכירות2", "מזכירות2"),
        ("מתמחה", "מתמחה"),
    )

    FILE_STATUS = (
        (None, "מצב התיק"),
        ("פעיל", "פעיל"),
        ("לא פעיל", "לא פעיל"),
        ("סגור", "סגור"),
    )

    INVOLVMENT = (
        (None, "מעורבות"),
        ("נהג", "נהג"),
        ("נוסע", "נוסע"),
        ("הולך רגל", "הולך רגל"),
    )

    work_accident = models.BooleanField('תאונת עבודה')
    status = models.CharField(
        'מצב התיק',
        max_length=10,
        choices=FILE_STATUS,
        default='פעיל'
    )
    file_header = models.CharField('סוג התיק', choices = FILE_TYPES, max_length=50, default="תאונת דרכים")
    file_owner = models.ForeignKey(MyClient, on_delete=models.CASCADE)
    # file_header = models.CharField(ClientFiles, on_delete=models.CASCADE)
    # default_event_date = (datetime.date.today() - datetime.timedelta(360)).strftime('%Y-%m-%d')
    # event_date = models.DateField('תאריך תאונה', default=default_event_date)
    close_date = models.DateField('תאריך סגירה', blank=True, null=True)
    open_date = models.DateField('תאריך פתיחה', default=timezone.now)
    event_date = models.DateField('תאריך תאונה')
    event_place = models.CharField('מקום התאונה', max_length=50)
    car_number = models.CharField('מספר רכב', max_length=11)
    insurance_company = models.CharField('מבטחת', max_length=50)
    # phase
    evacuation = models.BooleanField('אמבולנס')
    involvment = models.CharField('מעורבות', max_length=10,  choices=INVOLVMENT, default='מעורבות')
    circumstances = models.TextField('נסיבות')
    first_aid = models.TextField('טיפול ראשוני')
    complaints_and_findings = models.TextField(' תלונות וממצאים')
    follow_up = models.TextField('המשך טיפול')
    sick_leave = models.CharField('חופשת מחלה', max_length=20)
    damage = models.CharField('אסמכתא לנזק', max_length=20)
    missing_documents = models.TextField('מסמכים חסרים')
    superior = models.CharField(
        'מטפל',
        max_length=10,
        choices=FAKE_USERS,
        default='נאורי'
    )

    class Meta:
        verbose_name = 'תיק תד'
        verbose_name_plural = 'תיקי תד'

    def __str__(self):
        return self.file_header