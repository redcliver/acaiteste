from django.shortcuts import render
from caixa.models import caixa_geral
from pedidos.models import comanda, itemproduto
from decimal import *
from django.utils import timezone
import datetime
from datetime import datetime
from datetime import timedelta, date

# Create your views here.
def caixa1(request):
    caixa_atual = caixa_geral.objects.latest('id')
    return render(request, 'caixa.html', {'title':'Caixa', 'caixa_atual':caixa_atual})


def extrato(request):
    hoje = datetime.now().strftime('%Y-%m-%d')
    caixas = caixa_geral.objects.filter(data__date=hoje).all()
    dinheiro = 0
    cartao = 0
    saida = 0 
    total_geral = 0
    local = 0
    viagem = 0
    entrega = 0 
    total_pedido = 0
    for a in caixa_geral.objects.filter(data__date=hoje).filter(tipo=1, operacao=1).all():
        dinheiro = dinheiro + a.valor_operacao
    for b in caixa_geral.objects.filter(data__date=hoje).filter(tipo=2, operacao=1).all():
        cartao = cartao + b.valor_operacao
    for c in caixa_geral.objects.filter(data__date=hoje).filter(tipo=3, operacao=1).all():
        cartao = cartao + c.valor_operacao
    for d in caixa_geral.objects.filter(data__date=hoje).filter(operacao=2).all():
        saida = saida + d.valor_operacao
    for d in comanda.objects.filter(data__date=hoje).filter(tipo=1).all():
        local = local + 1
    for e in comanda.objects.filter(data__date=hoje).filter(tipo=2).all():
        viagem = viagem + 1
    for f in comanda.objects.filter(data__date=hoje).filter(tipo=3).all():
        entrega = entrega + 1
    total_geral = cartao + dinheiro
    total_pedido = local + viagem + entrega
    if request.method == 'POST':
        data1 = request.POST.get('data')
        caixas = caixa_geral.objects.filter(data__date=data1)
        dinheiro = 0
        cartao = 0
        saida = 0 
        total_geral = 0
        for a in caixa_geral.objects.filter(data__date=data1).filter(tipo=1, operacao=1).all():
            dinheiro = dinheiro + a.valor_operacao
        for b in caixa_geral.objects.filter(data__date=data1).filter(tipo=2, operacao=1).all():
            cartao = cartao + b.valor_operacao
        for c in caixa_geral.objects.filter(data__date=data1).filter(tipo=3, operacao=1).all():
            cartao = cartao + c.valor_operacao
        for d in caixa_geral.objects.filter(data__date=hoje).filter(operacao=2).all():
            saida = saida + d.valor_operacao
        total_geral = cartao + dinheiro
        return render(request, 'extrato.html', {'title':'Extrato', 'caixas':caixas, 'data':data1, 'total_geral':total_geral, 'dinheiro':dinheiro, 'cartao':cartao, 'saida':saida})    
    return render(request, 'extrato.html', {'title':'Extrato', 'caixas':caixas, 'data':hoje, 'total_geral':total_geral, 'dinheiro':dinheiro, 'cartao':cartao, 'saida':saida, 'local':local, 'viagem':viagem, 'entrega':entrega, 'total_pedido':total_pedido})

def extrato_periodo(request):
    data_inicio = datetime.now() + timezone.timedelta(days=-7)
    data_inicio = data_inicio.strftime('%Y-%m-%d')
    data_fim = datetime.now() + timezone.timedelta(days=1)
    data_fim = data_fim.strftime('%Y-%m-%d')
    caixas = caixa_geral.objects.filter(data__range=(data_inicio,data_fim)).all()
    dinheiro = 0
    cartao = 0
    saida = 0 
    total_geral = 0
    for a in caixa_geral.objects.filter(data__range=(data_inicio,data_fim)).filter(tipo=1, operacao=1).all():
        dinheiro = dinheiro + a.valor_operacao
    for b in caixa_geral.objects.filter(data__range=(data_inicio,data_fim)).filter(tipo=2, operacao=1).all():
        cartao = cartao + b.valor_operacao
    for c in caixa_geral.objects.filter(data__range=(data_inicio,data_fim)).filter(tipo=3, operacao=1).all():
        cartao = cartao + c.valor_operacao
    for d in caixa_geral.objects.filter(data__range=(data_inicio,data_fim)).filter(operacao=2).all():
        saida = saida + d.valor_operacao
    total_geral = cartao + dinheiro
    if request.method == 'POST':
        data_inicio = request.POST.get('data_inicio')
        data_fim = request.POST.get('data_fim')
        caixas = caixa_geral.objects.filter(data__range=(data_inicio,data_fim))
        dinheiro = 0
        cartao = 0
        saida = 0 
        total_geral = 0
        for a in caixa_geral.objects.filter(data__range=(data_inicio,data_fim)).filter(tipo=1, operacao=1).all():
            dinheiro = dinheiro + a.valor_operacao
        for b in caixa_geral.objects.filter(data__range=(data_inicio,data_fim)).filter(tipo=2, operacao=1).all():
            cartao = cartao + b.valor_operacao
        for c in caixa_geral.objects.filter(data__range=(data_inicio,data_fim)).filter(tipo=3, operacao=1).all():
            cartao = cartao + c.valor_operacao
        for d in caixa_geral.objects.filter(data__range=(data_inicio,data_fim)).filter(operacao=2).all():
            saida = saida + d.valor_operacao
        total_geral = cartao + dinheiro
        return render(request, 'extrato_periodo.html', {'title':'Extrato', 'caixas':caixas, 'data_inicio':data_inicio, 'data_fim':data_fim, 'total_geral':total_geral, 'dinheiro':dinheiro, 'cartao':cartao, 'saida':saida})    
    return render(request, 'extrato_periodo.html', {'title':'Extrato', 'caixas':caixas, 'data_inicio':data_inicio, 'data_fim':data_fim, 'total_geral':total_geral, 'dinheiro':dinheiro, 'cartao':cartao, 'saida':saida})

def retirada(request):
    caixa_atual = caixa_geral.objects.latest('id')
    if request.method == 'POST' and request.POST.get('retirada') != None:
        nova_retirada = request.POST.get('retirada')
        motivo = request.POST.get('motivo')
        caixa_atual = caixa_geral.objects.latest('id')
        total_caixa = caixa_atual.total - Decimal(nova_retirada)
        valor_op = Decimal(nova_retirada)
        novo_caixa = caixa_geral(operacao=2, tipo=1, valor_operacao=valor_op, descricao=motivo,id_operacao=caixa_atual.id, total=total_caixa)
        novo_caixa.save()
        caixa_atual = caixa_geral.objects.latest('id')
        msg = "Retirada realizada com sucesso!"
        return render(request, 'home/home.html', {'title':'Home', 'msg':msg})
    return render(request, 'retirada.html', {'title':'Retirada', 'caixa_atual':caixa_atual})

def entrada(request):
    caixa_atual = caixa_geral.objects.latest('id')
    if request.method == 'POST' and request.POST.get('entrada') != None:
        metodo = request.POST.get('metodo')        
        nova_entrada = request.POST.get('entrada')
        motivo = request.POST.get('motivo')
        caixa_atual = caixa_geral.objects.latest('id')
        total_caixa = caixa_atual.total - Decimal(nova_entrada)
        valor_op = Decimal(nova_entrada)
        novo_caixa = caixa_geral(operacao=1, tipo=metodo, valor_operacao=valor_op, descricao=motivo,id_operacao=caixa_atual.id, total=total_caixa)
        novo_caixa.save()
        caixa_atual = caixa_geral.objects.latest('id')
        msg = "Entrada realizada com sucesso!"
        return render(request, 'home/home.html', {'title':'Home', 'msg':msg})
    return render(request, 'entrada.html', {'title':'Retirada', 'caixa_atual':caixa_atual})

def fechar(request):
    caixa_atual = caixa_geral.objects.latest('id')
    hoje = datetime.now().strftime('%Y-%m-%d')
    dinheiro = 0
    cartao_debito = 0
    cartao_credito = 0
    entrega = 0 
    local = 0 
    viagem = 0 
    total_geral = 0
    for a in caixa_geral.objects.filter(data__date=hoje).filter(tipo=1, operacao=1).all():
        dinheiro = dinheiro + a.valor_operacao
    for b in caixa_geral.objects.filter(data__date=hoje).filter(tipo=2, operacao=1).all():
        cartao_debito = cartao_debito + b.valor_operacao
    for c in caixa_geral.objects.filter(data__date=hoje).filter(tipo=3, operacao=1).all():
        cartao_credito = cartao_credito + c.valor_operacao
    for d in comanda.objects.filter(data__date=hoje).filter(tipo=1).all():
        local = local + 1
    for e in comanda.objects.filter(data__date=hoje).filter(tipo=2).all():
        viagem = viagem + 1
    for f in comanda.objects.filter(data__date=hoje).filter(tipo=3).all():
        entrega = entrega + 1
    total_geral = cartao_debito + cartao_credito + dinheiro
    if request.method == 'POST' and request.POST.get('retirada') != None:
        nova_retirada = request.POST.get('retirada')
        motivo = "Fechamento caixa "+"."
        caixa_atual = caixa_geral.objects.latest('id')
        total_caixa = caixa_atual.total - Decimal(nova_retirada)
        valor_op = Decimal(nova_retirada)
        novo_caixa = caixa_geral(operacao=2, tipo=1, valor_operacao=valor_op, descricao=motivo,id_operacao=caixa_atual.id, total=total_caixa)
        novo_caixa.save()
        caixa_atual = caixa_geral.objects.latest('id')
        msg = "Retirada realizada com sucesso!"
        return render(request, 'home/home.html', {'title':'Home', 'msg':msg})
    return render(request, 'fechar.html', {'title':'Fechar caixa', 'caixa_atual':caixa_atual, 'total_geral':total_geral, 'dinheiro':dinheiro, 'cartao_debito':cartao_debito, 'cartao_credito':cartao_credito, 'local':local, 'viagem':viagem, 'entrega':entrega})

def dados(request):
    hoje = datetime.date.today().strftime('%Y-%m-%d')
    caixas = caixa_geral.objects.filter(data__contains=hoje)
    caixa_atual = caixa_geral.objects.latest('id')
    dinheiro = 0
    cartao = 0 
    entrega = 0
    for d in caixa_geral.objects.filter(data__contains=hoje, obs='Dinheiro'):
        d_id = d.item
        int(d_id)
        item = comanda.objects.filter(id=d_id).get()
        dinheiro = dinheiro + item.total
    for c in caixa_geral.objects.filter(data__contains=hoje, obs='Cartao'):
        c_id = c.item
        int(c_id)
        item = comanda.objects.filter(id=c_id).get()
        cartao = cartao + item.total
    for e in caixa_geral.objects.filter(data__contains=hoje):
        e_id = e.item
        try: 
            int(e_id)
            cmd = comanda.objects.filter(id=e_id).get()
            cmd1 = cmd.produtos.all()
            for p in cmd1:
                prod = p.produto_item.nome
                if prod == 'Entrega':
                    entrega = entrega +1
        except:
            cmd = None
    if request.method == 'POST':
        data_inicio = request.POST.get('data_inicio')
        data_fim = request.POST.get('data_fim')
        caixas = caixa_geral.objects.filter(data__range=(data_inicio,data_fim)).all()
        dinheiro = 0
        cartao = 0 
        entrega = 0
        local = 0
        faturamento = 0
        for d in caixa_geral.objects.filter(data__range=(data_inicio,data_fim), tipo='Entrada', obs='Dinheiro'):
            d_id = d.item
            int(d_id)
            item = comanda.objects.filter(id=d_id).get()
            dinheiro = dinheiro + item.total
        for c in caixa_geral.objects.filter(data__range=(data_inicio,data_fim), tipo='Entrada', obs='Cartao'):
            c_id = c.item
            int(c_id)
            item = comanda.objects.filter(id=c_id).get()
            cartao = cartao + item.total
        for e in caixa_geral.objects.filter(data__range=(data_inicio,data_fim), tipo='Entrada'):
            e_id = e.item
            int(e_id)
            item = comanda.objects.filter(id=e_id).get()
            faturamento = faturamento + item.total
            item1 = item.produtos.all()
            for f in item1:
                prod = f.produto_item.nome
                if prod == 'Entrega':
                    entrega = entrega +1
                else:
                    local = local +1
        return render(request, 'dados_periodo.html', {'title':'Dados Periodo', 'local':local, 'data_inicio':data_inicio, 'data_fim':data_fim, 'faturamento':faturamento, 'dinheiro':dinheiro, 'cartao':cartao, 'entrega':entrega})    
    return render(request, 'dados.html', {'title':'Dados', 'caixas':caixas, 'hoje':hoje, 'caixa_atual':caixa_atual, 'dinheiro':dinheiro, 'cartao':cartao, 'entrega':entrega})