# Generated by Django 4.1.3 on 2023-02-23 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snslaw', '0006_alter_newtadfile_file_header'),
    ]

    operations = [
        migrations.AddField(
            model_name='newtadfile',
            name='superior',
            field=models.CharField(choices=[(None, 'מטפל'), ('נאורי', 'נאורי'), ('ארז', 'ארז'), ('מיכאל', 'מיכאל'), ('מזכירות1', 'מזכירות1'), ('מזכירות2', 'מזכירות2'), ('מתמחה', 'מתמחה')], default='נאורי', max_length=10, verbose_name='מטפל'),
        ),
        migrations.AlterField(
            model_name='newtadfile',
            name='file_header',
            field=models.CharField(choices=[(None, 'סוג התיק'), ('תאונת דרכים', 'תאונת דרכים'), ('מלל בלבד', 'מלל בלבד'), ('חבויות', 'חבויות'), ('פוליסה', 'פוליסה'), ('רשלנות רפואית', 'רשלנות רפואית'), ('תלמידים', 'תלמידים'), ('תעבורה', 'תעבורה'), ('פלילי', 'פלילי'), ('פלילי', 'פנסיה'), ('הגנה', 'הגנה'), ('אחר', 'אחר')], default='תאונת דרכים', max_length=50, verbose_name='סוג התיק'),
        ),
    ]
