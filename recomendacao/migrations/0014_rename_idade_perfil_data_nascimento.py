# Generated by Django 5.1.5 on 2025-01-20 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recomendacao', '0013_alter_perfil_usuario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perfil',
            old_name='idade',
            new_name='data_nascimento',
        ),
    ]
