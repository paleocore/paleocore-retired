from django.shortcuts import render
from .models import Site, Date
from django.contrib.gis.shortcuts import render_to_kml
from django.shortcuts import render_to_response
from .forms import SiteSearch
from django.http import HttpResponse, HttpResponseRedirect
import csv


def home(request):
    sites = Site.objects.all().count
    dates = Date.objects.all().count
    search_result_n = 0
    if request.method == 'GET':
        if request.GET.get('sitename', ''):
            points_to_map = Site.objects.filter(site__exact=request.GET.get('sitename', ''))
            search_result = True
            search_result_n = 1
            form = SiteSearch
            return render(request, 'paleosites_index.html', {'sites': sites, 
                                                             'dates': dates, 
                                                             'map_points': points_to_map,
                                                             'form': form, 'search_result': search_result, 
                                                             'search_result_n': search_result_n, })
        # if request.GET.get('id', ''):
        #     points_to_map = Site.objects.filter(pk=request.GET.get('id', ''))
        #     search_result = True
        #     search_result_n = 1
        #     form = SiteSearch
        #     return render(request, 'paleosites_index.html', {'sites': sites,
        #                                                      'dates': dates,
        #                                                      'map_points': points_to_map,
        #                                                      'form': form, 'search_result': search_result,
        #                                                      'search_result_n': search_result_n, })
        if request.GET.get('download', '') == "sites":
            response = HttpResponse(content_type='text/csv;charset=utf-8')
            response['Content-Disposition'] = 'attachment; filename="Sites.csv"'
            writer = csv.writer(response, dialect='excel')
            writer.writerow(["ID", "Site", "Country", "DataSource", "Latitude", "Longitude", "Altitude", "Notes"])
            for a_site in Site.objects.all():
                if a_site.map_location:
                    longitude = a_site.map_location.x
                    latitude = a_site.map_location.y
                else:
                    longitude = -1
                    latitude = -1
                if a_site.altitude:
                    altitude = a_site.altitude
                else:
                    altitude = -1
                if not(a_site.notes):
                    notes = ""
                else:
                    notes = a_site.notes
                writer.writerow([a_site.id, a_site.site.encode("utf-8"), a_site.country.name.encode("utf-8"),
                                 a_site.data_source, latitude, longitude, altitude, notes.encode("utf-8")])
            return response
        if request.GET.get('download', '') == "dates":
            response = HttpResponse(content_type='text/csv;charset=utf-8')
            response['Content-Disposition'] = 'attachment; filename="Dates.csv"'
            writer = csv.writer(response, dialect='excel')
            writer.writerow(["Site", "Layer", "Industry", "Industry_2", "Industry_3", "Cat_No", "date", "sd_plus",
                             "sd_minus", "sample", "technique", "corrected_date_BP", "plus", "minus",
                             "hominid_remains", "bibliography", "Notes", "intcal09_max", "intcal09_min"])
            for a_date in Date.objects.all():
                if not(a_date.notes):
                    notes = ""
                else:
                    notes = a_date.notes.encode("utf-8")
                if not(a_date.layer):
                    layer = ""
                else:
                    layer = a_date.layer.encode("utf-8")
                if a_date.industry:
                    industry = a_date.industry.encode("utf-8")
                else:
                    industry = ""
                if a_date.industry_2:
                    industry_2 = a_date.industry_2.encode("utf-8")
                else:
                    industry_2 = ""
                if a_date.industry_3:
                    industry_3 = a_date.industry_3.encode("utf-8")
                else:
                    industry_3 = ""
                if not(a_date.hominid_remains):
                    hominid = ""
                else:
                    hominid = a_date.hominid_remains.encode("utf-8")
                if not(a_date.bibliography):
                    bibliography = ""
                else:
                    bibliography = a_date.bibliography.encode("utf-8")
                if not(a_date.sample):
                    sample = ""
                else:
                    sample = a_date.sample.encode("utf-8")
                if not(a_date.cat_no):
                    cat_no = ""
                else:
                    cat_no = a_date.cat_no.encode("utf-8")
                writer.writerow([a_date.site, layer, industry, industry_2, industry_3, cat_no, a_date.date,
                                 a_date.sd_plus, a_date.sd_minus, sample, a_date.technique, a_date.corrected_date_BP,
                                 a_date.plus, a_date.minus, hominid, bibliography, notes,
                                 a_date.intcal09_max, a_date.intcal09_min])
            return response
    if request.method == 'POST':
        form = SiteSearch(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            points_to_map = Site.objects.filter(site__contains=form_data['site_name'])
            search_result = True
            search_result_n = points_to_map.count()
        else:
            points_to_map = Site.objects.all()
            form = SiteSearch
            search_result = False
    else:
        points_to_map = Site.objects.all()
        form = SiteSearch
        search_result = False
        search_result_n = 0
    return render(request, 'paleosites_index.html', {'sites': sites,
                                                     'dates': dates,
                                                     'map_points': points_to_map,
                                                     'form': form,
                                                     'search_result': search_result,
                                                     'search_result_n': search_result_n, })


def all_kml(request):
    locations = Site.objects.kml()
    return render_to_kml("placemarks.kml", {'places' : locations})


def map_page(request):
    lcount = Site.objects.all().count()
    points_to_map = Site.objects.all()
    return render_to_response('map.html', {'location_count' : lcount, 'map_points' : points_to_map})