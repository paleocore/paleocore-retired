from lgrp.models import *
from difflib import SequenceMatcher
from itertools import permutations


def match_taxon(biology_object):
    """
    find taxon objects from item_scientific_name
    Return: (True/False, match_count, match_list)
    """
    # match, match_count, match_list = (False, 0, None)
    match_list = Taxon.objects.filter(name=biology_object.item_scientific_name)
    if len(match_list) == 1:  # one match
        result_tuple = (True, 1, match_list)
    else:
        result_tuple = (False, len(match_list), match_list)
    return result_tuple


def match_element(biology_object):
    """
    find anatomical element from string in item_description. Returns a result tuple. The first element is true
    only if there is one and only one match
    :param biology_object:
    :return: (True/False, match_count, match_list)
    """
    match, match_count, match_list = (False, 0, None)
    element_list = [e[1] for e in LGRP_ELEMENT_CHOICES]
    description = biology_object.item_description
    if description.lower() in element_list:
        match = True
        match_count = 1
        match_list = description
    result = (match, match_count, match_list)
    return result


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


def similar(t):
    a, b = t
    return SequenceMatcher(None, a, b).ratio()


def get_similar_taxa():
    """
    Get a list of all pairwise permutations of taxa sorted according to similarity
    Useful for detecting duplicate and near-duplicate taxonomic entries
    :return: list of 2-tuples ordered most similar to least
    """
    taxa = Taxon.objects.all()
    taxon_name_set = set([t.name for t in taxa])
    plist = [pair for pair in permutations(taxon_name_set, 2)]
    return sorted(plist, key=similar, reverse=True)


def prune_species():
    """
    Function to remove unused species
    :return:
    """
    species = TaxonRank.objects.get(name='Species')
    for taxon in Taxon.objects.all():
        if Biology.objects.filter(taxon=taxon).count() == 0 and taxon.rank == species:
            taxon.delete()

