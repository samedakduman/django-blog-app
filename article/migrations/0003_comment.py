# Generated by Django 3.1 on 2020-08-28 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20200816_1420'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_author', models.CharField(max_length=50, verbose_name='İsim')),
                ('comment_content', models.CharField(max_length=200, verbose_name='Yorum')),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='article.article', verbose_name='Makale')),
            ],
        ),
    ]
