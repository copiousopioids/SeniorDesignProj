from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Layout
from .forms import UploadLayoutForm

# Create your views here.


def index(request):
    recent_layout_list = Layout.objects.order_by('id')[:5]
    context = {'recent_layout_list': recent_layout_list}
    return render(request, 'hotspot/index.html', context)

def layout_detail(request, layout_id):
    return HttpResponse("You're looking at layout %s." % layout_id)

def layout_edit(request, layout_id):
    return HttpResponse("You're editing layout %s." % layout_id)

def layout_add(request):
    if request.method == 'POST':
        form = UploadLayoutForm(request.POST, request.FILES)

        if form.is_valid():
            # layout_title = form.cleaned_data['layout_title']
            # print(layout_title)
            # layout_owner = form.cleaned_data['layout_owner']

            # layout_image = form.cleaned_data['layout_image']
            newlayout = Layout(layout_title = form.cleaned_data['layout_title'],
                               layout_owner = form.cleaned_data['layout_owner'],
                               layout_image=request.FILES['layout_image'])
            newlayout.save()
            # form.save()
            # Redirect to index after POST
            return HttpResponseRedirect('/hotspot')
    else:
        form = UploadLayoutForm()

    recent_layout_list = Layout.objects.order_by('id')[:5]
    context = {'recent_layout_list': recent_layout_list, 'form': form}
    return render(request, 'hotspot/add.html', context)
    # return render(request, 'hotspot/add.html', context = {'form' : form} )

# def upload_layout(request):
#     #handle file upload
#
#
#     return render(request, 'hotspot/add.html', )
