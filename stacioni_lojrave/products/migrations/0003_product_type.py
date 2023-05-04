# Generated by Django 4.1.5 on 2023-05-04 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_offer'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('PlayStation', 'PlayStation'), ('Xbox', 'Xbox'), ('PC', 'PC'), ('Accessories', 'Accessories')], default=1, max_length=13),
            preserve_default=False,
        ),
    ]
