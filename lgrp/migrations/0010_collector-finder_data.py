# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from lgrp.models import Person, Occurrence
from django.core.exceptions import ObjectDoesNotExist


def update_collector(apps, schema_editor):
    for o in Occurrence.objects.all():
        try:
            p = Person.objects.get(name=o.collector)
            o.collector_person = p
            o.save()
        except ObjectDoesNotExist:
            if o.collector:  # if collector is not None
                p = Person.objects.create(name=o.collector)
                o.collector_person = p
                o.save()
                
                
def update_finder(apps, schema_editor):
    for o in Occurrence.objects.all():
        try:
            p = Person.objects.get(name=o.finder)
            o.finder_person = p
            o.save()
        except ObjectDoesNotExist:
            if o.finder:  # if finder is not None
                p = Person.objects.create(name=o.finder)
                o.finder_person = p
                o.save()


def reverse(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('lgrp', '0009_auto_20171229_1217'),
    ]

    operations = [
        migrations.RunPython(update_collector, reverse_code=reverse),
    ]



