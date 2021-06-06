from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from .models import Page
from .forms import PageForm
from django.shortcuts import redirect


class StaffRequiredMixin(object):

    """
    Nota: además de staff_member_required, existen los decoradores login_required y permission_required
    """
    
    #El método dispatch permite controlar la petición a una vista sobreescribiéndolo:
    @method_decorator(staff_member_required) #Este decorador con el argumento staff_member_required hará que obligue a estar identificado en las clases en las que pasemos el decorador indicando con "name" el método al que aplica
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)  

# Create your views here.
class PagesListView(ListView):
    model = Page

class PageDetailView(DetailView):
    model = Page

@method_decorator(staff_member_required, name='dispatch')
class PageCreate(CreateView):
    model = Page
    form_class = PageForm
    success_url = reverse_lazy('pages:pages')  

@method_decorator(staff_member_required, name='dispatch')
class PageUpdate(UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class PageDelete(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')
