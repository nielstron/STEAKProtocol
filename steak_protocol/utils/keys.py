from pathlib import Path

from pycardano import PaymentVerificationKey, PaymentSigningKey, Address, Network

from .network import network

keys_dir = Path(__file__).parent.parent.parent.joinpath("keys")


def get_address(name, network=network) -> Address:
    with open(
        keys_dir.joinpath(
            f"{name}.{'addr' if network == Network.MAINNET else 'test_addr'}"
        )
    ) as f:
        address = Address.from_primitive(f.read())
    return address


def get_signing_info(name, network=network):
    skey_path = str(keys_dir.joinpath(f"{name}.skey"))
    payment_skey = PaymentSigningKey.load(skey_path)
    payment_vkey = PaymentVerificationKey.from_signing_key(payment_skey)
    payment_address = Address(payment_vkey.hash(), network=network)
    return payment_vkey, payment_skey, payment_address
