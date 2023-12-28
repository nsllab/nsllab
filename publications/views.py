from django.shortcuts import render
from .models import Journal
from .choices import JOURNAL_STATUS, JOURNAL_TYPE

# Create your views here.
def journals(request):
    # query = request.GET.get('q')
    # print(f"QUery ########### {query}")
    journals = Journal.objects.order_by('-write_date')
    search = request.GET
    
    if 'title' in search:
        title = search['title']
        if title:
            journals = journals.filter(title__icontains=title)

    if 'year' in search:
        year = search['year']
        if year:
            journals = journals.filter(write_date__icontains=year)


    if 'journal_type' in search:
        journal_type = search['journal_type']
        if journal_type:
            journals = journals.filter(journal_type__iexact=journal_type)

    if 'status' in search:
        status = search['status']
        if status:
            journals = journals.filter(status__iexact=status)

    # if query:
    #     journals = journals.filter(
    #         Q(title__icontains=query) | Q(write_date__icontains=query)
    #     )

    context = {
        'journals': journals,
        'journal_type': JOURNAL_TYPE,
        'status': JOURNAL_STATUS,
    }
    return render(request, 'publications/journals/journals.html', context)