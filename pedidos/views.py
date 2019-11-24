#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from pedidos.models import comanda, produto, sorvete ,itemsorvete , itemproduto, adicional, acai, itemacai, mix, itemmix, casadinho, itemcasadinho, creme, itemcreme, mshake, itemmshake, petit, itempetit, fondue, itemfondue, suco, itemsuco
from caixa.models import caixa_geral
from outros.models import senha
from cliente.models import cliente
from decimal import *
from escposprinter import *
from datetime import datetime

# Create your views here.
def novo_pedido(request):
    clientes = cliente.objects.all().order_by('nome')
    return render(request, 'pedidos/novo_pedido.html', {'title':'Novo Pedido', 'clientes':clientes})

def local(request):
    if request.method == 'POST':
        try:
            cliente_obj = cliente.objects.filter(nome="Local").get()
        except:
            cliente_obj = cliente(nome="Local")
            cliente_obj.save()
        comanda_obj = comanda(tipo=1, cli=cliente_obj)
        comanda_obj.save()
        msg = "Pedido local"
        return render(request, 'pedidos/pedidos.html', {'title':'Pedidos', 'comanda_obj': comanda_obj, 'msg':msg})

    clientes = cliente.objects.all().order_by('nome')
    return render(request, 'pedidos/novo_pedido.html', {'title':'Novo Pedido', 'clientes':clientes})

def viagem(request):
    if request.method == 'POST':
        try:
            cliente_obj = cliente.objects.filter(nome="Viagem").get()
        except:
            cliente_obj = cliente(nome="Viagem")
            cliente_obj.save()
        comanda_obj = comanda(tipo=2, cli=cliente_obj)
        comanda_obj.save()
        msg = "Pedido viagem"
        return render(request, 'pedidos/pedidos.html', {'title':'Pedidos', 'comanda_obj': comanda_obj, 'msg':msg})

    clientes = cliente.objects.all().order_by('nome')
    return render(request, 'pedidos/novo_pedido.html', {'title':'Novo Pedido', 'clientes':clientes})

def entrega(request):
    clientes = cliente.objects.all().order_by('nome')
    if request.method == 'POST' and request.POST.get('telefone') != None and request.POST.get('cliente_id') == None:
        telefone = request.POST.get('telefone')
        try:
            cliente_obj = cliente.objects.filter(telefone1=telefone).get()
        except:
            cliente_obj = None
        if cliente_obj == None:
            try:
                cliente_obj = cliente.objects.filter(telefone2=telefone).get()
            except:
                cliente_obj = None
        if cliente_obj == None:
            return render(request, 'cliente/novo_cliente.html', {'title':'Novo Cliente', 'telefone':telefone})
        if cliente_obj != None:
            comanda_obj = comanda(tipo=3, cli=cliente_obj)
            comanda_obj.save()
            msg = "Pedido do " + cliente_obj.nome
            return render(request, 'pedidos/pedidos.html', {'title':'Pedidos', 'comanda_obj': comanda_obj, 'msg':msg})

    if request.method == 'POST' and request.POST.get('cliente_id') != None and request.POST.get('telefone') == '':
        cliente_id = request.POST.get('cliente_id')
        try:
            cliente_obj = cliente.objects.filter(id=cliente_id).get()
        except:
            cliente_obj = None
        if cliente_obj == None:
            return render(request, 'cliente/novo_cliente.html', {'title':'Novo Cliente'})
        if cliente_obj != None:
            comanda_obj = comanda(tipo=3, cli=cliente_obj)
            comanda_obj.save()
            msg = "Pedido do " + cliente_obj.nome
            return render(request, 'pedidos/pedidos.html', {'title':'Pedidos', 'comanda_obj': comanda_obj, 'msg':msg})

    return render(request, 'pedidos/novo_pedido.html', {'title':'Novo Pedido', 'clientes':clientes})

def pedidos(request):
    comanda_id = request.POST.get('comanda_id')
    try: ## Comanda_obj
        comanda_obj = comanda.objects.filter(id=comanda_id).get()
    except:
        comanda_obj = None
    pedido1 = request.POST.get('pedido')
    if pedido1 == 'acai':
        return render(request, 'pedidos/acai.html', {'title':'Acai na Tigela', 'comanda_obj':comanda_obj})
    if pedido1 == 'casadinho':
        return render(request, 'pedidos/casadinho.html', {'title':'Açaí Casadinho', 'comanda_obj':comanda_obj})
    if pedido1 == 'mix':
        return render(request, 'pedidos/mix.html', {'title':'Açaí Mix', 'comanda_obj':comanda_obj})
    if pedido1 == 'acaienergy':
        return render(request, 'pedidos/acaienergy.html', {'title':'Açaí Energy', 'comanda_obj':comanda_obj})
    if pedido1 == 'acaicreme':
        return render(request, 'pedidos/acaicreme.html', {'title':'Cremes', 'comanda_obj':comanda_obj})
    if pedido1 == 'sorvete':
        return render(request, 'pedidos/sorvete.html', {'title':'sorvete', 'comanda_obj':comanda_obj})
    if pedido1 == 'milkshake':
        return render(request, 'pedidos/milkshake.html', {'title':'Milk Shake', 'comanda_obj':comanda_obj})
    if pedido1 == 'petit':
        return render(request, 'pedidos/petit.html', {'title':'Petit Gateau', 'comanda_obj':comanda_obj})
    if pedido1 == 'fondue':
        return render(request, 'pedidos/fondue.html', {'title':'Fondue', 'comanda_obj':comanda_obj})
    if pedido1 == 'sucos':
        return render(request, 'pedidos/sucos.html', {'title':'Sucos', 'comanda_obj':comanda_obj})
    if pedido1 == 'produtos':
        return render(request, 'pedidos/produtos.html', {'title':'Produtos', 'comanda_obj':comanda_obj})

    return render(request, 'pedidos/pedidos.html', {'title':'Pedidos', 'comanda_obj':comanda_obj})

def tamanho(request):
    pedido1 = request.POST.get('pedido')
    comanda_id = request.POST.get('comanda_id')
    try: ## comanda_obj
        comanda_obj = comanda.objects.filter(id=comanda_id).get()
    except:
        comanda_obj = None
    return render(request, 'pedidos/tamanho.html', {'title':'Tamanho', 'pedido1':pedido1, 'comanda_obj':comanda_obj})

def confirmacao(request):
    pedido1 = request.GET.get('pedido')
    comanda_id = request.GET.get('comanda_id')
    return render(request, 'pedidos/confirmacao.html', {'title':'Confirmação', 'pedido1':pedido1, 'comanda_id':comanda_id})

def adicionais(request):
    item_acai_id = request.GET.get('item_acai_id')
    item_casadinho_id = request.GET.get('item_casadinho_id')
    item_mix_id = request.GET.get('item_mix_id')
    item_creme_id = request.GET.get('item_creme_id')
    item_sorvete_id = request.GET.get('item_sorvete_id')
    item_mshake_id = request.GET.get('item_mshake_id')
    item_petit_id = request.GET.get('item_petit_id')
    item_fondue_id = request.GET.get('item_fondue_id')
    adicionais = adicional.objects.all()
    comanda_id = request.GET.get('comanda_id')
    
    try:
        item_acai_id = itemacai.objects.filter(id=item_acai_id).get()
    except:
        item_acai_id = None
    try:
        item_casadinho_id = itemcasadinho.objects.filter(id=item_casadinho_id).get()
    except:
        item_casadinho_id = None
    try:
        item_mix_id = itemmix.objects.filter(id=item_mix_id).get()
    except:
        item_mix_id = None
    try:
        item_creme_id = itemcreme.objects.filter(id=item_creme_id).get()
    except:
        item_creme_id = None
    try:
        item_sorvete_id = itemsorvete.objects.filter(id=item_sorvete_id).get()
    except:
        item_sorvete_id = None
    try:
        item_mshake_id = itemmshake.objects.filter(id=item_mshake_id).get()
    except:
        item_mshake_id = None
    try:
        item_petit_id = itempetit.objects.filter(id=item_petit_id).get()
    except:
        item_petit_id = None
    try:
        item_fondue_id = itemfondue.objects.filter(id=item_fondue_id).get()
    except:
        item_fondue_id = None

    if item_acai_id != None :
        adicionais = adicional.objects.all()
        comanda_id = request.GET.get('comanda_id')
        return render(request, 'pedidos/adicionais.html', {'title':'Adicionais', 'adicionais':adicionais, 'item_acai_id':item_acai_id, 'comanda_id':comanda_id})
    if item_casadinho_id != None:
        adicionais = adicional.objects.all()
        comanda_id = request.GET.get('comanda_id')
        return render(request, 'pedidos/adicionais.html', {'title':'Adicionais', 'adicionais':adicionais, 'item_casadinho_id':item_casadinho_id, 'comanda_id':comanda_id})
    if item_mix_id != None :
        adicionais = adicional.objects.all()
        comanda_id = request.GET.get('comanda_id')
        return render(request, 'pedidos/adicionais.html', {'title':'Adicionais', 'adicionais':adicionais, 'item_mix_id':item_mix_id, 'comanda_id':comanda_id})
    if item_creme_id != None :
        adicionais = adicional.objects.all()
        comanda_id = request.GET.get('comanda_id')
        return render(request, 'pedidos/adicionais.html', {'title':'Adicionais', 'adicionais':adicionais, 'item_creme_id':item_creme_id, 'comanda_id':comanda_id})
    if item_sorvete_id != None :
        adicionais = adicional.objects.all()
        comanda_id = request.GET.get('comanda_id')
        return render(request, 'pedidos/adicionais.html', {'title':'Adicionais', 'adicionais':adicionais, 'item_sorvete_id':item_sorvete_id, 'comanda_id':comanda_id})
    if item_mshake_id != None :
        adicionais = adicional.objects.all()
        comanda_id = request.GET.get('comanda_id')
        return render(request, 'pedidos/adicionais.html', {'title':'Adicionais', 'adicionais':adicionais, 'item_mshake_id':item_mshake_id, 'comanda_id':comanda_id})
    if item_petit_id != None :
        adicionais = adicional.objects.all()
        comanda_id = request.GET.get('comanda_id')
        return render(request, 'pedidos/adicionais.html', {'title':'Adicionais', 'adicionais':adicionais, 'item_petit_id':item_petit_id, 'comanda_id':comanda_id})
    if item_fondue_id != None :
        adicionais = adicional.objects.all()
        comanda_id = request.GET.get('comanda_id')
        return render(request, 'pedidos/adicionais.html', {'title':'Adicionais', 'adicionais':adicionais, 'item_fondue_id':item_fondue_id, 'comanda_id':comanda_id})
    return render(request, 'pedidos/adicionais.html', {'title':'Adicionais', 'adicionais':adicionais, 'comanda_id':comanda_id})

def excluir(request):
    item_acai_id = request.GET.get('item_acai_id')
    item_casadinho_id = request.GET.get('item_casadinho_id')
    item_mix_id = request.GET.get('item_mix_id')
    item_creme_id = request.GET.get('item_creme_id')
    item_sorvete_id = request.GET.get('item_sorvete_id')
    item_mshake_id = request.GET.get('item_mshake_id')
    item_petit_id = request.GET.get('item_petit_id')
    item_fondue_id = request.GET.get('item_fondue_id')
    item_produto_id = request.GET.get('item_produto_id')
    comanda_id = request.GET.get('comanda_id')
    try: ## comanda_obj
        comanda_obj = comanda.objects.filter(id=comanda_id).get()
    except:
        comanda_obj = None
    try: ## item_acai_obj
        item_acai_obj = itemacai.objects.filter(id=item_acai_id).get()
    except:
        item_acai_obj = None
    try: ## item_casadinho_obj
        item_casadinho_obj = itemcasadinho.objects.filter(id=item_casadinho_id).get()
    except:
        item_casadinho_obj = None
    try: ## item_mix_obj
        item_mix_obj = itemmix.objects.filter(id=item_mix_id).get()
    except:
        item_mix_obj = None
    try: ## item_creme_obj
        item_creme_obj = itemcreme.objects.filter(id=item_creme_id).get()
    except:
        item_creme_obj = None
    try: ## item_sorvete_obj
        item_sorvete_obj = itemsorvete.objects.filter(id=item_sorvete_id).get()
    except:
        item_sorvete_obj = None
    try: ## item_mshake_obj
        item_mshake_obj = itemmshake.objects.filter(id=item_mshake_id).get()
    except:
        item_mshake_obj = None
    try: ## item_petit_obj
        item_petit_obj = itempetit.objects.filter(id=item_petit_id).get()
    except:
        item_petit_obj = None
    try: ## item_fondue_obj
        item_fondue_obj = itemfondue.objects.filter(id=item_fondue_id).get()
    except:
        item_fondue_obj = None
    try: ## item_produto_obj
        item_produto_obj = itemproduto.objects.filter(id=item_produto_id).get()
    except:
        item_produto_obj = None

    if item_acai_obj != None and comanda_obj != None: ## Excluir ACAI em comanda
        comanda_obj.total = comanda_obj.total - item_acai_obj.total
        item_acai_obj.delete()
        comanda_obj.save()
        acais1 = comanda_obj.acais.all()
        mixs1 = comanda_obj.mixs.all()
        casadinhos1 = comanda_obj.casadinhos.all()
        produtos1 = comanda_obj.produtos.all()
        cremes1 = comanda_obj.cremes.all()
        sorvetes1 = comanda_obj.sorvetes.all()
        mshakes1 = comanda_obj.mshakes.all()
        petits1 = comanda_obj.petits.all()
        fondues1 = comanda_obj.fondues.all()
        return render(request, 'pedidos/finalizar.html',{'title':'Fechamento', 'fondues1':fondues1, 'petits1':petits1, 'mshakes1':mshakes1, 'sorvetes1':sorvetes1, 'acais1':acais1, 'mixs1':mixs1, 'casadinhos1':casadinhos1, 'cremes1':cremes1, 'produtos1':produtos1, 'comanda_obj':comanda_obj})
    if item_mix_obj != None and comanda_obj != None: ## Excluir MIX em comanda
        comanda_obj.total = comanda_obj.total - item_mix_obj.total
        item_mix_obj.delete()
        comanda_obj.save()
        acais1 = comanda_obj.acais.all()
        mixs1 = comanda_obj.mixs.all()
        casadinhos1 = comanda_obj.casadinhos.all()
        produtos1 = comanda_obj.produtos.all()
        cremes1 = comanda_obj.cremes.all()
        sorvetes1 = comanda_obj.sorvetes.all()
        mshakes1 = comanda_obj.mshakes.all()
        petits1 = comanda_obj.petits.all()
        fondues1 = comanda_obj.fondues.all()
        return render(request, 'pedidos/finalizar.html',{'title':'Fechamento', 'fondues1':fondues1, 'petits1':petits1, 'mshakes1':mshakes1, 'sorvetes1':sorvetes1, 'acais1':acais1, 'mixs1':mixs1, 'casadinhos1':casadinhos1, 'cremes1':cremes1, 'produtos1':produtos1, 'comanda_obj':comanda_obj})
    if item_casadinho_obj != None and comanda_obj != None: ## Excluir CASADINHO em comanda
        comanda_obj.total = comanda_obj.total - item_casadinho_obj.total
        item_casadinho_obj.delete()
        comanda_obj.save()
        acais1 = comanda_obj.acais.all()
        mixs1 = comanda_obj.mixs.all()
        casadinhos1 = comanda_obj.casadinhos.all()
        produtos1 = comanda_obj.produtos.all()
        cremes1 = comanda_obj.cremes.all()
        sorvetes1 = comanda_obj.sorvetes.all()
        mshakes1 = comanda_obj.mshakes.all()
        petits1 = comanda_obj.petits.all()
        fondues1 = comanda_obj.fondues.all()
        return render(request, 'pedidos/finalizar.html',{'title':'Fechamento', 'fondues1':fondues1, 'petits1':petits1, 'mshakes1':mshakes1, 'sorvetes1':sorvetes1, 'acais1':acais1, 'mixs1':mixs1, 'casadinhos1':casadinhos1, 'cremes1':cremes1, 'produtos1':produtos1, 'comanda_obj':comanda_obj})
    if item_creme_obj != None and comanda_obj != None: ## Excluir CREME em comanda
        comanda_obj.total = comanda_obj.total - item_creme_obj.total
        item_creme_obj.delete()
        comanda_obj.save()
        acais1 = comanda_obj.acais.all()
        mixs1 = comanda_obj.mixs.all()
        casadinhos1 = comanda_obj.casadinhos.all()
        produtos1 = comanda_obj.produtos.all()
        cremes1 = comanda_obj.cremes.all()
        sorvetes1 = comanda_obj.sorvetes.all()
        mshakes1 = comanda_obj.mshakes.all()
        petits1 = comanda_obj.petits.all()
        fondues1 = comanda_obj.fondues.all()
        return render(request, 'pedidos/finalizar.html',{'title':'Fechamento', 'fondues1':fondues1, 'petits1':petits1, 'mshakes1':mshakes1, 'sorvetes1':sorvetes1, 'acais1':acais1, 'mixs1':mixs1, 'casadinhos1':casadinhos1, 'cremes1':cremes1, 'produtos1':produtos1, 'comanda_obj':comanda_obj})
    if item_sorvete_obj != None and comanda_obj != None: ## Excluir SORVETE em comanda
        comanda_obj.total = comanda_obj.total - item_sorvete_obj.total
        item_sorvete_obj.delete()
        comanda_obj.save()
        acais1 = comanda_obj.acais.all()
        mixs1 = comanda_obj.mixs.all()
        casadinhos1 = comanda_obj.casadinhos.all()
        produtos1 = comanda_obj.produtos.all()
        cremes1 = comanda_obj.cremes.all()
        sorvetes1 = comanda_obj.sorvetes.all()
        mshakes1 = comanda_obj.mshakes.all()
        petits1 = comanda_obj.petits.all()
        fondues1 = comanda_obj.fondues.all()
        return render(request, 'pedidos/finalizar.html',{'title':'Fechamento', 'fondues1':fondues1, 'petits1':petits1, 'mshakes1':mshakes1, 'sorvetes1':sorvetes1, 'acais1':acais1, 'mixs1':mixs1, 'casadinhos1':casadinhos1, 'cremes1':cremes1, 'produtos1':produtos1, 'comanda_obj':comanda_obj})
    if item_mshake_obj != None and comanda_obj != None: ## Excluir MILKSHAKE em comanda
        comanda_obj.total = comanda_obj.total - item_mshake_obj.total
        item_mshake_obj.delete()
        comanda_obj.save()
        acais1 = comanda_obj.acais.all()
        mixs1 = comanda_obj.mixs.all()
        casadinhos1 = comanda_obj.casadinhos.all()
        produtos1 = comanda_obj.produtos.all()
        cremes1 = comanda_obj.cremes.all()
        sorvetes1 = comanda_obj.sorvetes.all()
        mshakes1 = comanda_obj.mshakes.all()
        petits1 = comanda_obj.petits.all()
        fondues1 = comanda_obj.fondues.all()
        return render(request, 'pedidos/finalizar.html',{'title':'Fechamento', 'fondues1':fondues1, 'petits1':petits1, 'mshakes1':mshakes1, 'sorvetes1':sorvetes1, 'acais1':acais1, 'mixs1':mixs1, 'casadinhos1':casadinhos1, 'cremes1':cremes1, 'produtos1':produtos1, 'comanda_obj':comanda_obj})
    if item_petit_obj != None and comanda_obj != None: ## Excluir PETIT GATEAU em comanda
        comanda_obj.total = comanda_obj.total - item_petit_obj.total
        item_petit_obj.delete()
        comanda_obj.save()
        acais1 = comanda_obj.acais.all()
        mixs1 = comanda_obj.mixs.all()
        casadinhos1 = comanda_obj.casadinhos.all()
        produtos1 = comanda_obj.produtos.all()
        cremes1 = comanda_obj.cremes.all()
        sorvetes1 = comanda_obj.sorvetes.all()
        mshakes1 = comanda_obj.mshakes.all()
        petits1 = comanda_obj.petits.all()
        fondues1 = comanda_obj.fondues.all()
        return render(request, 'pedidos/finalizar.html',{'title':'Fechamento', 'fondues1':fondues1, 'petits1':petits1, 'mshakes1':mshakes1, 'sorvetes1':sorvetes1, 'acais1':acais1, 'mixs1':mixs1, 'casadinhos1':casadinhos1, 'cremes1':cremes1, 'produtos1':produtos1, 'comanda_obj':comanda_obj})
    if item_fondue_obj != None and comanda_obj != None: ## Excluir FONDUE em comanda
        comanda_obj.total = comanda_obj.total - item_fondue_obj.total
        item_fondue_obj.delete()
        comanda_obj.save()
        acais1 = comanda_obj.acais.all()
        mixs1 = comanda_obj.mixs.all()
        casadinhos1 = comanda_obj.casadinhos.all()
        produtos1 = comanda_obj.produtos.all()
        cremes1 = comanda_obj.cremes.all()
        sorvetes1 = comanda_obj.sorvetes.all()
        mshakes1 = comanda_obj.mshakes.all()
        petits1 = comanda_obj.petits.all()
        fondues1 = comanda_obj.fondues.all()
        return render(request, 'pedidos/finalizar.html',{'title':'Fechamento', 'fondues1':fondues1, 'petits1':petits1, 'mshakes1':mshakes1, 'sorvetes1':sorvetes1, 'acais1':acais1, 'mixs1':mixs1, 'casadinhos1':casadinhos1, 'cremes1':cremes1, 'produtos1':produtos1, 'comanda_obj':comanda_obj})
    if item_produto_obj != None and comanda_obj != None: ## Excluir FONDUE em comanda
        comanda_obj.total = comanda_obj.total - item_produto_obj.total
        item_produto_obj.delete()
        comanda_obj.save()
        acais1 = comanda_obj.acais.all()
        mixs1 = comanda_obj.mixs.all()
        casadinhos1 = comanda_obj.casadinhos.all()
        produtos1 = comanda_obj.produtos.all()
        cremes1 = comanda_obj.cremes.all()
        sorvetes1 = comanda_obj.sorvetes.all()
        mshakes1 = comanda_obj.mshakes.all()
        petits1 = comanda_obj.petits.all()
        fondues1 = comanda_obj.fondues.all()
        return render(request, 'pedidos/finalizar.html',{'title':'Fechamento', 'fondues1':fondues1, 'petits1':petits1, 'mshakes1':mshakes1, 'sorvetes1':sorvetes1, 'acais1':acais1, 'mixs1':mixs1, 'casadinhos1':casadinhos1, 'cremes1':cremes1, 'produtos1':produtos1, 'comanda_obj':comanda_obj})

def finalizar(request):
    pedido2 = request.POST.get('pedido')
    cliente_id = request.POST.get('cliente_id')
    try:
        cliente_obj = cliente.objects.filter(id=cliente_id).get()
    except:
        cliente_obj = None
    tamanho1 = request.POST.get('tamanho')
    acompanhamento = request.POST.get('acompanhamento')
    acai1 = request.POST.get('item_acai_id')
    casadinho1 = request.POST.get('item_casadinho_id')
    mix1 = request.POST.get('item_mix_id')
    creme1 = request.POST.get('item_creme_id')
    sorvete1 = request.POST.get('item_sorvete_id')
    mshake1 = request.POST.get('item_mshake_id')
    petit1 = request.POST.get('item_petit_id')
    fondue1 = request.POST.get('item_fondue_id')
    pedido_produto = request.POST.get('pedido_produto')
    pedido_sorvete = request.POST.get('pedido_sorvete')
    pedido_petit = request.POST.get('pedido_petit')
    pedido_fondue = request.POST.get('pedido_fondue')
    pedido_suco = request.POST.get('pedido_suco')
    adicionais1 = request.POST.getlist('adicional2')
    comanda_id = request.POST.get('comanda_id')
    if adicionais1 == []:
        adicionais1 = None
    
    try: ##Item Acai
        acai1 = itemacai.objects.filter(id=acai1).get()
    except:
        acai1 = None

    try: ##Item Casadinho
        casadinho1 = itemcasadinho.objects.filter(id=casadinho1).get()
    except:
        casadinho1 = None

    try: ##Item Mix
        mix1 = itemmix.objects.filter(id=mix1).get()
    except:
        mix1 = None

    try: ##Item Creme
        creme1 = itemcreme.objects.filter(id=creme1).get()
    except:
        creme1 = None

    try: ##Item Produto
        produto1 = itemproduto.objects.filter(id=produto1).get()
    except:
        produto1 = None

    try: ##Item Sorvete
        sorvete1 = itemsorvete.objects.filter(id=sorvete1).get()
    except:
        sorvete1 = None

    try: ##Item MShake
        mshake1 = itemmshake.objects.filter(id=mshake1).get()
    except:
        mshake1 = None

    try: ##Item Petit
        petit1 = itempetit.objects.filter(id=petit1).get()
    except:
        petit1 = None

    try: ##Item Fondue
        fondue1 = itemfondue.objects.filter(id=fondue1).get()
    except:
        fondue1 = None
    
    try: ## Comanda_obj
        comanda_obj = comanda.objects.filter(id=comanda_id).get()
    except:
        comanda_obj = None

    try: ## pedido produto
        pedido_produto = produto.objects.filter(img=pedido2).get()
    except:
        pedido_produto = None

    try: ## pedido petit
        pedido_petit = petit.objects.filter(img=pedido2).get()
    except:
        pedido_petit = None

    try: ## pedido fondue
        pedido_fondue = fondue.objects.filter(img=pedido2).get()
    except:
        pedido_fondue = None

    try: ## pedido suco
        pedido_suco = suco.objects.filter(img=pedido2).get()
    except:
        pedido_suco = None

    try: ## pedido sorvete
        pedido_sorvete = sorvete.objects.filter(img=pedido2).get()
    except:
        pedido_sorvete = None

    try: ## pedido acai
        pedido_acai = acai.objects.filter(img=pedido2, tamanho=tamanho1).get()
    except:
        pedido_acai = None

    try: ## pedido Casadinho
        pedido_casadinho = casadinho.objects.filter(img=pedido2, tamanho=tamanho1).get()
    except:
        pedido_casadinho = None

    try: ##pedido mix
        pedido_mix = mix.objects.filter(img=pedido2, tamanho=tamanho1).get()
    except:
        pedido_mix = None
        
    try: ##pedido creme
        pedido_creme = creme.objects.filter(img=pedido2, tamanho=tamanho1).get()
    except:
        pedido_creme = None

    try: ##pedido mshake
        pedido_mshake = mshake.objects.filter(img=pedido2, tamanho=tamanho1).get()
    except:
        pedido_mshake = None
        

    if pedido_acai != None and tamanho1 != None and comanda_obj != None and adicionais1 == None: ##add ACAI em comanda 
        total_pedido = pedido_acai.preco
        novo_item_acai = itemacai(acai_item=pedido_acai, acompanhamento=acompanhamento, total=total_pedido)
        novo_item_acai.save()
        comanda_obj.total = comanda_obj.total + total_pedido
        comanda_obj.save()
        comanda_obj.acais.add(novo_item_acai)
        comanda_obj.save()
        acais1 = comanda_obj.acais.all()
        mixs1 = comanda_obj.mixs.all()
        casadinhos1 = comanda_obj.casadinhos.all()
        cremes1 = comanda_obj.cremes.all()
        produtos1 = comanda_obj.produtos.all()
        sorvetes1 = comanda_obj.sorvetes.all()
        mshakes1 = comanda_obj.mshakes.all()
        petits1 = comanda_obj.petits.all()
        fondues1 = comanda_obj.fondues.all()
        sucos1 = comanda_obj.sucos.all()
        return render(request, 'pedidos/finalizar.html', {'title':'Fechamento', 'sucos1':sucos1, 'fondues1':fondues1, 'petits1':petits1, 'mshakes1':mshakes1, 'sorvetes1':sorvetes1, 'acais1':acais1, 'mixs1':mixs1, 'casadinhos1':casadinhos1, 'cremes1':cremes1, 'produtos1':produtos1, 'comanda_obj':comanda_obj})
    if pedido_mix != None and tamanho1 != None and comanda_obj != None and adicionais1 == None: ##add MIX em comanda 
        total_pedido = pedido_mix.preco
        novo_item = itemmix(mix_item=pedido_mix, acompanhamento=acompanhamento, total=total_pedido)
        novo_item.save()
        comanda_obj.total = comanda_obj.total + total_pedido
        comanda_obj.save()
        comanda_obj.mixs.add(novo_item)
        comanda_obj.save()
        acais1 = comanda_obj.acais.all()
        mixs1 = comanda_obj.mixs.all()
        casadinhos1 = comanda_obj.casadinhos.all()
        cremes1 = comanda_obj.cremes.all()
        produtos1 = comanda_obj.produtos.all()
        sorvetes1 = comanda_obj.sorvetes.all()
        mshakes1 = comanda_obj.mshakes.all()
        petits1 = comanda_obj.petits.all()
        fondues1 = comanda_obj.fondues.all()
        sucos1 = comanda_obj.sucos.all()
        return render(request, 'pedidos/finalizar.html', {'title':'Fechamento', 'sucos1':sucos1, 'fondues1':fondues1, 'petits1':petits1, 'mshakes1':mshakes1, 'sorvetes1':sorvetes1, 'acais1':acais1, 'mixs1':mixs1, 'casadinhos1':casadinhos1, 'cremes1':cremes1, 'produtos1':produtos1, 'comanda_obj':comanda_obj})
    if pedido_casadinho != None and tamanho1 != None and comanda_obj != None and adicionais1 == None: ##add CASADINHO em comanda 
        total_pedido = pedido_casadinho.preco
        novo_item = itemcasadinho(casadinho_item=pedido_casadinho, acompanhamento=acompanhamento, total=total_pedido)
        novo_item.save()
        comanda_obj.total = comanda_obj.total + total_pedido
        comanda_obj.save()
        comanda_obj.casadinhos.add(novo_item)
        comanda_obj.save()
        acais1 = comanda_obj.acais.all()
        mixs1 = comanda_obj.mixs.all()
        casadinhos1 = comanda_obj.casadinhos.all()
        cremes1 = comanda_obj.cremes.all()
        produtos1 = comanda_obj.produtos.all()
        sorvetes1 = comanda_obj.sorvetes.all()
        mshakes1 = comanda_obj.mshakes.all()
        petits1 = comanda_obj.petits.all()
        fondues1 = comanda_obj.fondues.all()
        sucos1 = comanda_obj.sucos.all()
        return render(request, 'pedidos/finalizar.html', {'title':'Fechamento', 'sucos1':sucos1, 'fondues1':fondues1, 'petits1':petits1, 'mshakes1':mshakes1, 'sorvetes1':sorvetes1, 'acais1':acais1, 'mixs1':mixs1, 'casadinhos1':casadinhos1, 'cremes1':cremes1, 'produtos1':produtos1, 'comanda_obj':comanda_obj})
    if pedido_creme != None and tamanho1 != None and comanda_obj != None and adicionais1 == None: ##add CREME em comanda 
        total_pedido = pedido_creme.preco
        novo_item = itemcreme(creme_item=pedido_creme, acompanhamento=acompanhamento, total=total_pedido)
        novo_item.save()
        comanda_obj.total = comanda_obj.total + total_pedido
        comanda_obj.save()
        comanda_obj.cremes.add(novo_item)
        comanda_obj.save()
        acais1 = comanda_obj.acais.all()
        mixs1 = comanda_obj.mixs.all()
        casadinhos1 = comanda_obj.casadinhos.all()
        cremes1 = comanda_obj.cremes.all()
        produtos1 = comanda_obj.produtos.all()
        sorvetes1 = comanda_obj.sorvetes.all()
        mshakes1 = comanda_obj.mshakes.all()
        petits1 = comanda_obj.petits.all()
        fondues1 = comanda_obj.fondues.all()
        sucos1 = comanda_obj.sucos.all()
        return render(request, 'pedidos/finalizar.html', {'title':'Fechamento', 'sucos1':sucos1, 'fondues1':fondues1, 'petits1':petits1, 'mshakes1':mshakes1, 'sorvetes1':sorvetes1, 'acais1':acais1, 'mixs1':mixs1, 'casadinhos1':casadinhos1, 'cremes1':cremes1, 'produtos1':produtos1, 'comanda_obj':comanda_obj})
    if pedido_mshake != None and tamanho1 != None and comanda_obj != None and adicionais1 == None: ##add MSHAKE em comanda 
        total_pedido = pedido_mshake.preco
        novo_item = itemmshake(mshake_item=pedido_mshake, total=total_pedido)
        novo_item.save()
        comanda_obj.total = comanda_obj.total + total_pedido
        comanda_obj.save()
        comanda_obj.mshakes.add(novo_item)
        comanda_obj.save()
        acais1 = comanda_obj.acais.all()
        mixs1 = comanda_obj.mixs.all()
        casadinhos1 = comanda_obj.casadinhos.all()
        cremes1 = comanda_obj.cremes.all()
        produtos1 = comanda_obj.produtos.all()
        sorvetes1 = comanda_obj.sorvetes.all()
        mshakes1 = comanda_obj.mshakes.all()
        petits1 = comanda_obj.petits.all()
        fondues1 = comanda_obj.fondues.all()
        sucos1 = comanda_obj.sucos.all()
        return render(request, 'pedidos/finalizar.html', {'title':'Fechamento', 'sucos1':sucos1, 'fondues1':fondues1, 'petits1':petits1, 'mshakes1':mshakes1, 'sorvetes1':sorvetes1, 'acais1':acais1, 'mixs1':mixs1, 'casadinhos1':casadinhos1, 'cremes1':cremes1, 'produtos1':produtos1, 'comanda_obj':comanda_obj})
    if pedido_suco != None and tamanho1 != None and comanda_obj != None and adicionais1 == None: ##add SUCO em comanda 
        total_pedido = pedido_suco.preco
        novo_item = itemsuco(suco_item=pedido_suco, total=total_pedido)
        novo_item.save()
        comanda_obj.total = comanda_obj.total + total_pedido
        comanda_obj.save()
        comanda_obj.sucos.add(novo_item)
        comanda_obj.save()
        acais1 = comanda_obj.acais.all()
        mixs1 = comanda_obj.mixs.all()
        casadinhos1 = comanda_obj.casadinhos.all()
        cremes1 = comanda_obj.cremes.all()
        produtos1 = comanda_obj.produtos.all()
        sorvetes1 = comanda_obj.sorvetes.all()
        mshakes1 = comanda_obj.mshakes.all()
        petits1 = comanda_obj.petits.all()
        fondues1 = comanda_obj.fondues.all()
        sucos1 = comanda_obj.sucos.all()
        return render(request, 'pedidos/finalizar.html', {'title':'Fechamento', 'sucos1':sucos1, 'fondues1':fondues1, 'petits1':petits1, 'mshakes1':mshakes1, 'sorvetes1':sorvetes1, 'acais1':acais1, 'mixs1':mixs1, 'casadinhos1':casadinhos1, 'cremes1':cremes1, 'produtos1':produtos1, 'comanda_obj':comanda_obj})
    if pedido_sorvete != None and tamanho1 != None and comanda_obj != None and adicionais1 == None: ##add SORVETE em comanda 
        total_pedido = pedido_sorvete.preco
        novo_item = itemsorvete(sorvete_item=pedido_sorvete, total=total_pedido)
        novo_item.save()
        comanda_obj.total = comanda_obj.total + total_pedido
        comanda_obj.save()
        comanda_obj.sorvetes.add(novo_item)
        comanda_obj.save()
        acais1 = comanda_obj.acais.all()
        mixs1 = comanda_obj.mixs.all()
        casadinhos1 = comanda_obj.casadinhos.all()
        cremes1 = comanda_obj.cremes.all()
        produtos1 = comanda_obj.produtos.all()
        sorvetes1 = comanda_obj.sorvetes.all()
        mshakes1 = comanda_obj.mshakes.all()
        petits1 = comanda_obj.petits.all()
        fondues1 = comanda_obj.fondues.all()
        sucos1 = comanda_obj.sucos.all()
        return render(request, 'pedidos/finalizar.html', {'title':'Fechamento', 'sucos1':sucos1, 'fondues1':fondues1, 'petits1':petits1, 'mshakes1':mshakes1, 'sorvetes1':sorvetes1, 'acais1':acais1, 'mixs1':mixs1, 'casadinhos1':casadinhos1, 'cremes1':cremes1, 'produtos1':produtos1, 'comanda_obj':comanda_obj})
    if pedido_fondue != None and tamanho1 != None and comanda_obj != None and adicionais1 == None: ##add FONDUE em comanda 
        total_pedido = pedido_fondue.preco
        novo_item = itemfondue(fondue_item=pedido_fondue, total=total_pedido)
        novo_item.save()
        comanda_obj.total = comanda_obj.total + total_pedido
        comanda_obj.save()
        comanda_obj.fondues.add(novo_item)
        comanda_obj.save()
        acais1 = comanda_obj.acais.all()
        mixs1 = comanda_obj.mixs.all()
        casadinhos1 = comanda_obj.casadinhos.all()
        cremes1 = comanda_obj.cremes.all()
        produtos1 = comanda_obj.produtos.all()
        sorvetes1 = comanda_obj.sorvetes.all()
        mshakes1 = comanda_obj.mshakes.all()
        petits1 = comanda_obj.petits.all()
        fondues1 = comanda_obj.fondues.all()
        sucos1 = comanda_obj.sucos.all()
        return render(request, 'pedidos/finalizar.html', {'title':'Fechamento', 'sucos1':sucos1, 'fondues1':fondues1, 'petits1':petits1, 'mshakes1':mshakes1, 'sorvetes1':sorvetes1, 'acais1':acais1, 'mixs1':mixs1, 'casadinhos1':casadinhos1, 'cremes1':cremes1, 'produtos1':produtos1, 'comanda_obj':comanda_obj})
    if pedido_petit != None and tamanho1 != None and comanda_obj != None and adicionais1 == None: ##add PETIT em comanda
        total_pedido = pedido_petit.preco
        novo_item = itempetit(petit_item=pedido_petit, total=total_pedido)
        novo_item.save()
        comanda_obj.total = comanda_obj.total + total_pedido
        comanda_obj.save()
        comanda_obj.petits.add(novo_item)
        comanda_obj.save()
        acais1 = comanda_obj.acais.all()
        mixs1 = comanda_obj.mixs.all()
        casadinhos1 = comanda_obj.casadinhos.all()
        cremes1 = comanda_obj.cremes.all()
        produtos1 = comanda_obj.produtos.all()
        sorvetes1 = comanda_obj.sorvetes.all()
        mshakes1 = comanda_obj.mshakes.all()
        petits1 = comanda_obj.petits.all()
        fondues1 = comanda_obj.fondues.all()
        sucos1 = comanda_obj.sucos.all()
        return render(request, 'pedidos/finalizar.html', {'title':'Fechamento', 'sucos1':sucos1, 'fondues1':fondues1, 'petits1':petits1, 'mshakes1':mshakes1, 'sorvetes1':sorvetes1, 'acais1':acais1, 'mixs1':mixs1, 'casadinhos1':casadinhos1, 'cremes1':cremes1, 'produtos1':produtos1, 'comanda_obj':comanda_obj})
    if pedido_produto != None and comanda_obj != None and adicionais1 == None: ##add PRODUTO em comanda 
        total_pedido = pedido_produto.preco
        novo_item = itemproduto(produto_item=pedido_produto, total=total_pedido)
        novo_item.save()
        comanda_obj.total = comanda_obj.total + total_pedido
        comanda_obj.save()
        comanda_obj.produtos.add(novo_item)
        comanda_obj.save()
        acais1 = comanda_obj.acais.all()
        mixs1 = comanda_obj.mixs.all()
        casadinhos1 = comanda_obj.casadinhos.all()
        cremes1 = comanda_obj.cremes.all()
        produtos1 = comanda_obj.produtos.all()
        sorvetes1 = comanda_obj.sorvetes.all()
        mshakes1 = comanda_obj.mshakes.all()
        petits1 = comanda_obj.petits.all()
        fondues1 = comanda_obj.fondues.all()
        sucos1 = comanda_obj.sucos.all()
        return render(request, 'pedidos/finalizar.html', {'title':'Fechamento', 'sucos1':sucos1, 'fondues1':fondues1, 'petits1':petits1, 'mshakes1':mshakes1, 'sorvetes1':sorvetes1, 'acais1':acais1, 'mixs1':mixs1, 'casadinhos1':casadinhos1, 'cremes1':cremes1, 'produtos1':produtos1, 'comanda_obj':comanda_obj})
    if acai1 != None and adicionais1 != None and comanda_obj != None and pedido2 == None: ## add adicional em acai
        acai1 = acai1.id
        item_adicional = itemacai.objects.filter(id=acai1).get()
        for adicional2 in adicionais1 :
            add_id = int(adicional2)
            addicional = adicional.objects.filter(id=add_id).get()
            item_adicional.adicionais.add(addicional)
            item_adicional.total = item_adicional.total + addicional.preco
            item_adicional.save()
            comanda_obj.total = comanda_obj.total + addicional.preco
            comanda_obj.save()
        acais1 = comanda_obj.acais.all()
        mixs1 = comanda_obj.mixs.all()
        casadinhos1 = comanda_obj.casadinhos.all()
        produtos1 = comanda_obj.produtos.all()
        cremes1 = comanda_obj.cremes.all()
        sorvetes1 = comanda_obj.sorvetes.all()
        mshakes1 = comanda_obj.mshakes.all()
        petits1 = comanda_obj.petits.all()
        fondues1 = comanda_obj.fondues.all()
        return render(request, 'pedidos/finalizar.html',{'title':'Fechamento', 'fondues1':fondues1, 'petits1':petits1, 'mshakes1':mshakes1, 'sorvetes1':sorvetes1, 'acais1':acais1, 'mixs1':mixs1, 'casadinhos1':casadinhos1, 'cremes1':cremes1, 'produtos1':produtos1, 'comanda_obj':comanda_obj})
    if mix1 != None and adicionais1 != None and comanda_obj != None and pedido2 == None: ## add adicional em mix
        mix1 = mix1.id
        item_adicional = itemmix.objects.filter(id=mix1).get()
        for adicional2 in adicionais1 :
            add_id = int(adicional2)
            addicional = adicional.objects.filter(id=add_id).get()
            item_adicional.adicionais.add(addicional)
            item_adicional.total = item_adicional.total + addicional.preco
            item_adicional.save()
            comanda_obj.total = comanda_obj.total + addicional.preco
            comanda_obj.save()
        acais1 = comanda_obj.acais.all()
        mixs1 = comanda_obj.mixs.all()
        casadinhos1 = comanda_obj.casadinhos.all()
        produtos1 = comanda_obj.produtos.all()
        cremes1 = comanda_obj.cremes.all()
        sorvetes1 = comanda_obj.sorvetes.all()
        mshakes1 = comanda_obj.mshakes.all()
        petits1 = comanda_obj.petits.all()
        fondues1 = comanda_obj.fondues.all()
        return render(request, 'pedidos/finalizar.html',{'title':'Fechamento', 'fondues1':fondues1, 'petits1':petits1, 'mshakes1':mshakes1, 'sorvetes1':sorvetes1, 'acais1':acais1, 'mixs1':mixs1, 'casadinhos1':casadinhos1, 'cremes1':cremes1, 'produtos1':produtos1, 'comanda_obj':comanda_obj})
    if casadinho1 != None and adicionais1 != None and comanda_obj != None and pedido2 == None: ## add adicional em casadinho
        casadinho1 = casadinho1.id
        item_adicional = itemcasadinho.objects.filter(id=casadinho1).get()
        for adicional2 in adicionais1 :
            add_id = int(adicional2)
            addicional = adicional.objects.filter(id=add_id).get()
            item_adicional.adicionais.add(addicional)
            item_adicional.total = item_adicional.total + addicional.preco
            item_adicional.save()
            comanda_obj.total = comanda_obj.total +addicional.preco
            comanda_obj.save()
        acais1 = comanda_obj.acais.all()
        mixs1 = comanda_obj.mixs.all()
        casadinhos1 = comanda_obj.casadinhos.all()
        produtos1 = comanda_obj.produtos.all()
        cremes1 = comanda_obj.cremes.all()
        sorvetes1 = comanda_obj.sorvetes.all()
        mshakes1 = comanda_obj.mshakes.all()
        petits1 = comanda_obj.petits.all()
        fondues1 = comanda_obj.fondues.all()
        return render(request, 'pedidos/finalizar.html',{'title':'Fechamento', 'fondues1':fondues1, 'petits1':petits1, 'mshakes1':mshakes1, 'sorvetes1':sorvetes1, 'acais1':acais1, 'mixs1':mixs1, 'casadinhos1':casadinhos1, 'cremes1':cremes1, 'produtos1':produtos1, 'comanda_obj':comanda_obj})
    if creme1 != None and adicionais1 != None and comanda_obj != None and pedido2 == None: ## add adicional em creme
        creme1 = creme1.id
        item_adicional = itemcreme.objects.filter(id=creme1).get()
        for adicional2 in adicionais1 :
            add_id = int(adicional2)
            addicional = adicional.objects.filter(id=add_id).get()
            item_adicional.adicionais.add(addicional)
            item_adicional.total = item_adicional.total + addicional.preco
            item_adicional.save()
            comanda_obj.total = comanda_obj.total +addicional.preco
            comanda_obj.save()
        acais1 = comanda_obj.acais.all()
        mixs1 = comanda_obj.mixs.all()
        casadinhos1 = comanda_obj.casadinhos.all()
        produtos1 = comanda_obj.produtos.all()
        cremes1 = comanda_obj.cremes.all()
        sorvetes1 = comanda_obj.sorvetes.all()
        mshakes1 = comanda_obj.mshakes.all()
        petits1 = comanda_obj.petits.all()
        fondues1 = comanda_obj.fondues.all()
        return render(request, 'pedidos/finalizar.html',{'title':'Fechamento', 'fondues1':fondues1, 'petits1':petits1, 'mshakes1':mshakes1, 'sorvetes1':sorvetes1, 'acais1':acais1, 'mixs1':mixs1, 'casadinhos1':casadinhos1, 'cremes1':cremes1, 'produtos1':produtos1, 'comanda_obj':comanda_obj})
    if sorvete1 != None and adicionais1 != None and comanda_obj != None and pedido2 == None: ## add adicional em sorvete
        sorvete1 = sorvete1.id
        item_adicional = itemsorvete.objects.filter(id=sorvete1).get()
        for adicional2 in adicionais1 :
            add_id = int(adicional2)
            addicional = adicional.objects.filter(id=add_id).get()
            item_adicional.adicionais.add(addicional)
            item_adicional.total = item_adicional.total + addicional.preco
            item_adicional.save()
            comanda_obj.total = comanda_obj.total +addicional.preco
            comanda_obj.save()
        acais1 = comanda_obj.acais.all()
        mixs1 = comanda_obj.mixs.all()
        casadinhos1 = comanda_obj.casadinhos.all()
        produtos1 = comanda_obj.produtos.all()
        cremes1 = comanda_obj.cremes.all()
        sorvetes1 = comanda_obj.sorvetes.all()
        mshakes1 = comanda_obj.mshakes.all()
        petits1 = comanda_obj.petits.all()
        fondues1 = comanda_obj.fondues.all()
        return render(request, 'pedidos/finalizar.html',{'title':'Fechamento', 'fondues1':fondues1, 'petits1':petits1, 'mshakes1':mshakes1, 'sorvetes1':sorvetes1, 'acais1':acais1, 'mixs1':mixs1, 'casadinhos1':casadinhos1, 'cremes1':cremes1, 'produtos1':produtos1, 'comanda_obj':comanda_obj})
    if mshake1 != None and adicionais1 != None and comanda_obj != None and pedido2 == None: ## add adicional em mshake
        mshake1 = mshake1.id
        item_adicional = itemmshake.objects.filter(id=mshake1).get()
        for adicional2 in adicionais1 :
            add_id = int(adicional2)
            addicional = adicional.objects.filter(id=add_id).get()
            item_adicional.adicionais.add(addicional)
            item_adicional.total = item_adicional.total + addicional.preco
            item_adicional.save()
            comanda_obj.total = comanda_obj.total +addicional.preco
            comanda_obj.save()
        acais1 = comanda_obj.acais.all()
        mixs1 = comanda_obj.mixs.all()
        casadinhos1 = comanda_obj.casadinhos.all()
        cremes1 = comanda_obj.cremes.all()
        produtos1 = comanda_obj.produtos.all()
        sorvetes1 = comanda_obj.sorvetes.all()
        mshakes1 = comanda_obj.mshakes.all()
        petits1 = comanda_obj.petits.all()
        fondues1 = comanda_obj.fondues.all()
        return render(request, 'pedidos/finalizar.html',{'title':'Fechamento', 'fondues1':fondues1, 'petits1':petits1, 'mshakes1':mshakes1, 'sorvetes1':sorvetes1, 'acais1':acais1, 'mixs1':mixs1, 'casadinhos1':casadinhos1, 'cremes1':cremes1, 'produtos1':produtos1, 'comanda_obj':comanda_obj})
    if petit1 != None and adicionais1 != None and comanda_obj != None and pedido2 == None: ## add adicional em petit
        petit1 = petit1.id
        item_adicional = itempetit.objects.filter(id=petit1).get()
        for adicional2 in adicionais1 :
            add_id = int(adicional2)
            addicional = adicional.objects.filter(id=add_id).get()
            item_adicional.adicionais.add(addicional)
            item_adicional.total = item_adicional.total + addicional.preco
            item_adicional.save()
            comanda_obj.total = comanda_obj.total +addicional.preco
            comanda_obj.save()
        acais1 = comanda_obj.acais.all()
        mixs1 = comanda_obj.mixs.all()
        casadinhos1 = comanda_obj.casadinhos.all()
        cremes1 = comanda_obj.cremes.all()
        produtos1 = comanda_obj.produtos.all()
        sorvetes1 = comanda_obj.sorvetes.all()
        mshakes1 = comanda_obj.mshakes.all()
        petits1 = comanda_obj.petits.all()
        fondues1 = comanda_obj.fondues.all()
        return render(request, 'pedidos/finalizar.html',{'title':'Fechamento', 'fondues1':fondues1, 'petits1':petits1, 'mshakes1':mshakes1, 'sorvetes1':sorvetes1, 'acais1':acais1, 'mixs1':mixs1, 'casadinhos1':casadinhos1, 'cremes1':cremes1, 'produtos1':produtos1, 'comanda_obj':comanda_obj})
    if fondue1 != None and adicionais1 != None and comanda_obj != None and pedido2 == None: ## add adicional em fondue
        fondue1 = fondue1.id
        item_adicional = itemfondue.objects.filter(id=fondue1).get()
        for adicional2 in adicionais1 :
            add_id = int(adicional2)
            addicional = adicional.objects.filter(id=add_id).get()
            item_adicional.adicionais.add(addicional)
            item_adicional.total = item_adicional.total + addicional.preco
            item_adicional.save()
            comanda_obj.total = comanda_obj.total +addicional.preco
            comanda_obj.save()
        acais1 = comanda_obj.acais.all()
        mixs1 = comanda_obj.mixs.all()
        casadinhos1 = comanda_obj.casadinhos.all()
        cremes1 = comanda_obj.cremes.all()
        produtos1 = comanda_obj.produtos.all()
        sorvetes1 = comanda_obj.sorvetes.all()
        mshakes1 = comanda_obj.mshakes.all()
        petits1 = comanda_obj.petits.all()
        fondues1 = comanda_obj.fondues.all()
        return render(request, 'pedidos/finalizar.html',{'title':'Fechamento', 'fondues1':fondues1, 'petits1':petits1, 'mshakes1':mshakes1, 'sorvetes1':sorvetes1, 'acais1':acais1, 'mixs1':mixs1, 'casadinhos1':casadinhos1, 'cremes1':cremes1, 'produtos1':produtos1, 'comanda_obj':comanda_obj})
    
    return render(request, 'pedidos/finalizar.html',{'title':'Fechamento','comanda_id':comanda_id})

def metodo(request):
    comanda_id = request.GET.get('comanda_id')
    comanda_atual = comanda.objects.filter(id=comanda_id).get()
    senha1 = senha.objects.latest('id')
    """Epson = printer.Usb(0x04b8,0x0202)
    acais1 = comanda_atual.acais.all()
    mixs1 = comanda_atual.mixs.all()
    casadinhos1 = comanda_atual.casadinhos.all()
    produtos1 = comanda_atual.produtos.all()
    cremes1 = comanda_atual.cremes.all()
    sorvetes1 = comanda_atual.sorvetes.all()
    mshakes1 = comanda_atual.mshakes.all()
    petits1 = comanda_atual.petits.all()
    fondues1 = comanda_atual.fondues.all()
    sucos1 = comanda_atual.sucos.all()
    Epson.set(align='center')
    Epson.text("C O N F E R E N C I A   C O Z I N H A \n\n")
    Epson.text("Comanda N: " + str(comanda_atual.id))
    Epson.text('\n')
    if senha1.numero <= 15:
        senha1.numero = senha1.numero + 1
        senha1.save()
    else:
        senha1.numero = 1
        senha1.save()
    Epson.set(align='left')
    Epson.text('Senha.......'+str(senha1)+'\n\n')
    Epson.text('------------------------------------------------\n')
    
    for acais in acais1:
        Epson.text("Acai : " + str(acais.acai_item.nome))
        Epson.text('\n')
        Epson.text('\n')
        Epson.text("Tamanho : " + str(acais.acai_item.tamanho))
        Epson.text('\n')
        Epson.text('\n')
        adds = acais.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
            Epson.text('------------------------------------------------\n')
            Epson.text('\n')
            Epson.text('\n')
    for mixs in mixs1:
        Epson.text("Mix : " + str(mixs.mix_item.nome))
        Epson.text('\n')
        Epson.text('\n')
        Epson.text("Tamanho : " + str(mixs.mix_item.tamanho))
        Epson.text('\n')
        Epson.text('\n')
        adds = mixs.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
            Epson.text('------------------------------------------------\n')
            Epson.text('\n')
            Epson.text('\n')
    for casadinhos in casadinhos1:
        Epson.text("Mix : " + str(casadinhos.casadinho_item.nome))
        Epson.text('\n')
        Epson.text('\n')
        Epson.text("Tamanho : " + str(casadinhos.casadinho_item.tamanho))
        Epson.text('\n')
        Epson.text('\n')
        adds = casadinhos.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
            Epson.text('------------------------------------------------\n')
            Epson.text('\n')
            Epson.text('\n')
    for produtos in produtos1:
        Epson.text("Produto : " + str(produtos.produto_item.nome))
        Epson.text('\n')
        Epson.text("Qnt : " + str(produtos.qnt) +"\n")
        Epson.text('------------------------------------------------\n')
        Epson.text('\n')
        Epson.text('\n')
    for sucos in sucos1:
        Epson.text("Suco : " + str(sucos.suco_item.nome))
        Epson.text('\n')
        Epson.text("Qnt : " + str(sucos.qnt) +"\n")
        Epson.text('------------------------------------------------\n')
        Epson.text('\n')
        Epson.text('\n')
    for cremes in cremes1:
        Epson.text("Creme Acai : " + str(cremes.creme_item.nome))
        Epson.text('\n')
        Epson.text('\n')
        Epson.text("Tamanho : " + str(cremes.creme_item.tamanho))
        Epson.text('\n')
        Epson.text('\n')
        adds = cremes.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
            Epson.text('------------------------------------------------\n')
            Epson.text('\n')
            Epson.text('\n')
    for sorvetes in sorvetes1:
        Epson.text("Sorvete : " + str(sorvetes.sorvete_item.nome))
        Epson.text('\n')
        Epson.text('\n')
        adds = sorvetes.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
            Epson.text('------------------------------------------------\n')
            Epson.text('\n')
            Epson.text('\n')
    for mshakes in mshakes1:
        Epson.text("Milk Shake : " + str(mshakes.mshake_item.nome))
        Epson.text('\n')
        Epson.text('\n')
        Epson.text("Tamanho : " + str(mshakes.mshake_item.tamanho))
        Epson.text('\n')
        Epson.text('\n')
        adds = mshakes.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
            Epson.text('------------------------------------------------\n')
            Epson.text('\n')
            Epson.text('\n')
    for petits in petits1:
        Epson.text("Petit gateau : " + str(petits.petit_item.nome))
        Epson.text('\n')
        Epson.text('\n')
        adds = petits.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
            Epson.text('------------------------------------------------\n')
            Epson.text('\n')
            Epson.text('\n')
    for fondues in fondues1:
        Epson.text("Fondue : " + str(fondues.fondue_item.nome))
        Epson.text('\n')
        Epson.text('\n')
        adds = fondues.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
            Epson.text('------------------------------------------------\n')
            Epson.text('\n')
            Epson.text('\n')
        
    Epson.cut()"""
    
    return render(request, 'metodo.html', {'title':'Metodo de pagamento', 'comanda_atual':comanda_atual})

def dinheiro(request):
    comanda_id = request.GET.get('comanda_id')
    comanda_obj = comanda.objects.filter(id=comanda_id).get()
    comanda_obj.pagamento = 1
    comanda_obj.save()
    caixa_atual = caixa_geral.objects.latest('id')
    novo_total = caixa_atual.total + comanda_obj.total
    desc = "Venda n: "+str(comanda_obj.id)+"."
    nova_entrada = caixa_geral(operacao=1, tipo=1, id_operacao=comanda_obj.id, valor_operacao=comanda_obj.total, descricao=desc, total=novo_total)
    nova_entrada.save()
    acais1 = comanda_obj.acais.all()
    mixs1 = comanda_obj.mixs.all()
    casadinhos1 = comanda_obj.casadinhos.all()
    produtos1 = comanda_obj.produtos.all()
    cremes1 = comanda_obj.cremes.all()
    sorvetes1 = comanda_obj.sorvetes.all()
    mshakes1 = comanda_obj.mshakes.all()
    petits1 = comanda_obj.petits.all()
    fondues1 = comanda_obj.fondues.all()
    sucos1 = comanda_obj.sucos.all()
    metodo_prep = comanda_obj.get_tipo_display()
    metodo_prep = str(metodo_prep)
    Epson = printer.Usb(0x04b8,0x0202)
    Epson.set(align='center')
    Epson.text('\n')
    Epson.text('\n')
    Epson.text('\n')
    Epson.text("* * * C O Z I N H A * * * \n\n")
    Epson.text('\n')
    Epson.set(bold=True)
    Epson.text("--> "+ str(metodo_prep) +" <--")
    Epson.text('\n')
    Epson.text('\n')
    Epson.set(bold=False)
    Epson.set(align='left')
    Epson.text("Comanda N: " + str(comanda_obj.id))
    Epson.text('\n')
    Epson.text('------------------------------------------------\n')
    for acais in acais1:
        Epson.set(bold=True)
        Epson.text("Acai : " + str(acais.acai_item.nome))
        Epson.text('\n')
        Epson.text("Acomp: " + str(acais.get_acompanhamento_display()))
        Epson.text('\n')
        Epson.text("Tamanho : " + str(acais.acai_item.tamanho))
        Epson.set(bold=False)
        Epson.text('\n')
        Epson.text('\n')
        adds = acais.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(acais.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    for mixs in mixs1:
        Epson.set(bold=True)
        Epson.text("Mix : " + str(mixs.mix_item.nome))
        Epson.text('\n')
        Epson.text("Acomp: " + str(mixs.get_acompanhamento_display()))
        Epson.text('\n')
        Epson.text("Tamanho : " + str(mixs.mix_item.tamanho))
        Epson.set(bold=False)
        Epson.text('\n')
        Epson.text('\n')
        adds = mixs.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(mixs.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    for casadinhos in casadinhos1:
        Epson.set(bold=True)
        Epson.text("Casadinho : " + str(casadinhos.casadinho_item.nome))
        Epson.text('\n')
        Epson.text("Acomp: " + str(casadinhos.get_acompanhamento_display()))
        Epson.text('\n')
        Epson.text("Tamanho : " + str(casadinhos.casadinho_item.tamanho))
        Epson.set(bold=False)
        Epson.text('\n')
        Epson.text('\n')
        adds = casadinhos.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(casadinhos.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    for sucos in sucos1:
        Epson.text("Suco : " + str(sucos.suco_item.nome))
        Epson.text('\n')
        Epson.text("Qnt : " + str(sucos.qnt) +"\n")
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(sucos.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    for cremes in cremes1:
        Epson.set(bold=True)
        Epson.text("Creme : " + str(cremes.creme_item.nome))
        Epson.text('\n')
        Epson.text("Acomp: " + str(cremes.get_acompanhamento_display()))
        Epson.text('\n')
        Epson.text("Tamanho : " + str(cremos.creme_item.tamanho))
        Epson.set(bold=False)
        Epson.text('\n')
        Epson.text('\n')
        adds = cremes.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(cremes.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    for sorvetes in sorvetes1:
        Epson.set(bold=True)
        Epson.text("Sorvete : " + str(sorvetes.sorvete_item.nome))
        Epson.set(bold=False)
        Epson.text('\n')
        Epson.text('\n')
        adds = sorvetes.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(sorvetes.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    for mshakes in mshakes1:
        Epson.set(bold=True)
        Epson.text("Milk Shake : " + str(mshakes.mshake_item.nome))
        Epson.text('\n')
        Epson.text("Tamanho : " + str(mshakes.mshake_item.tamanho))
        Epson.set(bold=False)
        Epson.text('\n')
        Epson.text('\n')
        adds = mshakes.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(mshakes.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    for petits in petits1:
        Epson.set(bold=True)
        Epson.text("Petit gateau : " + str(petits.petit_item.nome))
        Epson.set(bold=False)
        Epson.text('\n')
        Epson.text('\n')
        adds = petits.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(petits.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    for fondues in fondues1:
        Epson.set(bold=True)
        Epson.text("Fondue : " + str(fondues.fondue_item.nome))
        Epson.set(bold=False)
        Epson.text('\n')
        Epson.text('\n')
        adds = fondues.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(fondues.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    for produtos in produtos1:
        Epson.set(bold=True)
        Epson.text("Produto : " + str(produtos.produto_item.nome))
        Epson.text('\n')
        Epson.text("Qnt : " + str(produtos.qnt) +"\n")
        Epson.set(bold=False)
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(produtos.total)+'\n')
        Epson.set(align='left')
    Epson.set(bold=False)
    Epson.cut()

    return render(request, 'pedidos/dinheiro.html',{'title':'Pagamento em dinheiro', 'comanda_obj':comanda_obj})

def cartao_debito(request):
    comanda_id = request.GET.get('comanda_id')
    comanda_obj = comanda.objects.filter(id=comanda_id).get()
    comanda_obj.pagamento = 2
    comanda_obj.save()
    caixa_atual = caixa_geral.objects.latest('id')
    item_caixa = str(comanda_obj.id)
    novo_total = caixa_atual.total + comanda_obj.total
    desc = "Venda n: "+str(comanda_obj.id)+"."
    nova_entrada = caixa_geral(operacao=1, tipo=2, id_operacao=comanda_obj.id, valor_operacao=comanda_obj.total, descricao=desc, total=novo_total)
    nova_entrada.save()
    acais1 = comanda_obj.acais.all()
    mixs1 = comanda_obj.mixs.all()
    casadinhos1 = comanda_obj.casadinhos.all()
    produtos1 = comanda_obj.produtos.all()
    cremes1 = comanda_obj.cremes.all()
    sorvetes1 = comanda_obj.sorvetes.all()
    mshakes1 = comanda_obj.mshakes.all()
    petits1 = comanda_obj.petits.all()
    fondues1 = comanda_obj.fondues.all()
    sucos1 = comanda_obj.sucos.all()
    metodo_prep = comanda_obj.get_tipo_display()
    metodo_prep = str(metodo_prep)
    Epson = printer.Usb(0x04b8,0x0202)
    Epson.set(align='center')
    Epson.text('\n')
    Epson.text('\n')
    Epson.text('\n')
    Epson.text("* * * C O Z I N H A * * * \n\n")
    Epson.text('\n')
    Epson.set(bold=True)
    Epson.text("--> "+ str(metodo_prep) +" <--")
    Epson.text('\n')
    Epson.text('\n')
    Epson.set(bold=False)
    Epson.set(align='left')
    Epson.text("Comanda N: " + str(comanda_obj.id))
    Epson.text('\n')
    Epson.text('------------------------------------------------\n')
    for acais in acais1:
        Epson.set(bold=True)
        Epson.text("Acai : " + str(acais.acai_item.nome))
        Epson.text('\n')
        Epson.text("Acomp: " + str(acais.get_acompanhamento_display()))
        Epson.text('\n')
        Epson.text("Tamanho : " + str(acais.acai_item.get_tamanho_display()))
        Epson.set(bold=False)
        Epson.text('\n')
        Epson.text('\n')
        adds = acais.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(acais.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    for mixs in mixs1:
        Epson.set(bold=True)
        Epson.text("Mix : " + str(mixs.mix_item.nome))
        Epson.text('\n')
        Epson.text("Acomp: " + str(mixs.get_acompanhamento_display()))
        Epson.text('\n')
        Epson.text("Tamanho : " + str(mixs.mix_item.get_tamanho_display()))
        Epson.set(bold=False)
        Epson.text('\n')
        Epson.text('\n')
        adds = mixs.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(mixs.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    for casadinhos in casadinhos1:
        Epson.set(bold=True)
        Epson.text("Casadinho : " + str(casadinhos.casadinho_item.nome))
        Epson.text('\n')
        Epson.text("Acomp: " + str(casadinhos.get_acompanhamento_display()))
        Epson.text('\n')
        Epson.text("Tamanho : " + str(casadinhos.casadinho_item.get_tamanho_display()))
        Epson.set(bold=False)
        Epson.text('\n')
        Epson.text('\n')
        adds = casadinhos.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(casadinhos.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    for sucos in sucos1:
        Epson.text("Suco : " + str(sucos.suco_item.nome))
        Epson.text('\n')
        Epson.text("Qnt : " + str(sucos.qnt) +"\n")
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(sucos.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    for cremes in cremes1:
        Epson.set(bold=True)
        Epson.text("Creme : " + str(cremes.creme_item.nome))
        Epson.text('\n')
        Epson.text("Acomp: " + str(cremes.get_acompanhamento_display()))
        Epson.text('\n')
        Epson.text("Tamanho : " + str(cremos.creme_item.get_tamanho_display()))
        Epson.set(bold=False)
        Epson.text('\n')
        Epson.text('\n')
        adds = cremes.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(cremes.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    for sorvetes in sorvetes1:
        Epson.set(bold=True)
        Epson.text("Sorvete : " + str(sorvetes.sorvete_item.nome))
        Epson.set(bold=False)
        Epson.text('\n')
        Epson.text('\n')
        adds = sorvetes.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(sorvetes.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    for mshakes in mshakes1:
        Epson.set(bold=True)
        Epson.text("Milk Shake : " + str(mshakes.mshake_item.nome))
        Epson.text('\n')
        Epson.text("Tamanho : " + str(mshakes.mshake_item.get_tamanho_display()))
        Epson.set(bold=False)
        Epson.text('\n')
        Epson.text('\n')
        adds = mshakes.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(mshakes.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    for petits in petits1:
        Epson.set(bold=True)
        Epson.text("Petit gateau : " + str(petits.petit_item.nome))
        Epson.set(bold=False)
        Epson.text('\n')
        Epson.text('\n')
        adds = petits.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(petits.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    for fondues in fondues1:
        Epson.set(bold=True)
        Epson.text("Fondue : " + str(fondues.fondue_item.nome))
        Epson.set(bold=False)
        Epson.text('\n')
        Epson.text('\n')
        adds = fondues.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(fondues.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    for produtos in produtos1:
        Epson.set(bold=True)
        Epson.text("Produto : " + str(produtos.produto_item.nome))
        Epson.text('\n')
        Epson.text("Qnt : " + str(produtos.qnt) +"\n")
        Epson.set(bold=False)
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(produtos.total)+'\n')
        Epson.set(align='left')
    Epson.set(bold=False)
    Epson.cut()

    return render(request, 'pedidos/troco.html',{'title':'Pagamento em cartao', 'comanda_obj':comanda_obj, 'recebido':str(comanda_obj.total), 'troco':str(0.00)})

def cartao_credito(request):
    comanda_id = request.GET.get('comanda_id')
    comanda_obj = comanda.objects.filter(id=comanda_id).get()
    comanda_obj.pagamento = 3
    comanda_obj.save()
    caixa_atual = caixa_geral.objects.latest('id')
    item_caixa = str(comanda_obj.id)
    novo_total = caixa_atual.total + comanda_obj.total
    desc = "Venda n: "+str(comanda_obj.id)+"."
    nova_entrada = caixa_geral(operacao=1, tipo=3, id_operacao=comanda_obj.id, valor_operacao=comanda_obj.total, descricao=desc, total=novo_total)
    nova_entrada.save()
    acais1 = comanda_obj.acais.all()
    mixs1 = comanda_obj.mixs.all()
    casadinhos1 = comanda_obj.casadinhos.all()
    produtos1 = comanda_obj.produtos.all()
    cremes1 = comanda_obj.cremes.all()
    sorvetes1 = comanda_obj.sorvetes.all()
    mshakes1 = comanda_obj.mshakes.all()
    petits1 = comanda_obj.petits.all()
    fondues1 = comanda_obj.fondues.all()
    sucos1 = comanda_obj.sucos.all()
    metodo_prep = comanda_obj.get_tipo_display()
    metodo_prep = str(metodo_prep)
    Epson = printer.Usb(0x04b8,0x0202)
    Epson.set(align='center')
    Epson.text('\n')
    Epson.text('\n')
    Epson.text('\n')
    Epson.text("* * * C O Z I N H A * * * \n\n")
    Epson.text('\n')
    Epson.set(bold=True)
    Epson.text("--> "+ str(metodo_prep) +" <--")
    Epson.text('\n')
    Epson.text('\n')
    Epson.set(bold=False)
    Epson.set(align='left')
    Epson.text("Comanda N: " + str(comanda_obj.id))
    Epson.text('\n')
    Epson.text('------------------------------------------------\n')
    for acais in acais1:
        Epson.set(bold=True)
        Epson.text("Acai : " + str(acais.acai_item.nome))
        Epson.text('\n')
        Epson.text("Acomp: " + str(acais.get_acompanhamento_display()))
        Epson.text('\n')
        Epson.text("Tamanho : " + str(acais.acai_item.get_tamanho_display()))
        Epson.set(bold=False)
        Epson.text('\n')
        Epson.text('\n')
        adds = acais.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(acais.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    for mixs in mixs1:
        Epson.set(bold=True)
        Epson.text("Mix : " + str(mixs.mix_item.nome))
        Epson.text('\n')
        Epson.text("Acomp: " + str(mixs.get_acompanhamento_display()))
        Epson.text('\n')
        Epson.text("Tamanho : " + str(mixs.mix_item.get_tamanho_display()))
        Epson.set(bold=False)
        Epson.text('\n')
        Epson.text('\n')
        adds = mixs.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(mixs.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    for casadinhos in casadinhos1:
        Epson.set(bold=True)
        Epson.text("Casadinho : " + str(casadinhos.casadinho_item.nome))
        Epson.text('\n')
        Epson.text("Acomp: " + str(casadinhos.get_acompanhamento_display()))
        Epson.text('\n')
        Epson.text("Tamanho : " + str(casadinhos.casadinho_item.get_tamanho_display()))
        Epson.set(bold=False)
        Epson.text('\n')
        Epson.text('\n')
        adds = casadinhos.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(casadinhos.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    for sucos in sucos1:
        Epson.text("Suco : " + str(sucos.suco_item.nome))
        Epson.text('\n')
        Epson.text("Qnt : " + str(sucos.qnt) +"\n")
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(sucos.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    for cremes in cremes1:
        Epson.set(bold=True)
        Epson.text("Creme : " + str(cremes.creme_item.nome))
        Epson.text('\n')
        Epson.text("Acomp: " + str(cremes.get_acompanhamento_display()))
        Epson.text('\n')
        Epson.text("Tamanho : " + str(cremos.creme_item.get_tamanho_display()))
        Epson.set(bold=False)
        Epson.text('\n')
        Epson.text('\n')
        adds = cremes.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(cremes.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    for sorvetes in sorvetes1:
        Epson.set(bold=True)
        Epson.text("Sorvete : " + str(sorvetes.sorvete_item.nome))
        Epson.set(bold=False)
        Epson.text('\n')
        Epson.text('\n')
        adds = sorvetes.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(sorvetes.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    for mshakes in mshakes1:
        Epson.set(bold=True)
        Epson.text("Milk Shake : " + str(mshakes.mshake_item.nome))
        Epson.text('\n')
        Epson.text("Tamanho : " + str(mshakes.mshake_item.get_tamanho_display()))
        Epson.set(bold=False)
        Epson.text('\n')
        Epson.text('\n')
        adds = mshakes.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(mshakes.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    for petits in petits1:
        Epson.set(bold=True)
        Epson.text("Petit gateau : " + str(petits.petit_item.nome))
        Epson.set(bold=False)
        Epson.text('\n')
        Epson.text('\n')
        adds = petits.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(petits.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    for fondues in fondues1:
        Epson.set(bold=True)
        Epson.text("Fondue : " + str(fondues.fondue_item.nome))
        Epson.set(bold=False)
        Epson.text('\n')
        Epson.text('\n')
        adds = fondues.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(fondues.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    for produtos in produtos1:
        Epson.set(bold=True)
        Epson.text("Produto : " + str(produtos.produto_item.nome))
        Epson.text('\n')
        Epson.text("Qnt : " + str(produtos.qnt) +"\n")
        Epson.set(bold=False)
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(produtos.total)+'\n')
        Epson.set(align='left')
    Epson.set(bold=False)
    Epson.cut()

    return render(request, 'pedidos/troco.html',{'title':'Pagamento em cartao', 'comanda_obj':comanda_obj, 'recebido':str(comanda_obj.total), 'troco':str(0.00)})

def delivery(request):
    comanda_id = request.GET.get('comanda_id')
    troco = request.GET.get('troco')
    comanda_obj = comanda.objects.filter(id=comanda_id).get()
    acais1 = comanda_obj.acais.all()
    mixs1 = comanda_obj.mixs.all()
    casadinhos1 = comanda_obj.casadinhos.all()
    produtos1 = comanda_obj.produtos.all()
    cremes1 = comanda_obj.cremes.all()
    sorvetes1 = comanda_obj.sorvetes.all()
    mshakes1 = comanda_obj.mshakes.all()
    petits1 = comanda_obj.petits.all()
    fondues1 = comanda_obj.fondues.all()
    sucos1 = comanda_obj.sucos.all()
    met_pagamento = comanda_obj.get_pagamento_display()
    met_pagamento = str(met_pagamento)
    tel1 = comanda_obj.cli.telefone1
    tel1 = str(tel1)
    tel2 = comanda_obj.cli.telefone2
    tel2 = str(tel2)
    end = comanda_obj.cli.endereco
    end = str(end)
    num= comanda_obj.cli.numero
    num = str(num)
    bai = comanda_obj.cli.bairro
    bai = str(bai)
    ref = comanda_obj.cli.referencia
    ref = str(ref)

    Epson = printer.Usb(0x04b8,0x0202)
    Epson.set(align='center')
    Epson.set(bold=True)
    Epson.text("* * * E N T R E G A * * * \n\n")
    Epson.set(bold=False)
    Epson.text('\n')
    Epson.set(align='left')
    Epson.text("Comanda N: " + str(comanda_obj.id))
    Epson.text('\n')
    Epson.text('------------------------------------------------\n')
    for acais in acais1:
        Epson.set(bold=True)
        Epson.text("Acai : " + str(acais.acai_item.nome))
        Epson.text('\n')
        Epson.text("Acomp: " + str(acais.get_acompanhamento_display()))
        Epson.text('\n')
        Epson.text("Tamanho : " + str(acais.acai_item.get_tamanho_display()))
        Epson.set(bold=False)
        Epson.text('\n')
        Epson.text('\n')
        adds = acais.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(acais.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    for mixs in mixs1:
        Epson.set(bold=True)
        Epson.text("Mix : " + str(mixs.mix_item.nome))
        Epson.text('\n')
        Epson.text("Acomp: " + str(mixs.get_acompanhamento_display()))
        Epson.text('\n')
        Epson.text("Tamanho : " + str(mixs.mix_item.get_tamanho_display()))
        Epson.set(bold=False)
        Epson.text('\n')
        Epson.text('\n')
        adds = mixs.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(mixs.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    for casadinhos in casadinhos1:
        Epson.set(bold=True)
        Epson.text("Casadinho : " + str(casadinhos.casadinho_item.nome))
        Epson.text('\n')
        Epson.text("Acomp: " + str(casadinhos.get_acompanhamento_display()))
        Epson.text('\n')
        Epson.text("Tamanho : " + str(casadinhos.casadinho_item.get_tamanho_display()))
        Epson.set(bold=False)
        Epson.text('\n')
        Epson.text('\n')
        adds = casadinhos.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(casadinhos.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    for sucos in sucos1:
        Epson.text("Suco : " + str(sucos.suco_item.nome))
        Epson.text('\n')
        Epson.text("Qnt : " + str(sucos.qnt) +"\n")
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(sucos.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    for cremes in cremes1:
        Epson.set(bold=True)
        Epson.text("Creme : " + str(cremes.creme_item.nome))
        Epson.text('\n')
        Epson.text("Acomp: " + str(cremes.get_acompanhamento_display()))
        Epson.text('\n')
        Epson.text("Tamanho : " + str(cremos.creme_item.get_tamanho_display()))
        Epson.set(bold=False)
        Epson.text('\n')
        Epson.text('\n')
        adds = cremes.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(cremes.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    for sorvetes in sorvetes1:
        Epson.set(bold=True)
        Epson.text("Sorvete : " + str(sorvetes.sorvete_item.nome))
        Epson.set(bold=False)
        Epson.text('\n')
        Epson.text('\n')
        adds = sorvetes.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(sorvetes.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    for mshakes in mshakes1:
        Epson.set(bold=True)
        Epson.text("Milk Shake : " + str(mshakes.mshake_item.nome))
        Epson.text('\n')
        Epson.text("Tamanho : " + str(mshakes.mshake_item.get_tamanho_display()))
        Epson.set(bold=False)
        Epson.text('\n')
        Epson.text('\n')
        adds = mshakes.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(mshakes.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    for petits in petits1:
        Epson.set(bold=True)
        Epson.text("Petit gateau : " + str(petits.petit_item.nome))
        Epson.set(bold=False)
        Epson.text('\n')
        Epson.text('\n')
        adds = petits.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(petits.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    for fondues in fondues1:
        Epson.set(bold=True)
        Epson.text("Fondue : " + str(fondues.fondue_item.nome))
        Epson.set(bold=False)
        Epson.text('\n')
        Epson.text('\n')
        adds = fondues.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(fondues.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    for produtos in produtos1:
        Epson.set(bold=True)
        Epson.text("Produto : " + str(produtos.produto_item.nome))
        Epson.text('\n')
        Epson.text("Qnt : " + str(produtos.qnt) +"\n")
        Epson.set(bold=False)
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(produtos.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    Epson.text('\n')
    Epson.set(align='center')
    Epson.set(bold=True)
    Epson.text('Metodo: '+str(met_pagamento))
    Epson.text('\n')
    Epson.text('Valor: R$'+str(comanda_obj.total))
    Epson.text('\n')
    Epson.text('Troco: R$'+str(troco))
    Epson.text('\n')
    Epson.text('\n')
    Epson.text(str(comanda_obj.cli.nome))
    Epson.text('\n')
    Epson.set(align='left')
    Epson.text('Endereco:')
    Epson.text('\n')
    if end != '':
        Epson.set(align='center')
        Epson.text(str(end)+', '+str(num))
        Epson.text('\n')
        Epson.text(str(bai))
    if ref != '':
        Epson.text('\n')
        Epson.text(str(ref))
    if tel1 != '' or tel2 != '':
        Epson.set(align='left')
        Epson.text('\n')
        Epson.text('Telefone:')
        Epson.text('\n')
        Epson.set(align='center')
        if tel1 != '':
            Epson.text(str(tel1))
        if tel2 != '':
            Epson.text(str(tel2))
    Epson.set(bold=False)
    Epson.cut()
    msg = "Pedido finalizado com sucesso!"
    return render(request, 'home/home.html', {'title':'Home','msg':msg})

def via_cliente(request):
    comanda_id = request.GET.get('comanda_id')
    troco = request.GET.get('troco')
    comanda_obj = comanda.objects.filter(id=comanda_id).get()
    acais1 = comanda_obj.acais.all()
    mixs1 = comanda_obj.mixs.all()
    casadinhos1 = comanda_obj.casadinhos.all()
    produtos1 = comanda_obj.produtos.all()
    cremes1 = comanda_obj.cremes.all()
    sorvetes1 = comanda_obj.sorvetes.all()
    mshakes1 = comanda_obj.mshakes.all()
    petits1 = comanda_obj.petits.all()
    fondues1 = comanda_obj.fondues.all()
    sucos1 = comanda_obj.sucos.all()
    data = comanda_obj.data
    data = data.strftime("%d/%m/%Y - %H:%M")
    Epson = printer.Usb(0x04b8,0x0202)
    Epson.set(align='center')
    Epson.set(bold=True)
    Epson.text("* * * V I A - C L I E N T E * * * \n\n")
    Epson.set(bold=False)
    Epson.text('\n')
    Epson.set(align='left')
    Epson.text('\n')
    Epson.text("Comanda N: " + str(comanda_obj.id))
    Epson.text('\n')
    Epson.text("Data: " + str(data))
    Epson.text('\n')
    Epson.text('------------------------------------------------\n')
    for acais in acais1:
        Epson.set(bold=True)
        Epson.text("Acai : " + str(acais.acai_item.nome))
        Epson.text('\n')
        Epson.text("Acomp: " + str(acais.get_acompanhamento_display()))
        Epson.text('\n')
        Epson.text("Tamanho : " + str(acais.acai_item.get_tamanho_display()))
        Epson.set(bold=False)
        Epson.text('\n')
        Epson.text('\n')
        adds = acais.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(acais.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    for mixs in mixs1:
        Epson.set(bold=True)
        Epson.text("Mix : " + str(mixs.mix_item.nome))
        Epson.text('\n')
        Epson.text("Acomp: " + str(mixs.get_acompanhamento_display()))
        Epson.text('\n')
        Epson.text("Tamanho : " + str(mixs.mix_item.get_tamanho_display()))
        Epson.set(bold=False)
        Epson.text('\n')
        Epson.text('\n')
        adds = mixs.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(mixs.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    for casadinhos in casadinhos1:
        Epson.set(bold=True)
        Epson.text("Casadinho : " + str(casadinhos.casadinho_item.nome))
        Epson.text('\n')
        Epson.text("Acomp: " + str(casadinhos.get_acompanhamento_display()))
        Epson.text('\n')
        Epson.text("Tamanho : " + str(casadinhos.casadinho_item.get_tamanho_display()))
        Epson.set(bold=False)
        Epson.text('\n')
        Epson.text('\n')
        adds = casadinhos.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(casadinhos.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    for sucos in sucos1:
        Epson.text("Suco : " + str(sucos.suco_item.nome))
        Epson.text('\n')
        Epson.text("Qnt : " + str(sucos.qnt) +"\n")
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(sucos.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    for cremes in cremes1:
        Epson.set(bold=True)
        Epson.text("Creme : " + str(cremes.creme_item.nome))
        Epson.text('\n')
        Epson.text("Acomp: " + str(cremes.get_acompanhamento_display()))
        Epson.text('\n')
        Epson.text("Tamanho : " + str(cremos.creme_item.get_tamanho_display()))
        Epson.set(bold=False)
        Epson.text('\n')
        Epson.text('\n')
        adds = cremes.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(cremes.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    for sorvetes in sorvetes1:
        Epson.set(bold=True)
        Epson.text("Sorvete : " + str(sorvetes.sorvete_item.nome))
        Epson.set(bold=False)
        Epson.text('\n')
        Epson.text('\n')
        adds = sorvetes.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(sorvetes.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    for mshakes in mshakes1:
        Epson.set(bold=True)
        Epson.text("Milk Shake : " + str(mshakes.mshake_item.nome))
        Epson.text('\n')
        Epson.text("Tamanho : " + str(mshakes.mshake_item.get_tamanho_display()))
        Epson.set(bold=False)
        Epson.text('\n')
        Epson.text('\n')
        adds = mshakes.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(mshakes.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    for petits in petits1:
        Epson.set(bold=True)
        Epson.text("Petit gateau : " + str(petits.petit_item.nome))
        Epson.set(bold=False)
        Epson.text('\n')
        Epson.text('\n')
        adds = petits.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(petits.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    for fondues in fondues1:
        Epson.set(bold=True)
        Epson.text("Fondue : " + str(fondues.fondue_item.nome))
        Epson.set(bold=False)
        Epson.text('\n')
        Epson.text('\n')
        adds = fondues.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(fondues.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    for produtos in produtos1:
        Epson.set(bold=True)
        Epson.text("Produto : " + str(produtos.produto_item.nome))
        Epson.text('\n')
        Epson.text("Qnt : " + str(produtos.qnt) +"\n")
        Epson.set(bold=False)
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(produtos.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    Epson.text('\n')
    Epson.set(align='center')
    Epson.set(bold=True)
    Epson.text('Metodo: '+str(comanda_obj.get_pagamento_display()))
    Epson.text('\n')
    Epson.text('Valor: R$'+str(comanda_obj.total))
    Epson.text('\n')
    Epson.text('Troco: R$'+str(troco))
    Epson.text('\n')
    Epson.cut()
    
    msg = "Pedido finalizado com sucesso!"
    return render(request, 'home/home.html', {'title':'Home','msg':msg})

def troco(request):
    comanda_id = request.GET.get('comanda_id')
    comanda_obj = comanda.objects.filter(id=comanda_id).get()
    recebido = request.GET.get('recebido')
    troco = Decimal(recebido) - comanda_obj.total 
    """Epson = printer.Usb(0x04b8,0x0202)
    Epson.set(align='center')
    Epson.text('Total : R$'+ str(comanda_obj.total)+'\n')
    Epson.text('Recebido : R$'+str(recebido)+'\n')
    Epson.text('Troco : R$'+str(troco)+'\n')
    Epson.text('Metodo: Dinheiro\n\n\n')
    Epson.text('Obrigado e volte sempre!\n')
    Epson.cashdraw(2)
    Epson.cut()
    Epson.set(align='right')"""
    return render(request, 'pedidos/troco.html',{'title':'Troco', 'comanda_obj':comanda_obj, 'troco':troco, 'recebido':recebido})
def desconto(request):
    comanda_id = request.GET.get('comanda_id')
    comanda_atual = comanda.objects.filter(id=comanda_id).get()
    if request.method == 'POST':
        comanda_id = request.POST.get('comanda_id')
        comanda_atual = comanda.objects.filter(id=comanda_id).get()
        desc = request.POST.get('desc')
        total_desconto = comanda_atual.total - Decimal(desc)
        comanda_atual.total = total_desconto
        comanda_atual.save()
        return render(request, 'metodo.html', {'title':'Metodo de pagamento', 'comanda_atual':comanda_atual})
    return render(request, 'desconto.html',{'title':'Desconto', 'comanda_atual':comanda_atual})
def finalizar2(request):
    comanda_id = request.GET.get('comanda_id')
    comanda_atual = comanda.objects.filter(id=comanda_id).get()
    acais1 = comanda_atual.acais.all()
    mixs1 = comanda_atual.mixs.all()
    casadinhos1 = comanda_atual.casadinhos.all()
    produtos1 = comanda_atual.produtos.all()
    cremes1 = comanda_atual.cremes.all()
    sorvetes1 = comanda_atual.sorvetes.all()
    mshakes1 = comanda_atual.mshakes.all()
    petits1 = comanda_atual.petits.all()
    fondues1 = comanda_atual.fondues.all()
    sucos1 = comanda_atual.sucos.all()
    Epson = printer.Usb(0x04b8,0x0202)
    Epson.set(align='center')
    Epson.text("C O N F E R E N C I A   S I M P L E S \n\n")
    Epson.text("* * * NAO TEM VALOR FISCAL * * *\n")
    Epson.text("Acai Zero Grau - Tres Lagoas \n \n \n")
    Epson.set(align='left')
    Epson.text("Comanda N: " + str(comanda_atual.id))
    Epson.text('\n')
    Epson.text('------------------------------------------------\n')
    for acais in acais1:
        Epson.text("Acai : " + str(acais.acai_item.nome))
        Epson.text('\n')
        Epson.text('\n')
        Epson.text("Tamanho : " + str(acais.acai_item.tamanho))
        Epson.text('\n')
        Epson.text('\n')
        adds = acais.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(acais.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    for mixs in mixs1:
        Epson.text("Mix : " + str(mixs.mix_item.nome))
        Epson.text('\n')
        Epson.text('\n')
        Epson.text("Tamanho : " + str(mixs.mix_item.tamanho))
        Epson.text('\n')
        Epson.text('\n')
        adds = mixs.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(mixs.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    for casadinhos in casadinhos1:
        Epson.text("Mix : " + str(casadinhos.casadinho_item.nome))
        Epson.text('\n')
        Epson.text('\n')
        Epson.text("Tamanho : " + str(casadinhos.casadinho_item.tamanho))
        Epson.text('\n')
        Epson.text('\n')
        adds = casadinhos.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(casadinhos.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    for produtos in produtos1:
        Epson.text("Produto : " + str(produtos.produto_item.nome))
        Epson.text('\n')
        Epson.text("Qnt : " + str(produtos.qnt) +"\n")
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(produtos.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    for sucos in sucos1:
        Epson.text("Suco : " + str(sucos.suco_item.nome))
        Epson.text('\n')
        Epson.text("Qnt : " + str(sucos.qnt) +"\n")
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(sucos.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    for cremes in cremes1:
        Epson.text("Creme Acai : " + str(cremes.creme_item.nome))
        Epson.text('\n')
        Epson.text('\n')
        Epson.text("Tamanho : " + str(cremes.creme_item.tamanho))
        Epson.text('\n')
        Epson.text('\n')
        adds = cremes.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(cremes.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    for sorvetes in sorvetes1:
        Epson.text("Sorvete : " + str(sorvetes.sorvete_item.nome))
        Epson.text('\n')
        Epson.text('\n')
        adds = sorvetes.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(sorvetes.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    for mshakes in mshakes1:
        Epson.text("Milk Shake : " + str(mshakes.mshake_item.nome))
        Epson.text('\n')
        Epson.text('\n')
        Epson.text("Tamanho : " + str(mshakes.mshake_item.tamanho))
        Epson.text('\n')
        Epson.text('\n')
        adds = mshakes.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(mshakes.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    for petits in petits1:
        Epson.text("Petit gateau : " + str(petits.petit_item.nome))
        Epson.text('\n')
        Epson.text('\n')
        adds = petits.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(petits.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    for fondues in fondues1:
        Epson.text("Fondue : " + str(fondues.fondue_item.nome))
        Epson.text('\n')
        Epson.text('\n')
        adds = fondues.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(fondues.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    Epson.set(align='center')
    Epson.text('Total : R$'+ str(comanda_atual.total)+'\n')
    Epson.text('Recebido : R$'+str(comanda_atual.total)+'\n')
    Epson.text('Troco : R$ 0,00\n')
    Epson.text('Metodo: Cartao\n\n\n')
    Epson.text('Obrigado e volte sempre!\n')
    Epson.cut()
    Epson.set(align='right')
    msg = "Pedido finalizado com sucesso!"
    return render(request, 'home/home.html', {'title':'Home','msg':msg})
def finalizar1(request):
    comanda_id = request.GET.get('comanda_id')
    comanda_obj = comanda.objects.filter(id=comanda_id).get()
    recebido = request.GET.get('recebido')
    troco = Decimal(recebido) - Decimal(comanda_obj.total)
    acais1 = comanda_obj.acais.all()
    mixs1 = comanda_obj.mixs.all()
    casadinhos1 = comanda_obj.casadinhos.all()
    produtos1 = comanda_obj.produtos.all()
    cremes1 = comanda_obj.cremes.all()
    sorvetes1 = comanda_obj.sorvetes.all()
    mshakes1 = comanda_obj.mshakes.all()
    petits1 = comanda_obj.petits.all()
    fondues1 = comanda_obj.fondues.all()
    sucos1 = comanda_obj.sucos.all()
    """Epson = printer.Usb(0x04b8,0x0202)
    Epson.set(align='center')
    Epson.text("C O N F E R E N C I A   S I M P L E S \n\n")
    Epson.text("* * * NAO TEM VALOR FISCAL * * *\n")
    Epson.text("Acai Zero Grau - Tres Lagoas \n \n \n")
    Epson.set(align='left')
    Epson.text("Comanda N: " + str(comanda_obj.id))
    Epson.text('\n')
    Epson.text('------------------------------------------------\n')
    for acais in acais1:
        Epson.text("Acai : " + str(acais.acai_item.nome))
        Epson.text('\n')
        Epson.text('\n')
        Epson.text("Tamanho : " + str(acais.acai_item.tamanho))
        Epson.text('\n')
        Epson.text('\n')
        adds = acais.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(acais.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    for mixs in mixs1:
        Epson.text("Mix : " + str(mixs.mix_item.nome))
        Epson.text('\n')
        Epson.text('\n')
        Epson.text("Tamanho : " + str(mixs.mix_item.tamanho))
        Epson.text('\n')
        Epson.text('\n')
        adds = mixs.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(mixs.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    for casadinhos in casadinhos1:
        Epson.text("Mix : " + str(casadinhos.casadinho_item.nome))
        Epson.text('\n')
        Epson.text('\n')
        Epson.text("Tamanho : " + str(casadinhos.casadinho_item.tamanho))
        Epson.text('\n')
        Epson.text('\n')
        adds = casadinhos.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(casadinhos.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    for produtos in produtos1:
        Epson.text("Produto : " + str(produtos.produto_item.nome))
        Epson.text('\n')
        Epson.text("Qnt : " + str(produtos.qnt) +"\n")
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(produtos.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    for sucos in sucos1:
        Epson.text("Suco : " + str(sucos.suco_item.nome))
        Epson.text('\n')
        Epson.text("Qnt : " + str(sucos.qnt) +"\n")
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(sucos.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    for cremes in cremes1:
        Epson.text("Creme Acai : " + str(cremes.creme_item.nome))
        Epson.text('\n')
        Epson.text('\n')
        Epson.text("Tamanho : " + str(cremes.creme_item.tamanho))
        Epson.text('\n')
        Epson.text('\n')
        adds = cremes.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(cremes.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    for sorvetes in sorvetes1:
        Epson.text("Sorvete : " + str(sorvetes.sorvete_item.nome))
        Epson.text('\n')
        Epson.text('\n')
        adds = sorvetes.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(sorvetes.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    for mshakes in mshakes1:
        Epson.text("Milk Shake : " + str(mshakes.mshake_item.nome))
        Epson.text('\n')
        Epson.text('\n')
        Epson.text("Tamanho : " + str(mshakes.mshake_item.tamanho))
        Epson.text('\n')
        Epson.text('\n')
        adds = mshakes.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(mshakes.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    for petits in petits1:
        Epson.text("Petit gateau : " + str(petits.petit_item.nome))
        Epson.text('\n')
        Epson.text('\n')
        adds = petits.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(petits.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    for fondues in fondues1:
        Epson.text("Fondue : " + str(fondues.fondue_item.nome))
        Epson.text('\n')
        Epson.text('\n')
        adds = fondues.adicionais.all()
        if adds != None:
            Epson.text('Adicionais:')
            Epson.text('\n')
            for adicionais in adds:
                Epson.text("   - " + str(adicionais))
                Epson.text('\n')
        Epson.text('\n')
        Epson.text('\n')
        Epson.set(align='right')
        Epson.text('Total : R$'+str(fondues.total)+'\n')
        Epson.set(align='left')
        Epson.text('------------------------------------------------\n')
    Epson.set(align='center')
    Epson.text('Total : R$'+ str(comanda_atual.total)+'\n')
    Epson.text('Recebido : R$'+str(recebido)+'\n')
    Epson.text('Troco : R$'+str(troco)+'\n')
    Epson.text('Metodo: Dinheiro\n\n\n')
    Epson.text('Obrigado e volte sempre!\n')
    Epson.cut()
    Epson.set(align='right')"""
    msg = "Pedido finalizado com sucesso!"
    return render(request, 'home/home.html', {'title':'Home','msg':msg})