# Esercizio sugli indirizzi Bitcoin
#
# Scrivere un programma in Python per generare un indirizzo
# Bitcoin valido. Per verificare che l'indirizzo generato sia valido
# è possibile utilizzare il servizio https://thomas.vanhoutte.be/tools/validate-bitcoin-address.php
#
# Per generare un indirizzo Bitcoin è possibile leggere il seguente post:
# https://medium.com/coinmonks/bitcoin-address-generation-on-python-e267df5ff3a3 
#
# Laboratorio di Tecnologie Blockchain - Docente: Enrico Zimuel
# ITS ICT Piemonte (https://www.its-ictpiemonte.it/)

import binascii
from hashlib import sha256, new
import base58 as base58
import ecdsa

# Genero la chiave privata
ecdsaPrivateKey = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)

# Estraggo la chiave pubblica
ecdsaPublicKey = '04' + ecdsaPrivateKey.get_verifying_key()\
                                       .to_string()\
                                       .hex()

hash256FromECDSAPublicKey = sha256(binascii.unhexlify(ecdsaPublicKey)).hexdigest()

ridemd160FromHash256 = new('ripemd160', binascii.unhexlify(hash256FromECDSAPublicKey))

prependNetworkByte = '00' + ridemd160FromHash256.hexdigest()

# Calcolo il checksum con SHA256(SHA256(prependNetworkByte))
hash = prependNetworkByte
for x in range(1, 3):
    hash = sha256(binascii.unhexlify(hash)).hexdigest()
# Prelevo gli ultimi otto caratteri
cheksum = hash[:8]

appendChecksum = prependNetworkByte + cheksum

bitcoinAddress = base58.b58encode(binascii.unhexlify(appendChecksum))

print("Indirizzo Bitcoin: ", bitcoinAddress.decode('utf8'))