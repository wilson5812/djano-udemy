# Generated by Django 5.1 on 2024-08-19 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_tag_project_vote_ratio_project_vote_total_review_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='demo',
            new_name='demo_link',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='sourcelink',
            new_name='source_link',
        ),
        migrations.AddField(
            model_name='project',
            name='featured_image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
    ]