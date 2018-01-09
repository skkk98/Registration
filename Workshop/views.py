from django.shortcuts import render
from django.views.generic import View
from .forms import RegisterHere

def index(request):
    return render(request, 'Workshop/registration.html')

class Workshop(View):
    form_class = RegisterHere
    template_name = 'Workshop/registration.html'

    def get(self, request):
        form = self.form_class(None)

        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            workshop = form.save(commit=False)

            name = form.cleaned_data['Name']
            email = form.cleaned_data['Email']
            mobile = form.cleaned_data['Mobile']
            workshops = form.cleaned_data['Workshop']

            workshop.save()
            print('sent')
            return render(request, self.template_name, {'form': form})

        return render(request, self.template_name, {'form': form})
