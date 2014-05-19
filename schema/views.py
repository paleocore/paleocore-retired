from django.shortcuts import render_to_response
from django.template import RequestContext
from schema.models import Term, Project, CompareView, TermView, ProjectView, RelateProjectTerms, RelatedTermView, TermCategory#, TermRelationshipView
from django.db.models import Q
from schema.forms import TermViewForm, RelateProjectsForm, RelateTermsForm
from django.forms.models import modelform_factory
from django.db import connection
import json
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django import forms
from fiber.models import ContentItem
from django.contrib.auth import authenticate,login

def standard(request):
    categories = TermCategory.objects.all()
    nCategories = categories.count()
    indices = range(1,nCategories)
    #zip the iterables into one so they can be iterated in tandem in the template
    categories_indices = zip(categories,indices)
    return render_to_response('standard.html',
                                {"categories_indices":categories_indices},
                                RequestContext(request))

def classes(request,category):
    matching_terms = None
    matching_class = None
    try:
        matching_class = TermCategory.objects.get(pk=category)
        matching_terms = Term.objects.filter(category=category,project__exact=5)

    except:
        pass

    return render_to_response("classes.html",
                                {"matching_terms":matching_terms,"matching_class":matching_class},
                                RequestContext(request))

def ontologyTree(request,categoryID=0):

    return render_to_response("ontologyTree.html",
                            {"categoryID":categoryID},
                              RequestContext(request))
# def ontology(request):
#     return render_to_response("ontology.html",
#                             {},
#                               RequestContext(request))
#
# def verticalOntologyTree(request):
#     return render_to_response("verticalOntologyTree.html",
#                             {},
#                               RequestContext(request))
#
def ontologyJSONtree(request):

    response = HttpResponse(mimetype='application/json')

    theParents=[]
    theChildren=[]
    categories = TermCategory.objects.filter(tree_visibility=True)
    for category in categories:
        if category.parent:
            theParents.append(category.parent.id)
            theChildren.append(category.id)
        else:
            theParents.append("NONE")
            theChildren.append(category.id)
    links=zip(theParents,theChildren)
    parents, children = zip(*links)

    def get_nodes(node):
        d = {}

        if get_parent(node) != "NONE":
            d["name"] = TermCategory.objects.get(pk=node).name
            d["URL"] = "/schema/ontology/" + str(node)
            d["categoryID"] =  node
        else:
            try:
                d["name"] = TermCategory.objects.get(pk=node).name
                d["URL"] = "/schema/ontology/" + str(node)
                d["categoryID"] =  node
            except:
                d["name"] = ""
                d["URL"] = "/schema/ontology/"
                d["categoryID"] =  ""


        if get_children(node):
            d['children'] = [get_nodes(child) for child in get_children(node)]
        return d

    def get_children(node):
        return [x[1] for x in links if x[0] == node]

    def get_parent(node):
        try:
            return [x[0] for x in links if x[1] == node][0]
        except:
            return "NONE"



    tree = get_nodes("NONE")

    response.write(json.dumps(tree, indent=4))

    return response


def terms(request):

    #cms_terms_intro = ContentItem.objects.get(name='terms_intro')

    m = CompareView()
    if request.method == 'POST':
        form = TermViewForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            m.showColumns = cd['showColumns']
            m.showProjects = cd['showProjects']
            m.showCategories = cd['showCategories']
            projects = Project.objects.filter(~Q(id=cd['baseProject'].id))
            m.projects = sorted(projects, key=lambda project: project.relatedTermCount(), reverse=True)
            m.baseProject = Project.objects.get(id=cd['baseProject'].id)
            for term in m.baseProject.terms():
                if term.category in m.showCategories:
                    termView = TermView()
                    termView.name = term.name
                    termView.id = term.id
                    termView.definition = term.definition
                    termView.data_type = term.data_type
                    m.termViews.append(termView)
                    for termRelationship in term.term_relationships.all():
                        projectView = ProjectView()
                        projectView.name = termRelationship.related_term.project.name
                        projectView.relatedTermRelationship = termRelationship
                        termView.projectsWithRelatedTerms.append(projectView)
        #request.session['compareView'] = m
    else:
        if request.session.get('compareView'):
            m = request.session['compareView']
            form = TermViewForm(initial = { 'baseProject' : m.baseProject.id, 'showProjects' : m.showProjects, 'showColumns' : m.showColumns} )
        else:
            form = TermViewForm()
    return render_to_response('terms.html', {'m': m, 'form': form}, RequestContext(request))

def termRelationsList(request):
    r = []
    cursor = connection.cursor()
    cursor.execute("SELECT term, term_id, term_project, related_projects FROM term_project_relationship_count_including_unrelated ORDER BY related_projects DESC")
    termDict = fetchAll(cursor)
    for t in termDict:
        rtv = RelatedTermView()
        rtv.term_id = t['term_id']
        rtv.name = t['term']
        rtv.project_name = t['term_project']
        rtv.related_projects = t['related_projects']
        r.append(rtv)

    return render_to_response('term_relationship_list.html', {'r': r}, RequestContext(request))


def fetchAll(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]

def term(request, id):
    t = Term.objects.get(id=id)
    pCount = Project.objects.count()
    return render_to_response('term.html', {'t': t, 'pCount': pCount}, RequestContext(request))

def addTerm(request,referringCategory=None):
    termForm = modelform_factory(Term, exclude=("U"), widgets={"controlled_vocabulary":forms.Textarea})
    if request.method == "POST":
        form = termForm(request.POST)
        if form.is_valid():
            savedCategory = form.cleaned_data["category"].id
            form.save()
            messages.add_message(request, messages.INFO, 'Success! Term was saved.')
            return HttpResponseRedirect("/ontology/" + str(savedCategory))
        else:
            messages.add_message(request, messages.INFO, 'Please correct the errors below.')

    else:
        initialValues={"project":5,"status":2}
        if referringCategory:
            initialValues["category"] = referringCategory
        form = termForm(initial = initialValues)#initial values are Paleocore for project and "standard" for status

    return render_to_response('addTerm.html',
                              {"form":form},
                              RequestContext(request))

def addClass(request):
    termCategoryForm = modelform_factory(TermCategory,exclude=("is_occurrence",),widgets={"description":forms.Textarea})
    if not request.user.is_authenticated():
        return render_to_response('anonymous_user.html',{"referringPageURL":"/addClass/"},RequestContext(request))
    else:
        if request.user.has_perm("paleoschema.add_term"):
            if request.method == "POST":
                form = termCategoryForm(request.POST)
                if form.is_valid():
                    form.save()
                    messages.add_message(request, messages.INFO, 'Success! Class was saved.')
                    return HttpResponseRedirect("/ontology/")
                else:
                    messages.add_message(request, messages.INFO, 'Please correct the errors below.')
            else:
                form = termCategoryForm()
        else:
            return HttpResponseRedirect("/data/drp/nopermission/")


        return render_to_response('addClass.html',
                              {"form":form},
                              RequestContext(request))