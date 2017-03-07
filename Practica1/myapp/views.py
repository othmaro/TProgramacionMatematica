from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.contrib.auth.models import User
from .forms import registro
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def vista_registro(request):
    if request.method == 'POST':
        form = registro(request.POST)
        if form.is_valid():
            usuario = User.objects.create_user(
            username = form.cleaned_data['user_name'],
            password = form.cleaned_data['password'],
            email = form.cleaned_data['user_name'],
            first_name = form.cleaned_data['your_name'],
            last_name = form.cleaned_data['apellido'],
            )
            template = loader.get_template('myapp/profile.html')
            context ={}
            return HttpResponse(template.render(request))
    else:
        form = registro()
        variables = RequestContext(request, {
        'form': form
    })

    return render_to_response(
    'myapp/registro.html',
    variables,
    )
