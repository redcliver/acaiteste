from django.shortcuts import render
from .models import cliente

# Create your views here.
def novo_cliente(request):
    if request.method == 'POST' and request.POST.get('nome') != None:
        nome = request.POST.get('nome')
        telefone1 = request.POST.get('telefone1')
        telefone2 = request.POST.get('telefone2')        
        cpf = request.POST.get('cpf')
        endereco = request.POST.get('endereco')
        numero = request.POST.get('numero')
        bairro = request.POST.get('bairro')
        referencia = request.POST.get('referencia')
        novo_cliente = cliente(nome=nome, telefone1=telefone1, telefone2=telefone2, cpf=cpf, endereco=endereco, numero=numero, bairro=bairro, referencia=referencia)
        novo_cliente.save()
        msg = nome + " salvo(a) com sucesso."
        clientes = cliente.objects.all().order_by('nome')
        return render(request, 'pedidos/novo_pedido.html', {'title':'Novo Pedido', 'msg':msg, 'clientes':clientes})

    return render(request, 'cliente/novo_cliente.html', {'title':'Novo Cliente'})

def edita_cliente(request):
    clientes = cliente.objects.all().order_by('nome')
    if request.method == 'POST' and request.POST.get('cliente_id') != None:
        cliente_id = request.POST.get('cliente_id')
        cliente_obj = cliente.objects.get(id=cliente_id)
        return render(request, 'cliente/visualiza_cliente.html', {'title':'Edita Cliente', 'cliente_obj':cliente_obj})
    return render(request, 'cliente/edita_cliente.html', {'title':'Edita Cliente', 'clientes':clientes})

def salva_cliente(request):
    if request.method == 'POST' and request.POST.get('nome') != None:
        nome = request.POST.get('nome')
        telefone1 = request.POST.get('telefone1')
        telefone2 = request.POST.get('telefone2')        
        cpf = request.POST.get('cpf')
        endereco = request.POST.get('endereco')
        numero = request.POST.get('numero')
        bairro = request.POST.get('bairro')
        referencia = request.POST.get('referencia')
        estado = request.POST.get('estado')
        cliente_id = request.POST.get('cliente_id')
        cliente_obj = cliente.objects.get(id=cliente_id)
        cliente_obj.nome = nome
        cliente_obj.telefone1 = telefone1
        cliente_obj.telefone2 = telefone2
        cliente_obj.cpf = cpf
        cliente_obj.endereco = endereco
        cliente_obj.numero = numero
        cliente_obj.bairro = bairro
        cliente_obj.referencia = referencia
        cliente_obj.estado = estado
        cliente_obj.save()
        msg = nome + " editado(a) com sucesso."
        return render(request, 'cliente/visualiza_cliente.html', {'title':'Edita Cliente', 'cliente_obj':cliente_obj, 'msg':msg})
    return render(request, 'cliente/edita_cliente.html', {'title':'Edita Cliente'})

def exclui_cliente(request):
    clientes = cliente.objects.filter(estado=1).all().order_by('nome')
    if request.method == 'POST' and request.POST.get('cliente_id') != None:
        cliente_id = request.POST.get('cliente_id')
        cliente_obj = cliente.objects.get(id=cliente_id)
        cliente_obj.estado = 2
        cliente_obj.save()
        msg = cliente_obj.nome + " excluido(a) com sucesso."
        clientes = cliente.objects.filter(estado=1).all().order_by('nome')
        return render(request, 'cliente/edita_cliente.html', {'title':'Edita Cliente', 'clientes':clientes, 'msg':msg})
    return render(request, 'cliente/edita_cliente.html', {'title':'Edita Cliente', 'clientes':clientes})

def dados_cliente(request):
    ativos = cliente.objects.filter(estado=1).count()
    inativos = cliente.objects.filter(estado=2).count()
    return render(request, 'cliente/dados_cliente.html', {'title':'Dados Cliente', 'ativos':ativos, 'inativos':inativos})