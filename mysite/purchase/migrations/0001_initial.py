# Generated by Django 3.0.8 on 2020-07-15 20:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sale', '0001_initial'),
        ('basic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arrive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否有效')),
                ('is_delay', models.BooleanField(default=False, verbose_name='是否延迟')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='到货时间')),
                ('create_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='建立人员')),
            ],
            options={
                'verbose_name': '到货单',
                'verbose_name_plural': '到货单',
                'permissions': (('active_arrive', '可中止到货单'),),
            },
        ),
        migrations.CreateModel(
            name='Procurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_correspond', models.CharField(choices=[('1', '有对应订单'), ('0', '无对应订单')], max_length=1, verbose_name='是否有对应订单')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否有效')),
                ('status', models.CharField(choices=[('N', '尚未到货'), ('A', '全部到货'), ('P', '部分到货'), ('O', '超额到货')], default='N', max_length=1, verbose_name='状态')),
                ('etd', models.DateField(verbose_name='预定到货日期')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='采购时间')),
                ('create_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='建立人员')),
                ('order', models.ForeignKey(blank=True, help_text='仅找尚未出货的订单', limit_choices_to={'is_active': True, 'status': 'N'}, null=True, on_delete=django.db.models.deletion.PROTECT, to='sale.Order', verbose_name='对应订单')),
                ('supplier', models.ForeignKey(limit_choices_to={'status': 'A'}, on_delete=django.db.models.deletion.PROTECT, to='basic.Supplier', verbose_name='供货商')),
            ],
            options={
                'verbose_name': '采购单',
                'verbose_name_plural': '采购单',
                'permissions': (('active_procurement', '可中止采购单'),),
            },
        ),
        migrations.CreateModel(
            name='ProcurementMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.CharField(default='', max_length=2, verbose_name='单身项次')),
                ('quantity', models.PositiveIntegerField(verbose_name='采购数量')),
                ('price', models.DecimalField(decimal_places=4, max_digits=16, verbose_name='未税金额')),
                ('tax', models.DecimalField(decimal_places=4, max_digits=16, verbose_name='税金')),
                ('tax_price', models.DecimalField(decimal_places=4, max_digits=16, verbose_name='含税金额')),
                ('subtotal', models.DecimalField(decimal_places=4, max_digits=16, verbose_name='小计未税金额')),
                ('tax_subtotal', models.DecimalField(decimal_places=4, max_digits=16, verbose_name='小计含税金额')),
                ('tax_pay', models.DecimalField(decimal_places=4, default=0, max_digits=16, verbose_name='已付含税金额')),
                ('description', models.CharField(blank=True, max_length=256, verbose_name='描述')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='basic.Currency', verbose_name='币别')),
                ('material', models.ForeignKey(limit_choices_to={'status': 'A'}, on_delete=django.db.models.deletion.DO_NOTHING, to='basic.Material', verbose_name='原料')),
                ('procurement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purchase.Procurement', verbose_name='采购单单头')),
            ],
            options={
                'verbose_name': '采购单单身',
                'verbose_name_plural': '采购单单身',
            },
        ),
        migrations.CreateModel(
            name='ArriveDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.CharField(default='', max_length=2, verbose_name='单身项次')),
                ('quantity', models.PositiveIntegerField(verbose_name='到货数量')),
                ('description', models.CharField(blank=True, max_length=256, verbose_name='描述')),
                ('arrive', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purchase.Arrive', verbose_name='到货单单头')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basic.Material', verbose_name='到货原料')),
            ],
            options={
                'verbose_name': '到货单单身',
                'verbose_name_plural': '到货单单身',
            },
        ),
        migrations.AddField(
            model_name='arrive',
            name='procurement',
            field=models.ForeignKey(help_text='仅显示"有效"且非"全部到货"的采购单', on_delete=django.db.models.deletion.PROTECT, to='purchase.Procurement', verbose_name='对应采购单'),
        ),
        migrations.AddField(
            model_name='arrive',
            name='supplier',
            field=models.ForeignKey(limit_choices_to={'status': 'A'}, on_delete=django.db.models.deletion.PROTECT, to='basic.Supplier', verbose_name='供货商'),
        ),
    ]