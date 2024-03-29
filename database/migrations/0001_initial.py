# Generated by Django 4.2 on 2024-01-06 06:26

import database.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('number', models.IntegerField(validators=[database.validators.max_integer_validator])),
                ('credit_hours', models.IntegerField(default=4)),
                ('comments', models.TextField(blank=True, null=True)),
                ('offered_annually', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abbreviation', models.CharField(max_length=4)),
                ('name', models.CharField(max_length=256, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ModelSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
                ('obj_type', models.ForeignKey(limit_choices_to=models.Q(models.Q(('app_label', 'database'), ('model', 'course')), models.Q(('app_label', 'database'), ('model', 'student')), models.Q(('app_label', 'database'), ('model', 'preference')), _connector='OR'), on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('year', models.IntegerField(default=2024, validators=[database.validators.year_validator])),
                ('season', models.CharField(choices=[('FL', 'Fall'), ('WI', 'Winter'), ('SP', 'Spring'), ('SU', 'Summer')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_id', models.CharField(max_length=4, unique=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sections+', to='database.course')),
            ],
        ),
        migrations.CreateModel(
            name='WeekdaySet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monday', models.BooleanField(default=False)),
                ('tuesday', models.BooleanField(default=False)),
                ('wednesday', models.BooleanField(default=False)),
                ('thursday', models.BooleanField(default=False)),
                ('friday', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'possible weekdays',
            },
        ),
        migrations.CreateModel(
            name='Timeblock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block_id', models.CharField(max_length=32, unique=True)),
                ('start_hour', models.IntegerField(choices=[(0, '00'), (1, '01'), (2, '02'), (3, '03'), (4, '04'), (5, '05'), (6, '06'), (7, '07'), (8, '08'), (9, '09'), (10, '10'), (11, '11'), (12, '12')])),
                ('start_minutes', models.IntegerField(choices=[(0, '00'), (5, '05'), (10, '10'), (15, '15'), (20, '20'), (25, '25'), (30, '30'), (35, '35'), (40, '40'), (45, '45'), (50, '50'), (55, '55')])),
                ('end_hour', models.IntegerField(choices=[(0, '00'), (1, '01'), (2, '02'), (3, '03'), (4, '04'), (5, '05'), (6, '06'), (7, '07'), (8, '08'), (9, '09'), (10, '10'), (11, '11'), (12, '12')])),
                ('end_minutes', models.IntegerField(choices=[(0, '00'), (5, '05'), (10, '10'), (15, '15'), (20, '20'), (25, '25'), (30, '30'), (35, '35'), (40, '40'), (45, '45'), (50, '50'), (55, '55')])),
                ('weekdays', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timeblocks+', to='database.weekdayset')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='database.department')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.IntegerField(blank=True, null=True, unique=True, validators=[database.validators.student_id_validator])),
                ('class_standing', models.CharField(blank=True, choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior'), ('GR', 'Graduate')], max_length=2, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SetMembership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.modelset')),
            ],
        ),
        migrations.CreateModel(
            name='SectionNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField()),
                ('color', models.CharField(choices=[('#FFFFFF', 'White'), ('#C0C0C0', 'Silver'), ('#808080', 'Gray'), ('#000000', 'Black'), ('#FF0000', 'Red'), ('#800000', 'Maroon'), ('#FFFF00', 'Yellow'), ('#808000', 'Olive'), ('#00FF00', 'Lime'), ('#008000', 'Green'), ('#00FFFF', 'Aqua'), ('#008080', 'Teal'), ('#0000FF', 'Blue'), ('#000080', 'Navy'), ('#FF00FF', 'Fuchsia'), ('#800080', 'Purple')], max_length=7)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='database.section')),
            ],
        ),
        migrations.AddField(
            model_name='section',
            name='other_instructor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sections assisted with+', to='database.teacher'),
        ),
        migrations.AddField(
            model_name='section',
            name='primary_instructor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sections taught+', to='database.teacher'),
        ),
        migrations.AddField(
            model_name='section',
            name='schedule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sections+', to='database.schedule'),
        ),
        migrations.AddField(
            model_name='section',
            name='timeblock',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sections+', to='database.timeblock'),
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approval', models.BooleanField(default=False)),
                ('approving_teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.teacher')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.section')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.student')),
            ],
            options={
                'verbose_name_plural': 'registrations',
            },
        ),
        migrations.CreateModel(
            name='Preference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.BooleanField()),
                ('object_1_id', models.PositiveIntegerField(blank=True, null=True)),
                ('object_2_id', models.PositiveIntegerField(blank=True, null=True)),
                ('object_1_content_type', models.ForeignKey(blank=True, limit_choices_to=models.Q(models.Q(('app_label', 'database'), ('model', 'course')), models.Q(('app_label', 'accounts'), ('model', 'baseuser')), models.Q(('app_label', 'database'), ('model', 'timeblock')), models.Q(('app_label', 'database'), ('model', 'section')), _connector='OR'), null=True, on_delete=django.db.models.deletion.CASCADE, related_name='object_1_content_type', to='contenttypes.contenttype')),
                ('object_2_content_type', models.ForeignKey(blank=True, limit_choices_to=models.Q(models.Q(('app_label', 'database'), ('model', 'course')), models.Q(('app_label', 'accounts'), ('model', 'baseuser')), models.Q(('app_label', 'database'), ('model', 'timeblock')), models.Q(('app_label', 'database'), ('model', 'section')), _connector='OR'), null=True, on_delete=django.db.models.deletion.CASCADE, related_name='object_2_content_type', to='contenttypes.contenttype')),
            ],
            options={
                'verbose_name_plural': 'preferences',
            },
        ),
        migrations.AddField(
            model_name='course',
            name='default_primary_instructor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='database.teacher'),
        ),
        migrations.AddField(
            model_name='course',
            name='default_timeblock',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='database.timeblock'),
        ),
        migrations.AddField(
            model_name='course',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses offered+', to='database.department'),
        ),
    ]
