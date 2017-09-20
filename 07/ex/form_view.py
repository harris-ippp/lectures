from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView  
from .forms import InputForm

def form(request):

    state = request.GET.get('state', 'PA') # PA = default
    params = {'form_action' : reverse_lazy('myapp:form'), 
              'form_method' : 'get',
              'form' : InputForm({'state' : state}),
              'state' : STATES_DICT[state]}

    return render(request, 'form.html', params)

