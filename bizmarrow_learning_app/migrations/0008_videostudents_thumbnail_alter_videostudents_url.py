# Generated by Django 4.2.7 on 2023-12-19 14:28

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('bizmarrow_learning_app', '0007_alter_videostudents_student_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='videostudents',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to='media/thumbnail'),
        ),
        migrations.AlterField(
            model_name='videostudents',
            name='url',
            field=embed_video.fields.EmbedVideoField(),
        ),
    ]
