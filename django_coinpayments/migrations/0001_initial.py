# Generated by Django 2.0.4 on 2018-04-06 14:04

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoinPaymentsTransaction',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.CharField(editable=False, max_length=100, primary_key=True, serialize=False, verbose_name='id')),
                ('address', models.CharField(max_length=150, verbose_name='Address')),
                ('amount', models.DecimalField(decimal_places=18, max_digits=100, verbose_name='Amount')),
                ('confirms_needed', models.PositiveSmallIntegerField(verbose_name='Confirms needed')),
                ('qrcode_url', models.URLField(verbose_name='QR Code Url')),
                ('status_url', models.URLField(verbose_name='Status Url')),
                ('timeout', models.DateTimeField(verbose_name='Valid until')),
            ],
            options={
                'verbose_name': 'CoinPayments Transaction',
                'verbose_name_plural': 'CoinPayments Transactions',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('currency_original', models.CharField(choices=[('BCH', 'Bitcoin Cash'), ('BLK', 'BlackCoin'), ('BTC', 'Bitcoin'), ('DASH', 'Dash'), ('DCR', 'Decred'), ('DGB', 'DigiByte'), ('DOGE', 'Dogecoin'), ('ETC', 'Ether Classic'), ('ETH', 'Ether'), ('EXP', 'Expanse'), ('GAME', 'GameCredits'), ('LSK', 'LISK'), ('LTC', 'Litecoin'), ('MAID', 'MaidSafeCoin'), ('NAV', 'NAV Coin'), ('NEO', 'NEO'), ('POT', 'PotCoin'), ('SBD', 'Steem Dollars'), ('STEEM', 'STEEM'), ('STRAT', 'Stratis'), ('VTC', 'Vertcoin'), ('XEM', 'NEM'), ('XMR', 'Monero'), ('XRP', 'Ripple'), ('XVG', 'VERGE')], max_length=8, verbose_name='Original currency')),
                ('currency_paid', models.CharField(choices=[('BCH', 'Bitcoin Cash'), ('BLK', 'BlackCoin'), ('BTC', 'Bitcoin'), ('DASH', 'Dash'), ('DCR', 'Decred'), ('DGB', 'DigiByte'), ('DOGE', 'Dogecoin'), ('ETC', 'Ether Classic'), ('ETH', 'Ether'), ('EXP', 'Expanse'), ('GAME', 'GameCredits'), ('LSK', 'LISK'), ('LTC', 'Litecoin'), ('MAID', 'MaidSafeCoin'), ('NAV', 'NAV Coin'), ('NEO', 'NEO'), ('POT', 'PotCoin'), ('SBD', 'Steem Dollars'), ('STEEM', 'STEEM'), ('STRAT', 'Stratis'), ('VTC', 'Vertcoin'), ('XEM', 'NEM'), ('XMR', 'Monero'), ('XRP', 'Ripple'), ('XVG', 'VERGE')], max_length=8, verbose_name='Payment currency')),
                ('amount', models.DecimalField(decimal_places=18, max_digits=100, verbose_name='Amount')),
                ('amount_paid', models.DecimalField(decimal_places=18, max_digits=100, verbose_name='Amount paid')),
                ('status', models.CharField(choices=[('PRPE', 'Provider-related payment pending'), ('PEND', 'Pending'), ('CNCL', 'Cancelled'), ('TOUT', 'Timed out'), ('PAID', 'Paid')], max_length=4)),
                ('provider_tx', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='django_coinpayments.CoinPaymentsTransaction', verbose_name='Payment transaction')),
            ],
            options={
                'verbose_name': 'Payment',
                'verbose_name_plural': 'Payments',
            },
        ),
    ]
