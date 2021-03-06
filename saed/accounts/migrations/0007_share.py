# Generated by Django 2.2.6 on 2021-05-12 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20210511_2330'),
    ]

    operations = [
        migrations.CreateModel(
            name='Share',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ ایجاد')),
                ('modified', models.DateTimeField(auto_now=True, null=True, verbose_name='تاریخ تغییر')),
                ('type_of_regulations', models.CharField(choices=[('absorption', 'جذب'), ('promotional', 'ترفیع'), ('grant', 'پژوهانه یا گرنت'), ('right_to_encouragement', 'حق التشویق'), ('status_conversion', 'تبدیل وضعیت')], default='absorption', max_length=200, verbose_name='نوع آیین نامه')),
                ('type_of_articel', models.CharField(choices=[('JCR', 'JCR'), ('SCOPUS', 'SCOPUS'), ('WOS', 'WOS'), ('Scientific_research', 'علمی پژوهشی')], default='JCR', max_length=200, verbose_name='نوع مقاله')),
                ('score_first_quarter', models.IntegerField(blank=True, null=True, verbose_name='امتیاز چارک اول')),
                ('score_second_quarter', models.IntegerField(blank=True, null=True, verbose_name='امتیاز چارک دوم')),
                ('score_third_quarter', models.IntegerField(blank=True, null=True, verbose_name='امتیاز چارک سوم')),
                ('score_fourth_quarter', models.IntegerField(blank=True, null=True, verbose_name='امتیاز چارک چهارم')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
