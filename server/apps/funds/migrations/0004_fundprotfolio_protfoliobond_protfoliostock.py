# Generated by Django 3.0.7 on 2020-12-29 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funds', '0003_usersnews'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProtfolioStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period_start', models.DateTimeField(help_text='开始日期', verbose_name='开始日期')),
                ('period_end', models.DateTimeField(help_text='报告期', verbose_name='报告期')),
                ('pub_date', models.DateTimeField(help_text='公告日期', verbose_name='公告日期')),
                ('rank', models.IntegerField(help_text='报告类持仓排名', verbose_name='持仓排名')),
                ('symbol', models.CharField(default='', help_text='股票代码', max_length=32, verbose_name='股票代码')),
                ('name', models.CharField(default='', help_text='股票名称', max_length=100, verbose_name='股票名称')),
                ('shares', models.DecimalField(decimal_places=4, default=0.0, max_digits=20, verbose_name='持有股票数量')),
                ('market_cap', models.DecimalField(decimal_places=4, default=0.0, max_digits=20, verbose_name='持有股票的市值')),
                ('proportion', models.DecimalField(decimal_places=4, default=0.0, max_digits=10, verbose_name='占净值比例')),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='funds.FundMain', verbose_name='基金代码')),
            ],
            options={
                'verbose_name': '基金持股信息',
                'verbose_name_plural': '基金持股信息',
            },
        ),
        migrations.CreateModel(
            name='ProtfolioBond',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period_start', models.DateTimeField(help_text='开始日期', verbose_name='开始日期')),
                ('period_end', models.DateTimeField(help_text='报告期', verbose_name='报告期')),
                ('pub_date', models.DateTimeField(help_text='公告日期', verbose_name='公告日期')),
                ('rank', models.IntegerField(help_text='报告类持仓排名', verbose_name='持仓排名')),
                ('symbol', models.CharField(default='', help_text='债券代码', max_length=32, verbose_name='债券代码')),
                ('name', models.CharField(default='', help_text='债券名称', max_length=100, verbose_name='债券名称')),
                ('shares', models.DecimalField(decimal_places=4, default=0.0, max_digits=20, verbose_name='持有债券数量')),
                ('market_cap', models.DecimalField(decimal_places=4, default=0.0, max_digits=20, verbose_name='持有债券的市值')),
                ('proportion', models.DecimalField(decimal_places=4, default=0.0, max_digits=10, verbose_name='占净值比例')),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='funds.FundMain', verbose_name='基金代码')),
            ],
            options={
                'verbose_name': '基金持股信息',
                'verbose_name_plural': '基金持股信息',
            },
        ),
        migrations.CreateModel(
            name='FundProtfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='基金名称', max_length=80, verbose_name='基金名称')),
                ('period_start', models.DateTimeField(help_text='开始日期', verbose_name='开始日期')),
                ('period_end', models.DateTimeField(help_text='报告期', verbose_name='报告期')),
                ('pub_date', models.DateTimeField(help_text='公告日期', verbose_name='公告日期')),
                ('equity_value', models.DecimalField(decimal_places=4, default=0.0, max_digits=20, verbose_name='权益类投资金额')),
                ('equity_rate', models.DecimalField(decimal_places=4, default=0.0, max_digits=10, verbose_name='权益类投资占比')),
                ('stock_value', models.DecimalField(decimal_places=4, default=0.0, max_digits=20, verbose_name='股票投资金额')),
                ('stock_rate', models.DecimalField(decimal_places=4, default=0.0, max_digits=10, verbose_name='股票投资占比')),
                ('fixed_income_value', models.DecimalField(decimal_places=4, default=0.0, max_digits=20, verbose_name='固定收益投资金额')),
                ('fixed_income_rate', models.DecimalField(decimal_places=4, default=0.0, max_digits=10, verbose_name='固定收益投资占比')),
                ('precious_metal_value', models.DecimalField(decimal_places=4, default=0.0, max_digits=20, verbose_name='贵金属投资金额')),
                ('precious_metal_rate', models.DecimalField(decimal_places=4, default=0.0, max_digits=10, verbose_name='贵金属投资占比')),
                ('derivative_value', models.DecimalField(decimal_places=4, default=0.0, max_digits=20, verbose_name='金融衍生品投资金额')),
                ('derivative_rate', models.DecimalField(decimal_places=4, default=0.0, max_digits=10, verbose_name='金融衍生品投资占比')),
                ('buying_back_value', models.DecimalField(decimal_places=4, default=0.0, max_digits=20, verbose_name='买入返售金融资产金额')),
                ('buying_back_rate', models.DecimalField(decimal_places=4, default=0.0, max_digits=10, verbose_name='买入返售金融资产占比')),
                ('deposit_value', models.DecimalField(decimal_places=4, default=0.0, max_digits=20, verbose_name='银行存款和结算备付金合计')),
                ('deposit_rate', models.DecimalField(decimal_places=4, default=0.0, max_digits=10, verbose_name='银行存款和结算备付金合计占比')),
                ('others_value', models.DecimalField(decimal_places=4, default=0.0, max_digits=20, verbose_name='其他资产')),
                ('others_rate', models.DecimalField(decimal_places=4, default=0.0, max_digits=10, verbose_name='其他资产占比')),
                ('total_asset', models.DecimalField(decimal_places=4, default=0.0, max_digits=20, verbose_name='总资产合计')),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='funds.FundMain', verbose_name='基金代码')),
            ],
            options={
                'verbose_name': '基金资产组合信息',
                'verbose_name_plural': '基金资产组合信息',
            },
        ),
    ]
