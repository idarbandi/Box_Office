# Generated by Django 4.0 on 2022-10-24 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('financial', '0002_alter_payment_invoice_number'),
        ('package', '0002_alter_benefits_package'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveBigIntegerField()),
                ('status', models.SmallIntegerField(choices=[(10, 'Paid'), (-10, 'Not Paid')], default=-10)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now_add=True)),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase', to='package.package')),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='purchase', to='financial.payment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchases', to='auth.user')),
            ],
        ),
    ]