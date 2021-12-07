from django.shortcuts import render
from . import util
import markdown2
from django.urls import reverse
from django.http import HttpResponseRedirect


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):
    if util.get_entry(entry):
        return render(request, "encyclopedia/entry.html", {
            "text": markdown2.markdown(util.get_entry(entry)),
            "title": entry
        })
    else:
        return render(request, "encyclopedia/notfound.html")

def search(request): 
    if request.method == "POST":
        searched = request.POST['q']

        if util.get_entry(searched):
            return entry(request, searched)
        else:
            list_entries = util.list_entries()
            search_results = []

            for item in list_entries:
                if searched in item:
                    search_results.append(item)

            return render(request, 'encyclopedia/search.html',
            {'searched': searched, 'list': search_results})
    else:
        return render(request, 'encyclopedia/search.html',
        {})


'''
def search(request, ...)
    if util.get_entry(entry):
        return render(request, "encyclopedia/entry.html", {
            "text": markdown2.markdown(util.get_entry(entry)),
            "title": entry
        })
    elif entry in util.list_entries
        return render(request, "pagina met overeenkomende resultan")
    else entry:
    nope not found
'''