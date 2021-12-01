from django.shortcuts import render
from . import util
import markdown2


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):
    entries = util.list_entries()
    if entry in entries:
        text = markdown2.markdown(util.get_entry(entry))
    else:
        text = None

    return render(request, "encyclopedia/entry.html", {
        "title": entry,
        "entries": entries,
        "text": text
    })

def search_entries(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        return render(request, "encyclopedia/search_entries.html", {
            "searched": searched
        })
    
    else:
        return render(request, "encyclopedia/search_entries.html")