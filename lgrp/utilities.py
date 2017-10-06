from lgrp.models import *


def match_taxon(biology_object):
    """
    find taxon objects from item_scientific_name
    Return: (True/False, match_count, match_list)
    """
    match_list = Taxon.objects.filter(name=biology_object.item_scientific_name)
    if len(match_list) == 1:  # one match
        result_tuple = (True, 1, match_list)
    else:
        result_tuple = (False, len(match_list), match_list)
    return result_tuple


def update_taxa():
    bios = Biology.objects.all()
    bios2fix = bios.filter(taxon__name='Life').exclude(item_scientific_name=None)
    for bio in bios2fix:
        if bio.item_scientific_name == 'Mammal':
            bio.item_scientific_name = 'Mammalia'
            bio.taxon = Taxon.objects.get(name='Mammalia')
            print 'matching mammal for {}'.format(bio)
        elif bio.item_scientific_name == 'Hippopotomidae':
            bio.item_scientific_name = 'Hippopotamidae'
            bio.taxon = Taxon.objects.get(name='Hippopotamidae')
            print 'matching hippo for {}'.format(bio)
        elif bio.item_scientific_name == 'Primate':
            bio.item_scientific_name = 'Primates'
            bio.taxon = Taxon.objects.get(name='Primates')
            print 'matching primate for {}'.format(bio)
        elif match_taxon(bio)[0]:
            bio.taxon = match_taxon(bio)[2][0]
            print 'found match for {}'.format(bio)
        else:
            print 'no match for {}'.format(bio)
            pass
        bio.save()
