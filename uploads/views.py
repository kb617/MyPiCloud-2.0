import os
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from uploads.models import Document
from uploads.forms import DocumentForm


def home(request):
    documents = Document.objects.all()
    return render(request, 'uploads/home.html', { 'documents': documents })


# def simple_upload(request):
#     if request.method == 'POST' and request.FILES['myfile']:
#         myfile = request.FILES['myfile']
#         fs = FileSystemStorage()
#         filename = fs.save(myfile.name, myfile)
#         uploaded_file_url = fs.url(filename)
#         return render(request, 'uploads/simple_upload.html', {
#             'uploaded_file_url': uploaded_file_url
#         })
#     return render(request, 'uploads/simple_upload.html')


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'uploads/model_form_upload.html', {'form': form})


def delete_document(request, doc_id):
    try:
        doc = Document.objects.get(pk=doc_id)
        doc.delete()
        os.remove(os.path.join(settings.MEDIA_ROOT, doc.document.name))
    except Document.DoesNotExist:
        pass
    return redirect('home')
