# Generated by Django 3.2.4 on 2023-11-12 04:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter_name', models.CharField(max_length=255)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ChapterPDF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf_file', models.CharField(max_length=255)),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.chapter')),
            ],
        ),
        migrations.CreateModel(
            name='ChapterVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_file', models.CharField(max_length=255)),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.chapter')),
            ],
        ),
        migrations.RemoveField(
            model_name='file',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='image',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='module',
            name='course',
        ),
        migrations.RemoveField(
            model_name='text',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='video',
            name='owner',
        ),
        migrations.AlterModelOptions(
            name='course',
            options={},
        ),
        migrations.RemoveField(
            model_name='course',
            name='created',
        ),
        migrations.RemoveField(
            model_name='course',
            name='overview',
        ),
        migrations.RemoveField(
            model_name='course',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='course',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='course',
            name='students',
        ),
        migrations.RemoveField(
            model_name='course',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='course',
            name='title',
        ),
        migrations.AddField(
            model_name='course',
            name='course_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='description',
            field=models.CharField(default='Default Course description', max_length=255),
        ),
        migrations.DeleteModel(
            name='Content',
        ),
        migrations.DeleteModel(
            name='File',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.DeleteModel(
            name='Module',
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
        migrations.DeleteModel(
            name='Text',
        ),
        migrations.DeleteModel(
            name='Video',
        ),
        migrations.AddField(
            model_name='chapter',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.course'),
        ),
    ]