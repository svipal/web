# Generated by Django 2.2.20 on 2021-04-22 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0177_profile_poap_owner_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bounty',
            name='web3_type',
            field=models.CharField(choices=[('legacy_gitcoin', 'Legacy Bounty'), ('bounties_network', 'Bounties Network'), ('qr', 'QR Code'), ('web3_modal', 'Web3 Modal'), ('polkadot_ext', 'Polkadot Ext'), ('binance_ext', 'Binance Ext'), ('harmony_ext', 'Harmony Ext'), ('rsk_ext', 'RSK Ext'), ('xinfin_ext', 'Xinfin Ext'), ('algorand_ext', 'Algorand Ext'), ('fiat', 'Fiat'), ('manual', 'Manual')], default='bounties_network', max_length=50),
        ),
        migrations.AlterField(
            model_name='bountyfulfillment',
            name='payout_type',
            field=models.CharField(blank=True, choices=[('bounties_network', 'bounties_network'), ('qr', 'qr'), ('fiat', 'fiat'), ('web3_modal', 'web3_modal'), ('polkadot_ext', 'polkadot_ext'), ('binance_ext', 'binance_ext'), ('harmony_ext', 'harmony_ext'), ('rsk_ext', 'rsk_ext'), ('xinfin_ext', 'xinfin_ext'), ('algorand_ext', 'algorand_ext'), ('manual', 'manual')], help_text='payment type used to make the payment', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='bountyfulfillment',
            name='tenant',
            field=models.CharField(blank=True, choices=[('BTC', 'BTC'), ('ETH', 'ETH'), ('ETC', 'ETC'), ('ZIL', 'ZIL'), ('CELO', 'CELO'), ('PYPL', 'PYPL'), ('POLKADOT', 'POLKADOT'), ('BINANCE', 'BINANCE'), ('HARMONY', 'HARMONY'), ('FILECOIN', 'FILECOIN'), ('RSK', 'RSK'), ('XINFIN', 'XINFIN'), ('ALGORAND', 'ALGORAND'), ('OTHERS', 'OTHERS')], help_text='specific tenant type under the payout_type', max_length=10, null=True),
        ),
    ]