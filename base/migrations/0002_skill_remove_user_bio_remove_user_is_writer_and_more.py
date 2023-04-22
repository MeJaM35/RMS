# Generated by Django 4.1.7 on 2023-03-18 13:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_writer',
        ),
        migrations.RemoveField(
            model_name='user',
            name='pronouns',
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('admin', 'admin'), ('recruiter', 'recruiter'), ('applicant', 'applicant')], default='applicant', max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='pfp',
            field=models.ImageField(blank=True, default='user-regular.svg', null=True, upload_to='pfps'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='Recruiter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=50, null=True)),
                ('User', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('logo', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='pfps')),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('activated', models.BooleanField(default=False)),
                ('admin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('recruiters', models.ManyToManyField(blank=True, related_name='org', to='base.recruiter')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=20, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('start_date', models.DateField()),
                ('pay_range', models.IntegerField()),
                ('description', models.TextField(null=True)),
                ('Org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='org', to='base.organization')),
                ('Recruiter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recruiter', to='base.recruiter')),
            ],
        ),
        migrations.CreateModel(
            name='Exp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=20, null=True)),
                ('company', models.CharField(max_length=20, null=True)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('skills', models.ManyToManyField(blank=True, to='base.skill')),
            ],
        ),
        migrations.CreateModel(
            name='Edu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=20, null=True)),
                ('inst', models.CharField(max_length=20, null=True)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('grade', models.IntegerField(blank=True, null=True)),
                ('credentials', models.URLField(blank=True)),
                ('skills', models.ManyToManyField(blank=True, to='base.skill')),
            ],
        ),
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField(blank=True, null=True)),
                ('age', models.IntegerField(null=True)),
                ('pronouns', models.CharField(max_length=10, null=True)),
                ('location', models.CharField(max_length=10, null=True)),
                ('resume', models.FileField(null=True, upload_to='resume')),
                ('User', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='applicant', to=settings.AUTH_USER_MODEL)),
                ('edu', models.ManyToManyField(blank=True, to='base.edu')),
                ('exp', models.ManyToManyField(blank=True, to='base.exp')),
                ('skills', models.ManyToManyField(blank=True, to='base.skill')),
            ],
        ),
    ]
