from django.views.generic import FormView
from django.shortcuts import render_to_response

from .forms import MyForm


class IndexPage(FormView):
    form_class = MyForm
    template_name = "myapp/index.html"

    def form_valid(self, form):
        name = form.cleaned_data['name']
        return render_to_response("myapp/rendered.html", {'name': name})
