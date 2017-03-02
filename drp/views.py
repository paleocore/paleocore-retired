from django.shortcuts import render
from django.views import generic
from projects.models import Project
from django.shortcuts import HttpResponse, render_to_response
from django.db.models.loading import get_model
from django.template import RequestContext
import json
from ast import literal_eval
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

from drp.models import Occurrence, Biology


class DRPSummaryViewGeneric(generic.DetailView):
    template_name = 'drp/project_summary.html'
    context_object_name = 'project'

    def get_object(self):
        return Occurrence.objects.all(paleocore_appname=self.kwargs["pcoreapp"])


def drp_summary_view(request):

    occurrences = Occurrence.objects.all()
    occur_count= occurrences.count()

    collections = Occurrence.objects.filter(basis_of_record__exact='FossilSpecimen')
    coll_count = collections.count()

    observations = Occurrence.objects.filter(basis_of_record__exact='HumanObservation')
    obs_count = observations.count()

    arch_coll = collections.filter(item_type__in=['Artifactual']).count()
    bio_coll = collections.filter(item_type__in=['Faunal', 'Floral']).count()
    geo_coll = collections.filter(item_type__in=['Geological']).count()

    arch_obs = observations.filter(item_type__in=['Artifactual']).count()
    bio_obs = observations.filter(item_type__in=['Faunal', 'Floral']).count()
    geo_obs = observations.filter(item_type__in=['Geological']).count()

    arch_occur = occurrences.filter(item_type__in=['Artifactual']).count()
    bio_occur = occurrences.filter(item_type__in=['Faunal', 'Floral']).count()
    geo_occur = occurrences.filter(item_type__in=['Geological']).count()

    bios = Biology.objects.all()
    dik_bios = bios.filter(collection_code__exact='DIK')
    asb_bios = bios.filter(collection_code__exact='ASB')

    def get_taxon_list(qs):

        class TaxonCount():
            def __init__(self):
                self.name = None
                self.count = 0

        taxon_set = set()
        taxon_dict = {}
        taxon_list = []

        for b in qs:
            fname = b.taxon.full_name()
            if fname not in taxon_set:
                taxon_dict[fname] = 1
            else:
                taxon_dict[fname] += 1
            taxon_set.add(b.taxon.full_name())

        for t in sorted(taxon_set):
            mytaxon = TaxonCount()
            mytaxon.name=t
            mytaxon.count=taxon_dict[t]
            taxon_list.append(mytaxon)
        return taxon_list

    def get_duplicate_barcodes(qs):
        barcode_set = set()
        barcode_duplicates = []
        for r in qs:
            if r in barcode_set:
                barcode_duplicates.append(r)
            else:
                barcode_set.add(r)
        return barcode_duplicates



    collections = occurrences.filter(basis_of_record__exact='FossilSpecimen')
    collections_archaeology = collections.filter(item_type__in=['Artifactual',])
    collections_biology = collections.filter(item_type__in=['Faunal', 'Floral'])
    collections_geology = collections.filter(item_type__in=['Geological',])




    project = get_object_or_404(Project, paleocore_appname='drp')
    return render_to_response('projects/project_summary.html',
                              {"project": project,
                               "occur_count": occur_count,
                               "obs_count": obs_count,
                               "coll_count": coll_count,
                               "arch_coll": arch_coll,
                               "bio_coll": bio_coll,
                               "geo_coll": geo_coll,
                               "arch_obs": arch_obs,
                               "bio_obs": bio_obs,
                               "geo_obs": geo_obs,
                               "arch_occur": arch_occur,
                               "bio_occur": bio_occur,
                               "geo_occur": geo_occur,
                               "taxon_list": get_taxon_list(bios),
                               "dik_taxon_list": get_taxon_list(dik_bios),
                               "asb_taxon_list": get_taxon_list(asb_bios),
                               "barcode_duplicates": get_duplicate_barcodes(occurrences)
                               },
                              context_instance=RequestContext(request))
