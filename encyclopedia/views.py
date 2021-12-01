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
        searched = request.POST["searched"].lower()

        query_display = []
        for page in util.list_entries():
            if searched == page:
                return entry(request, page)
            elif searched in page:
                query_display.append(page)

        return render(request, "encyclopedia/search_entries.html", {
            "searched": searched,
            "queries": query_display
        })
    
    else:
        return render(request, "encyclopedia/search_entries.html")