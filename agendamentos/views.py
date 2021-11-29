from django.db.models.query import EmptyQuerySet
from django.shortcuts import (render, redirect, get_object_or_404, HttpResponseRedirect)
from django.http.response import Http404, HttpResponse, HttpResponseNotFound
from django.views import generic
from agendamentos.forms import AgendamentosForm
from .models import Agendamento, AgendamentosFuncionarios, Funcionario
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import date, datetime

class AgendamentoListView(ListView):
    paginate_by = 1
    model = Agendamento

def home1(request):
    List = Agendamento.objects.all()
    if request.session.get('usuario'):
        pass
        pass
        return render(request, 'home.html', {'List': List})
    else:
        return redirect('/auth/login/?status=2')

def home(request):
    if request.session.get('usuario'):
        request_usuario = request.session.get('usuario')
        dados_funcionario = Funcionario.objects.filter(id=request_usuario)
        lista_agendamento = Agendamento.objects.filter(funcionario_cpf=request_usuario).order_by('data')
        paginator = Paginator(lista_agendamento, 1) # Show 1 contacts per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {'page_obj': page_obj, 'lista_agendamento': lista_agendamento, 'dados_funcionario': dados_funcionario,}
        if dados_funcionario[0].tipo == 'motorista':
            request.session['usuario'] = dados_funcionario[0].id
            return redirect('/home/itinerario/')
        return render(request, 'agendamentos/home.html', context)
    else:
        return redirect('/auth/login/?status=2')

def home3(request):
    cpf = request.session['usuario']
    return HttpResponse (cpf)

class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = Funcionario
    template_name ='home.html'
    paginate_by = 1

    def get_queryset(self):
        return Funcionario.objects.filter(cpf='22126395898')

def excluir(request):
    idagendaform = request.POST.get('idagendaform')
    dataform = request.POST.get('dataform')
    reservaform = request.POST.get('reservaform')
    if request.session.get('usuario'):
        request_usuario = request.session.get('usuario')
        dados_funcionario = Funcionario.objects.filter(id=request_usuario)
        lista_agendamento = Agendamento.objects.filter(funcionario_cpf=request_usuario).order_by('data')
        paginator = Paginator(lista_agendamento, 1) # Show 1 contacts per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        if idagendaform is not None:
            i = Agendamento.objects.get(id=idagendaform)
            i.reserva = reservaform
            i.delete()
            #existe = Agendamento.objects.filter(funcionario_cpf=request_usuario)
            #if existe:
            #    return redirect('/home/modificar')
            #else:
            return redirect('/home/')
        if lista_agendamento:
            return render(request, 'agendamentos/excluir.html', {'page_obj': page_obj, 'lista_agendamento': lista_agendamento, 'dados_funcionario': dados_funcionario,})
        else:
            return redirect('/home/')
    else:
        return redirect('/auth/login/?status=2')


def agendar1(request):
    if request.session.get('usuario'):
        request_usuario = request.session.get('usuario')
        dataform = request.POST.get('dataform')
        reservaform = request.POST.get('reservaform')
        dados_funcionario = Funcionario.objects.filter(id=request_usuario)
        status = request.GET.get('status')
        return render(request, 'agendamentos/agendar.html', {'dados_funcionario': dados_funcionario, 'status': status})
    else:
        return redirect('/auth/login/?status=2')

def agendar(request):
    if request.session.get('usuario'):
        request_usuario = request.session.get('usuario')
        dataform = request.POST.get('dataform')
        reservaform = request.POST.get('reservaform')
        cpf = Funcionario.objects.get(id=request_usuario)
        dados_funcionario = Funcionario.objects.filter(id=request_usuario)
        status = request.GET.get('status')
        if dataform is not None:
            agenda = Agendamento(funcionario_cpf = cpf,
                               data = dataform,
                            reserva = reservaform)
            agenda.save()
            return redirect('/home/agendar/?status=0')
        else:
            return render(request, 'agendamentos/agendar.html', {'dados_funcionario': dados_funcionario, 'status': status})
    else:
        return redirect('/auth/login/?status=2')


def agenda(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["dataset"] = Agendamento.objects.all()
         
    return render(request, "list_view.html", context)

def detail_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["data"] = Agendamento.objects.get(id = id)
         
    return render(request, "detail_view.html", context)

def update_view(request, id):
    if request.session.get('usuario'):
        # dictionary for initial data with
        # field names as keys
        context ={}
 
        # fetch the object related to passed id
        obj = get_object_or_404(Agendamento, id = id)
 
        # pass the object as instance in form
        form = AgendamentosForm(request.POST or None, instance = obj)
 
        # save the data from the form and
        # redirect to detail_view
        id_usuario_logado = request.session.get('usuario')
        dono_agendamento = Agendamento.objects.filter(id=id).filter(funcionario_cpf=id_usuario_logado)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/home/"+id+"/update")
 
        # add form dictionary to context
        context["form"] = form

        if len(dono_agendamento) > 0:
            return render(request, "update_view.html", context)
        else:
            return HttpResponseNotFound('<h1>Page not found</h1>')
    else:
        return redirect('/auth/login/?status=2')

def list_view(request):
    # dictionary for initial data with
    # field names as keys
    today = date.today()
    context ={}
 
    # add the dictionary during initialization
    #context["dataset"] = Agendamento.objects.filter(data=today).order_by('funcionario_cpf')
    lista_agendamento = Agendamento.objects.filter(data=today).order_by('funcionario_cpf')
    dados_funcionario = Funcionario.objects.filter(linha=1)
    hoje = datetime.today().strftime('%d/%m/%Y')
    context = {'lista_agendamento': lista_agendamento, 'dados_funcionario': dados_funcionario, 'hoje' : hoje}
    return render(request, "list_view.html", context)

def itinerario(request):
    if request.session.get('usuario'):
        request_usuario = request.session.get('usuario')
        hoje = datetime.today().strftime('%Y-%m-%d')
        dados_funcionario = Funcionario.objects.filter(id=request_usuario)
        lista_agendamento = Agendamento.objects.filter(data=hoje).order_by('data')
        paginator = Paginator(lista_agendamento, 1) # Show 1 contacts per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {'page_obj': page_obj, 'lista_agendamento': lista_agendamento, 'dados_funcionario': dados_funcionario,}
        return render(request, 'agendamentos/itinerario.html', context)
    else:
        return redirect('/auth/login/?status=2')


    cpf = request.POST.get('cpf')
    senha = request.POST.get('senha')
    senha = hashlib.sha256(senha.encode()).hexdigest() 
    usuarios = Funcionario.objects.filter(cpf = cpf).filter(senha = senha)
    if usuarios[0].tipo == 'motorista':
        request.session['usuario'] = usuarios[0].id
        return redirect('/home/itinerario/')
    if len(usuarios) == 0:
        return redirect('/auth/login/?status=1')
    elif len(usuarios) > 0:
        request.session['usuario'] = usuarios[0].id
        return redirect('/home/')