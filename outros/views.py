#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from pedidos.models import produto , sorvete, adicional, acai, mix, casadinho, creme, mshake, petit, fondue, suco

# Create your views here.
def outros(request):
    return render(request, 'outros.html', {'title':'Outros'})

def addacai(request):
    adicionais = adicional.objects.all()
    if request.method == 'POST':
        acai_nome = request.POST.get('nome')
        acai_tamanho = request.POST.get('tamanho')
        acai_img = request.POST.get('img')
        acai_preco = request.POST.get('preco')
        acai_add = request.POST.getlist('adicional')
        novo_acai = acai(nome=acai_nome, tamanho=acai_tamanho, img=acai_img, preco=acai_preco)
        novo_acai.save()
        msg = "Açaí salvo com sucesso!"
        return render(request, 'home/home.html',{'title':'Home', 'msg':msg})
    return render(request, 'addacai.html', {'title':'Add Acai', 'adicionais':adicionais})
def addcasadinho(request):
    adicionais = adicional.objects.all()
    if request.method == 'POST':
        casadinho_nome = request.POST.get('nome')
        casadinho_tamanho = request.POST.get('tamanho')
        casadinho_img = request.POST.get('img')
        casadinho_preco = request.POST.get('preco')
        casadinho_add = request.POST.getlist('adicional')
        novo_casadinho = casadinho(nome=casadinho_nome, tamanho=casadinho_tamanho, img=casadinho_img, preco=casadinho_preco)
        novo_casadinho.save()
        msg = "Mix salvo com sucesso!"
        return render(request, 'home/home.html',{'title':'Home', 'msg':msg})
    return render(request, 'addmix.html', {'title':'Add Mix'})
def addmix(request):
    adicionais = adicional.objects.all()
    if request.method == 'POST':
        mix_nome = request.POST.get('nome')
        mix_tamanho = request.POST.get('tamanho')
        mix_img = request.POST.get('img')
        mix_preco = request.POST.get('preco')
        mix_add = request.POST.getlist('adicional')
        novo_mix = mix(nome=mix_nome, tamanho=mix_tamanho, img=mix_img, preco=mix_preco)
        novo_mix.save()
        msg = "Mix salvo com sucesso!"
        return render(request, 'home/home.html',{'title':'Home', 'msg':msg})
    return render(request, 'addmix.html', {'title':'Add Mix'})
def addcreme(request):
    adicionais = adicional.objects.all()
    if request.method == 'POST':
        creme_nome = request.POST.get('nome')
        creme_tamanho = request.POST.get('tamanho')
        creme_img = request.POST.get('img')
        creme_preco = request.POST.get('preco')
        creme_add = request.POST.getlist('adicional')
        novo_creme = creme(nome=creme_nome, tamanho=creme_tamanho, img=creme_img, preco=creme_preco)
        novo_creme.save()
        msg = "Creme salvo com sucesso!"
        return render(request, 'home/home.html',{'title':'Home', 'msg':msg})
    return render(request, 'addcreme.html', {'title':'Add Creme', 'adicionais':adicionais})
def addproduto(request):
    if request.method == 'POST':
        prod_nome = request.POST.get('nome')
        prod_img = request.POST.get('img')
        prod_preco = request.POST.get('preco')
        novo_prod = produto(nome=prod_nome, img=prod_img, preco=prod_preco)
        novo_prod.save()
        msg = "Produto salvo com sucesso!"
        return render(request, 'home/home.html',{'title':'Home', 'msg':msg})
    return render(request, 'addproduto.html', {'title':'Add Produto'})
def addsorvete(request):
    if request.method == 'POST':
        sorv_nome = request.POST.get('nome')
        sorv_img = request.POST.get('img')
        sorv_preco = request.POST.get('preco')
        novo_sorv = sorvete(nome=sorv_nome, img=sorv_nome, preco=sorv_preco)
        novo_sorv.save()
        msg = "Sorvete salvo com sucesso!"
        return render(request, 'home/home.html',{'title':'Home', 'msg':msg})
    return render(request, 'addsorvete.html', {'title':'Add Sorvete'})
def addmshake(request):
    if request.method == 'POST':
        mshake_nome = request.POST.get('nome')
        mshake_img = request.POST.get('img')
        mshake_preco = request.POST.get('preco')
        mshake_tamanho = request.POST.get('tamanho')
        novo_mshake = mshake(nome=mshake_nome, img=mshake_img, preco=mshake_preco, tamanho=mshake_tamanho)
        novo_mshake.save()
        msg = "Milk Shake salvo com sucesso!"
        return render(request, 'home/home.html',{'title':'Home', 'msg':msg})
    return render(request, 'addmshake.html', {'title':'Add Milk Shake'})
def addpetit(request):
    if request.method == 'POST':
        petit_nome = request.POST.get('nome')
        petit_img = request.POST.get('img')
        petit_preco = request.POST.get('preco')
        novo_petit = petit(nome=petit_nome, img=petit_img, preco=petit_preco)
        novo_petit.save()
        msg = "Petit Gateau salvo com sucesso!"
        return render(request, 'home/home.html',{'title':'Home', 'msg':msg})
    return render(request, 'addpetit.html', {'title':'Add Petit Gateau'})
def addfondue(request):
    if request.method == 'POST':
        fond_nome = request.POST.get('nome')
        fond_img = request.POST.get('img')
        fond_preco = request.POST.get('preco')
        novo_fond = fondue(nome=fond_nome, img=fond_img, preco=fond_preco)
        novo_fond.save()
        msg = "Fondue salvo com sucesso!"
        return render(request, 'home/home.html',{'title':'Home', 'msg':msg})
    return render(request, 'addfondue.html', {'title':'Add Fondue'})
def addsuco(request):
    if request.method == 'POST':
        suco_nome = request.POST.get('nome')
        suco_img = request.POST.get('img')
        suco_preco = request.POST.get('preco')
        novo_suco = suco(nome=suco_nome, img=suco_img, preco=suco_preco)
        novo_suco.save()
        msg = "Suco salvo com sucesso!"
        return render(request, 'home/home.html',{'title':'Home', 'msg':msg})
    return render(request, 'addsuco.html', {'title':'Add Suco'})

def addadicional(request):
    return render(request, 'addadicional.html', {'title':'Add Adicional'})

