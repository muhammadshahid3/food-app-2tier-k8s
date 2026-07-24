from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Food Name')),
                ('image', models.ImageField(upload_to='foods/', verbose_name='Food Image')),
                ('min_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Minimum Price')),
                ('max_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Maximum Price')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created_at'],
                'verbose_name': 'Food',
                'verbose_name_plural': 'Foods',
            },
        ),
    ]
