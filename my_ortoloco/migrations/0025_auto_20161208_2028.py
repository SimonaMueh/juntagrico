# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-08 19:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    def data_migration(apps, schema_editor):
        Abo = apps.get_model("my_ortoloco", "Abo")
        Loco = apps.get_model("my_ortoloco", "Loco")
        ExtraAbo = apps.get_model("my_ortoloco", "ExtraAbo")
       
        for loco in Loco.objects.all():
            loco.abo_id=loco.tmp_abo_id
            loco.save()
            
        for extra in ExtraAbo.objects.all():
            extra.main_abo_id=extra.tmp_abo_id
            extra.save()
            
    dependencies = [
        ('my_ortoloco', '0024_auto_20161208_1632'),
    ]

    operations = [
        migrations.RunPython(data_migration),
    ]