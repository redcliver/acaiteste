from django.db import models
from cliente.models import cliente

from django.utils import timezone

# Create your models here.
class adicional(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    img = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.nome

class acai(models.Model):
    SIZES = (
        ('P', 'Pequeno'),
        ('G', 'Grande'),
        ('S', 'GG'),
    )
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    img = models.CharField(max_length=200, null=True, blank=True)
    tamanho = models.CharField(max_length=1, choices=SIZES)
    adicionais = models.ManyToManyField(adicional)
    def __str__(self):
        return self.nome

class itemacai(models.Model):
    ACOMP = (
        ('N', 'Nada'),
        ('M', 'Mel'),
        ('L', 'Leite Condensado'),
    )
    id = models.AutoField(primary_key=True)
    acai_item = models.ForeignKey(acai, on_delete=models.CASCADE)
    acompanhamento = models.CharField(max_length=1, choices=ACOMP, default="N")
    adicionais = models.ManyToManyField(adicional)
    obs = models.CharField(max_length=200, null=True, blank=True)
    qnt = models.IntegerField(default=1)
    total = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return str(self.id)

class mix(models.Model):
    SIZES = (
        ('P', 'Pequeno'),
        ('G', 'Grande'),
    )
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    img = models.CharField(max_length=200, null=True, blank=True)
    tamanho = models.CharField(max_length=1, choices=SIZES)
    adicionais = models.ManyToManyField(adicional)
    def __str__(self):
        return self.nome

class itemmix(models.Model):
    ACOMP = (
        ('N', 'Nada'),
        ('M', 'Mel'),
        ('L', 'Leite Condensado'),
    )
    id = models.AutoField(primary_key=True)
    mix_item = models.ForeignKey(mix, on_delete=models.CASCADE)    
    acompanhamento = models.CharField(max_length=1, choices=ACOMP, default="N")
    adicionais = models.ManyToManyField(adicional)
    obs = models.CharField(max_length=200, null=True, blank=True)
    qnt = models.IntegerField(default=1)
    total = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return str(self.id)

class casadinho(models.Model):
    SIZES = (
        ('P', 'Pequeno'),
        ('G', 'Grande'),
    )
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    img = models.CharField(max_length=200, null=True, blank=True)
    tamanho = models.CharField(max_length=1, choices=SIZES)
    adicionais = models.ManyToManyField(adicional)
    def __str__(self):
        return self.nome

class itemcasadinho(models.Model):
    ACOMP = (
        ('N', 'Nada'),
        ('M', 'Mel'),
        ('L', 'Leite Condensado'),
    )
    id = models.AutoField(primary_key=True)
    casadinho_item = models.ForeignKey(casadinho, on_delete=models.CASCADE)
    acompanhamento = models.CharField(max_length=1, choices=ACOMP, default="N")
    adicionais = models.ManyToManyField(adicional)
    obs = models.CharField(max_length=200, null=True, blank=True)
    qnt = models.IntegerField(default=1)
    total = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return str(self.id)

class creme(models.Model):
    SIZES = (
        ('P', 'Pequeno'),
        ('G', 'Grande'),
    )
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    img = models.CharField(max_length=200, null=True, blank=True)
    tamanho = models.CharField(max_length=1, choices=SIZES)
    adicionais = models.ManyToManyField(adicional)
    def __str__(self):
        return self.nome

class itemcreme(models.Model):
    ACOMP = (
        ('N', 'Nada'),
        ('M', 'Mel'),
        ('L', 'Leite Condensado'),
    )
    id = models.AutoField(primary_key=True)
    creme_item = models.ForeignKey(creme, on_delete=models.CASCADE)
    acompanhamento = models.CharField(max_length=1, choices=ACOMP, default="N")
    adicionais = models.ManyToManyField(adicional)
    obs = models.CharField(max_length=200, null=True, blank=True)
    qnt = models.IntegerField(default=1)
    total = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return str(self.id)

class sorvete(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    img = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.nome

class itemsorvete(models.Model):
    id = models.AutoField(primary_key=True)
    sorvete_item = models.ForeignKey(sorvete, on_delete=models.CASCADE)
    adicionais = models.ManyToManyField(adicional)
    obs = models.CharField(max_length=200, null=True, blank=True)
    qnt = models.IntegerField(default=1)
    total = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return str(self.id)

class mshake(models.Model):
    SIZES = (
        ('P', 'Pequeno'),
        ('G', 'Grande'),
    )
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    img = models.CharField(max_length=200, null=True, blank=True)
    tamanho = models.CharField(max_length=1, choices=SIZES)
    def __str__(self):
        return self.nome

class itemmshake(models.Model):
    id = models.AutoField(primary_key=True)
    mshake_item = models.ForeignKey(mshake, on_delete=models.CASCADE)
    adicionais = models.ManyToManyField(adicional)
    obs = models.CharField(max_length=200, null=True, blank=True)
    qnt = models.IntegerField(default=1)
    total = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return str(self.id)
class petit(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    img = models.CharField(max_length=200, null=True, blank=True)
    adicionais = models.ManyToManyField(adicional)
    def __str__(self):
        return self.nome

class itempetit(models.Model):
    id = models.AutoField(primary_key=True)
    petit_item = models.ForeignKey(petit, on_delete=models.CASCADE)
    adicionais = models.ManyToManyField(adicional)
    obs = models.CharField(max_length=200, null=True, blank=True)
    qnt = models.IntegerField(default=1)
    total = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return str(self.id)

class fondue(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    img = models.CharField(max_length=200, null=True, blank=True)
    adicionais = models.ManyToManyField(adicional)
    def __str__(self):
        return self.nome

class itemfondue(models.Model):
    id = models.AutoField(primary_key=True)
    fondue_item = models.ForeignKey(fondue, on_delete=models.CASCADE)
    adicionais = models.ManyToManyField(adicional)
    obs = models.CharField(max_length=200, null=True, blank=True)
    qnt = models.IntegerField(default=1)
    total = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return str(self.id)

class produto(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    img = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.nome

class itemproduto(models.Model):
    id = models.AutoField(primary_key=True)
    produto_item = models.ForeignKey(produto, on_delete=models.CASCADE)
    obs = models.CharField(max_length=200, null=True, blank=True)
    qnt = models.IntegerField(default=1)
    total = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return str(self.id)
class suco(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    img = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.nome

class itemsuco(models.Model):
    ADD = (
        ('L', 'Leite'),
        ('S', 'Sorvete'),
    )
    id = models.AutoField(primary_key=True)
    suco_item = models.ForeignKey(suco, on_delete=models.CASCADE)
    add1 = models.CharField(max_length=1, choices=ADD, null=True, blank=True)
    obs = models.CharField(max_length=200, null=True, blank=True)
    qnt = models.IntegerField(default=1)
    total = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return str(self.id)

class comanda(models.Model):
    TP = (
        ('1', 'Local'),
        ('2', 'Viagem'),
        ('3', 'Entrega'),
        ('4', 'Comanada sem registro'),
    )
    PG = (
        ('1', 'Dinheiro'),
        ('2', 'Cartao Debito'),
        ('3', 'Cartao Credito'),
        ('4', 'Comanada sem registro'),
    )
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=1, choices=TP, default=4)
    pagamento = models.CharField(max_length=1, choices=PG, default=4)
    cli = models.ForeignKey(cliente, null=True, blank=True, on_delete=models.CASCADE)
    acais = models.ManyToManyField(itemacai)
    mixs = models.ManyToManyField(itemmix)
    casadinhos = models.ManyToManyField(itemcasadinho)
    cremes = models.ManyToManyField(itemcreme)
    sorvetes = models.ManyToManyField(itemsorvete)
    mshakes = models.ManyToManyField(itemmshake)
    petits = models.ManyToManyField(itempetit)
    fondues = models.ManyToManyField(itemfondue)
    produtos = models.ManyToManyField(itemproduto)
    sucos = models.ManyToManyField(itemsuco)
    total = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    data = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return str(self.id)