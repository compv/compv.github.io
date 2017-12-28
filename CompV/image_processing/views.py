from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import ImagesDatasets
from django.shortcuts import render
from django.contrib.auth.forms import User
from image_processing.forms import RegistrationForm
from django.shortcuts import redirect


def index(request):
    return render(request,'image_processing/index.html')



def upload_and_image_processing(request):
    html = "<html><body> now it is True image processing page</bidy></html>"
    return HttpResponse(html)



def datasets(request):
    latest_datasets_list = ImagesDatasets.objects.order_by('-creation_date')[:10]
    context = {'latest_dataset_list':latest_datasets_list}
    return render(request, 'image_processing/datasets.html', context)


# зробити виклик помилки 404, якщо датасeт не існує
def dataset_detail(request, dataset_id):
    dataset = get_object_or_404(ImagesDatasets, pk=dataset_id)
    return render(request, 'image_processing/dataset detail.html', {'dataset':dataset})


def registration(request):
    return render(request,'image_processing/registration.html')




def registration(request):

    if (request.method == "POST"):
        form = RegistrationForm(request.POST)

        if (form.is_valid()):
            user = form.save()
            user.save()
            return render(request, 'image_processing/')
    else:
        form = RegistrationForm()

    return render(request, 'image_processing/registration.html', {'form': form})
















