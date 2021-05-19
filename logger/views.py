from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Custom_Org
from .forms import District_Form, School_Form, UploadFileForm


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return HttpResponseRedirect('/success/url/')
    else:
        form = ModelFormWithFileField()
    return render(request, 'upload.html', {'form': form})


def index(request):
    latest_org = Custom_Org.objects.order_by('-name')[:5]
    context = {
        'latest_org': latest_org,
    }
    return render(request, 'logger/index.html', context)


def org_detail(request, Custom_Org_id):
    org = get_object_or_404(Custom_Org, pk=Custom_Org_id)
    return render(request, 'logger/org_detail.html', {'org': org})


# @login_required
def district_view(request):
    form = Custom_Org(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('home_view'))
    else:
        context = {
            'form': form
        }
    return render(request, 'district.html', context)

def district_detail(request, Custom_Org_id):
    response = "You're looking at district %s."
    return HttpResponse(response % Custom_Org_id)

# Junk view assignment until I can replace it with a proper menu
# @login_required
def home_view(request):
    return render(request, "home.html", {})
