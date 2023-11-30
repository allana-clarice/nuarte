# Generated by Django 4.2.7 on 2023-11-24 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("nuarte", "0006_instrumento_imagem"),
    ]

    operations = [
        migrations.AddField(
            model_name="historico",
            name="devolucao",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="historico",
            name="instrumento",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="nuarte.instrumento"
            ),
        ),
    ]