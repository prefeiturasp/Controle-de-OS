# Generated by Django 2.1.1 on 2018-10-01 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cadastro', '0001_initial'),
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movimentacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movimentacao', models.CharField(max_length=100)),
                ('dt_movimentacao', models.DateField()),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.Usuario')),
                ('n_os', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.Cadastro')),
            ],
        ),
    ]
