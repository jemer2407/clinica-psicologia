from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import EmailMessage
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from .models import Subscriber
from .forms import SuscriberForm, EmailMarketingForm

# Create your views here.

# vista pública para suscribirse a la newsletter
class SubscriberCreateView(SuccessMessageMixin, CreateView):
    model = Subscriber
    form_class = SuscriberForm
    template_name = 'emailmarketing/subscriber_form.html'
    success_message = "Gracias por suscribirte a nuestra newsletter"
    success_url = reverse_lazy('subscriber-create')


# vista privada para listar los suscritores a la newsletter
@method_decorator(staff_member_required, name='dispatch')
class SubscriberListView(ListView):
    model = Subscriber
    template_name = 'emailmarketing/subscribers_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de suscriptores'
        return context

# vista para crear suscriptores desde login
# vista privada para suscribirse a la newsletter
@method_decorator(staff_member_required, name='dispatch')
class LoginSubscriberCreateView(CreateView):
    model = Subscriber
    form_class = SuscriberForm
    template_name = 'emailmarketing/subscriber_maintenance_form.html'
    success_url = reverse_lazy('subscribers-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Suscriptor'
        return context


# vista para editar un paciente
@method_decorator(staff_member_required, name='dispatch')
class SubscriberUpdateView(UpdateView):
    model = Subscriber
    form_class = SuscriberForm
    template_name = 'emailmarketing/subscriber_form.html'
    success_url = reverse_lazy('subscribers-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Suscriptor'
        return context

# vista para eliminar un paciente
@method_decorator(staff_member_required, name='dispatch')
class SubscriberDeleteView(DeleteView):
    model = Subscriber
    template_name = 'emailmarketing/subscriber_confirm_delete.html'
    success_url = reverse_lazy('subscribers-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Suscriptor'
        return context

# vista para la campaña de email marketing
@method_decorator(staff_member_required, name='dispatch')
def emailMarketing(request):

    title = 'Campaña Email Marketing'
    contact_form = EmailMarketingForm()

    if request.method == 'POST':
        contact_form = EmailMarketingForm(data=request.POST)
        if contact_form.is_valid():
            subject = request.POST.get('subject', '')
            message = request.POST.get('message', '')
            
            # obtenemos los emails de todos los suscriptores

            subscribers = Subscriber.objects.all()
            
            
            # Enviamos el correo y redireccionamos

            for subscriber in subscribers:

                email = EmailMessage(
                    "Clínica Psicología: Campaña de Email Marketing",
                    "Asunto {} \n\nEscribió:\n\n{}".format(subject, message),
                    "no-contestar@clinica-psicologia.com",
                    [subscriber.email],
                    #reply_to=[subscriber.email]
                )
                try:
                    email.send()
                    # Todo ha ido bien y rediccionamos a ok
                    #return redirect(reverse('campaign-email-form') + "?ok")
                except:
                    # algo no ha ido bien y rediccionamos a FAIL
                    
                    return redirect(reverse('subscribers-list') + "?fail")
            return redirect(reverse('subscribers-list') + "?ok")
        
    return render(request, 'emailmarketing/send_email_everyone.html', {
        'title': title,
        'form': contact_form
    })
    


