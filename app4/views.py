from django.shortcuts import render

# Create your views here.


def jinja_printing_tags(request):
    dict = {'name': 'venkateshwarlu', 'age': 23, 'mobile': 9100}
    return render(request, 'jinja_printing_tags.html', dict)
