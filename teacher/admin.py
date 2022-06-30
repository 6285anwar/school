
from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from .models import teacher
from django import forms
from .models import teacher
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname','photo','email','phone','room','subjects')

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls

    def upload_csv(self, request):

        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]
            
            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'The wrong file type was uploaded')
                return HttpResponseRedirect(request.path_info)
            
            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")

            for x in csv_data:
                fields = x.split(",")
                created = teacher.objects.update_or_create(
                    firstname = fields[0],
                    lastname = fields[1],
                    photo = fields[2],
                    email = fields[3],
                    phone = fields[4],
                    room = fields[5],
                    subject = fields[6],
                    
                    )
            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "dashboard.html", data)

admin.site.register(teacher, TeacherAdmin)
