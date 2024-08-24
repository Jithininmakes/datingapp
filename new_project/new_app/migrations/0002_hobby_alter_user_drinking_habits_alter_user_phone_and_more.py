# Generated by Django 4.2.13 on 2024-08-24 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hobby',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, null=True, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='drinking_habits',
            field=models.CharField(choices=[('', 'Drinking Habit'), ('yes', 'Yes'), ('no', 'No')], default='no', max_length=3),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='smoking_habits',
            field=models.CharField(choices=[('', 'Smoking Habit'), ('yes', 'Yes'), ('no', 'No')], default='no', max_length=3),
        ),
        migrations.AddField(
            model_name='user',
            name='hobbies',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='new_app.hobby'),
        ),
    ]
