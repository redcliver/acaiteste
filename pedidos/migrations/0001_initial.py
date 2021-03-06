# Generated by Django 2.2.4 on 2019-11-24 13:56

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='acai',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5)),
                ('img', models.CharField(blank=True, max_length=200, null=True)),
                ('tamanho', models.CharField(choices=[('P', 'Pequeno'), ('G', 'Grande'), ('S', 'GG')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='adicional',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5)),
                ('img', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='casadinho',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5)),
                ('img', models.CharField(blank=True, max_length=200, null=True)),
                ('tamanho', models.CharField(choices=[('P', 'Pequeno'), ('G', 'Grande')], max_length=1)),
                ('adicionais', models.ManyToManyField(to='pedidos.adicional')),
            ],
        ),
        migrations.CreateModel(
            name='creme',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5)),
                ('img', models.CharField(blank=True, max_length=200, null=True)),
                ('tamanho', models.CharField(choices=[('P', 'Pequeno'), ('G', 'Grande')], max_length=1)),
                ('adicionais', models.ManyToManyField(to='pedidos.adicional')),
            ],
        ),
        migrations.CreateModel(
            name='fondue',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5)),
                ('img', models.CharField(blank=True, max_length=200, null=True)),
                ('adicionais', models.ManyToManyField(to='pedidos.adicional')),
            ],
        ),
        migrations.CreateModel(
            name='mshake',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5)),
                ('img', models.CharField(blank=True, max_length=200, null=True)),
                ('tamanho', models.CharField(choices=[('P', 'Pequeno'), ('G', 'Grande')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='produto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5)),
                ('img', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='sorvete',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5)),
                ('img', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='suco',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5)),
                ('img', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='petit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5)),
                ('img', models.CharField(blank=True, max_length=200, null=True)),
                ('adicionais', models.ManyToManyField(to='pedidos.adicional')),
            ],
        ),
        migrations.CreateModel(
            name='mix',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5)),
                ('img', models.CharField(blank=True, max_length=200, null=True)),
                ('tamanho', models.CharField(choices=[('P', 'Pequeno'), ('G', 'Grande')], max_length=1)),
                ('adicionais', models.ManyToManyField(to='pedidos.adicional')),
            ],
        ),
        migrations.CreateModel(
            name='itemsuco',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('add1', models.CharField(blank=True, choices=[('L', 'Leite'), ('S', 'Sorvete')], max_length=1, null=True)),
                ('obs', models.CharField(blank=True, max_length=200, null=True)),
                ('qnt', models.IntegerField(default=1)),
                ('total', models.DecimalField(decimal_places=2, max_digits=5)),
                ('suco_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.suco')),
            ],
        ),
        migrations.CreateModel(
            name='itemsorvete',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('obs', models.CharField(blank=True, max_length=200, null=True)),
                ('qnt', models.IntegerField(default=1)),
                ('total', models.DecimalField(decimal_places=2, max_digits=5)),
                ('adicionais', models.ManyToManyField(to='pedidos.adicional')),
                ('sorvete_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.sorvete')),
            ],
        ),
        migrations.CreateModel(
            name='itemproduto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('obs', models.CharField(blank=True, max_length=200, null=True)),
                ('qnt', models.IntegerField(default=1)),
                ('total', models.DecimalField(decimal_places=2, max_digits=5)),
                ('produto_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.produto')),
            ],
        ),
        migrations.CreateModel(
            name='itempetit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('obs', models.CharField(blank=True, max_length=200, null=True)),
                ('qnt', models.IntegerField(default=1)),
                ('total', models.DecimalField(decimal_places=2, max_digits=5)),
                ('adicionais', models.ManyToManyField(to='pedidos.adicional')),
                ('petit_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.petit')),
            ],
        ),
        migrations.CreateModel(
            name='itemmshake',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('obs', models.CharField(blank=True, max_length=200, null=True)),
                ('qnt', models.IntegerField(default=1)),
                ('total', models.DecimalField(decimal_places=2, max_digits=5)),
                ('adicionais', models.ManyToManyField(to='pedidos.adicional')),
                ('mshake_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.mshake')),
            ],
        ),
        migrations.CreateModel(
            name='itemmix',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('acompanhamento', models.CharField(choices=[('N', 'Nada'), ('M', 'Mel'), ('L', 'Leite Condensado')], default='N', max_length=1)),
                ('obs', models.CharField(blank=True, max_length=200, null=True)),
                ('qnt', models.IntegerField(default=1)),
                ('total', models.DecimalField(decimal_places=2, max_digits=5)),
                ('adicionais', models.ManyToManyField(to='pedidos.adicional')),
                ('mix_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.mix')),
            ],
        ),
        migrations.CreateModel(
            name='itemfondue',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('obs', models.CharField(blank=True, max_length=200, null=True)),
                ('qnt', models.IntegerField(default=1)),
                ('total', models.DecimalField(decimal_places=2, max_digits=5)),
                ('adicionais', models.ManyToManyField(to='pedidos.adicional')),
                ('fondue_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.fondue')),
            ],
        ),
        migrations.CreateModel(
            name='itemcreme',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('acompanhamento', models.CharField(choices=[('N', 'Nada'), ('M', 'Mel'), ('L', 'Leite Condensado')], default='N', max_length=1)),
                ('obs', models.CharField(blank=True, max_length=200, null=True)),
                ('qnt', models.IntegerField(default=1)),
                ('total', models.DecimalField(decimal_places=2, max_digits=5)),
                ('adicionais', models.ManyToManyField(to='pedidos.adicional')),
                ('creme_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.creme')),
            ],
        ),
        migrations.CreateModel(
            name='itemcasadinho',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('acompanhamento', models.CharField(choices=[('N', 'Nada'), ('M', 'Mel'), ('L', 'Leite Condensado')], default='N', max_length=1)),
                ('obs', models.CharField(blank=True, max_length=200, null=True)),
                ('qnt', models.IntegerField(default=1)),
                ('total', models.DecimalField(decimal_places=2, max_digits=5)),
                ('adicionais', models.ManyToManyField(to='pedidos.adicional')),
                ('casadinho_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.casadinho')),
            ],
        ),
        migrations.CreateModel(
            name='itemacai',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('acompanhamento', models.CharField(choices=[('N', 'Nada'), ('M', 'Mel'), ('L', 'Leite Condensado')], default='N', max_length=1)),
                ('obs', models.CharField(blank=True, max_length=200, null=True)),
                ('qnt', models.IntegerField(default=1)),
                ('total', models.DecimalField(decimal_places=2, max_digits=5)),
                ('acai_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.acai')),
                ('adicionais', models.ManyToManyField(to='pedidos.adicional')),
            ],
        ),
        migrations.CreateModel(
            name='comanda',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(choices=[('1', 'Local'), ('2', 'Viagem'), ('3', 'Entrega'), ('4', 'Comanada sem registro')], default=4, max_length=1)),
                ('pagamento', models.CharField(choices=[('1', 'Dinheiro'), ('2', 'Cartao Debito'), ('3', 'Cartao Credito'), ('4', 'Comanada sem registro')], default=4, max_length=1)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('data', models.DateTimeField(default=django.utils.timezone.now)),
                ('acais', models.ManyToManyField(to='pedidos.itemacai')),
                ('casadinhos', models.ManyToManyField(to='pedidos.itemcasadinho')),
                ('cli', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cliente.cliente')),
                ('cremes', models.ManyToManyField(to='pedidos.itemcreme')),
                ('fondues', models.ManyToManyField(to='pedidos.itemfondue')),
                ('mixs', models.ManyToManyField(to='pedidos.itemmix')),
                ('mshakes', models.ManyToManyField(to='pedidos.itemmshake')),
                ('petits', models.ManyToManyField(to='pedidos.itempetit')),
                ('produtos', models.ManyToManyField(to='pedidos.itemproduto')),
                ('sorvetes', models.ManyToManyField(to='pedidos.itemsorvete')),
                ('sucos', models.ManyToManyField(to='pedidos.itemsuco')),
            ],
        ),
        migrations.AddField(
            model_name='acai',
            name='adicionais',
            field=models.ManyToManyField(to='pedidos.adicional'),
        ),
    ]
