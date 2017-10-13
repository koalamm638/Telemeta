# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-03-02 21:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('skosxl', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('alias', models.CharField(blank=True, default='', max_length=100)),
                ('comment', models.TextField(default='')),
            ],
            options={
                'verbose_name': 'author',
            },
        ),
        migrations.CreateModel(
            name='AuthorRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authors', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mcm.Author', verbose_name='author')),
            ],
            options={
                'verbose_name': 'Author role',
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('old_id', models.IntegerField(unique=True)),
                ('text', models.TextField(default='', verbose_name='text')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'event',
            },
        ),
        migrations.CreateModel(
            name='EventEdition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edition', models.IntegerField(blank=True, default=None, null=True)),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mcm.Event')),
            ],
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'event type',
            },
        ),
        migrations.CreateModel(
            name='EventVenue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'event venue',
            },
        ),
        migrations.CreateModel(
            name='GeographicalClassification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'geographical classification',
            },
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'reference',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(blank=True, max_length=200, verbose_name='title')),
                ('text', models.TextField(default='', verbose_name='text')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('document_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mcm.Document')),
                ('code', models.CharField(blank=True, max_length=200, verbose_name='code')),
            ],
            options={
                'verbose_name': 'Document / H - Article',
                'verbose_name_plural': 'Documents - H - Articles',
            },
            bases=('mcm.document',),
        ),
        migrations.CreateModel(
            name='BookThesis',
            fields=[
                ('document_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mcm.Document')),
                ('code', models.CharField(blank=True, max_length=200, verbose_name='code')),
            ],
            options={
                'verbose_name': 'Document / F - Ouvrage & Th\xe8se',
                'verbose_name_plural': 'Documents - F - Ouvrages & Th\xe8ses',
            },
            bases=('mcm.document',),
        ),
        migrations.CreateModel(
            name='Disc',
            fields=[
                ('document_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mcm.Document')),
                ('code', models.CharField(blank=True, max_length=200, verbose_name='code')),
            ],
            options={
                'verbose_name': 'Document / B - Disque',
                'verbose_name_plural': 'Documents - B - Disques',
            },
            bases=('mcm.document',),
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('document_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mcm.Document')),
                ('code', models.CharField(blank=True, max_length=200, verbose_name='code')),
            ],
            options={
                'verbose_name': 'Document / G - Revue',
                'verbose_name_plural': 'Documents - G - Revues',
            },
            bases=('mcm.document',),
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('document_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mcm.Document')),
                ('code', models.CharField(blank=True, max_length=200, verbose_name='code')),
                ('release_date', models.DateField(blank=True, null=True, verbose_name='release date')),
                ('indexation_date', models.DateField(blank=True, null=True, verbose_name='indexation date')),
                ('event_edition', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mcm.EventEdition')),
                ('event_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mcm.EventType')),
                ('event_venue', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mcm.EventVenue')),
                ('geographic_classification', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mcm.GeographicalClassification')),
                ('references', models.ManyToManyField(to='mcm.Reference', verbose_name='reference')),
            ],
            options={
                'verbose_name': 'Document / A - Notice spectacle',
                'verbose_name_plural': 'Documents - A - Notices spectacle',
            },
            bases=('mcm.document',),
        ),
        migrations.CreateModel(
            name='Object',
            fields=[
                ('document_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mcm.Document')),
            ],
            options={
                'verbose_name': 'Document / L - Objet',
                'verbose_name_plural': 'Documents - L-Objets',
            },
            bases=('mcm.document',),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('document_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mcm.Document')),
                ('code', models.CharField(blank=True, max_length=200, verbose_name='code')),
            ],
            options={
                'verbose_name': 'Document / I - Photo',
                'verbose_name_plural': 'Documents - I - Photos',
            },
            bases=('mcm.document',),
        ),
        migrations.CreateModel(
            name='PosterBooklet',
            fields=[
                ('document_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mcm.Document')),
                ('code', models.CharField(blank=True, max_length=200, verbose_name='code')),
            ],
            options={
                'verbose_name': 'Document / J - Affiche-Brochure',
                'verbose_name_plural': 'Documents - J - Affiches-Brochures',
            },
            bases=('mcm.document',),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('document_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mcm.Document')),
                ('code', models.CharField(blank=True, max_length=200, verbose_name='code')),
            ],
            options={
                'verbose_name': 'Document / C - Vid\xe9o DVD&VHS',
                'verbose_name_plural': 'Documents - C - Vid\xe9os DVD&VHS',
            },
            bases=('mcm.document',),
        ),
        migrations.CreateModel(
            name='VideoFile',
            fields=[
                ('document_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mcm.Document')),
                ('code', models.CharField(blank=True, max_length=200, verbose_name='code')),
            ],
            options={
                'verbose_name': 'Document / D - Vid\xe9o en ligne',
                'verbose_name_plural': 'Documents - D - Vid\xe9os en ligne',
            },
            bases=('mcm.document',),
        ),
        migrations.AddField(
            model_name='document',
            name='authors',
            field=models.ManyToManyField(through='mcm.AuthorRole', to='mcm.Author', verbose_name='author'),
        ),
        migrations.AddField(
            model_name='document',
            name='keywords',
            field=models.ManyToManyField(to='skosxl.Concept', verbose_name='keyword'),
        ),
        migrations.AddField(
            model_name='document',
            name='related',
            field=models.ManyToManyField(related_name='_document_related_+', to='mcm.Document', verbose_name='see also'),
        ),
        migrations.AddField(
            model_name='authorrole',
            name='document',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mcm.Document'),
        ),
        migrations.AddField(
            model_name='authorrole',
            name='role',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='mcm.Role'),
        ),
    ]