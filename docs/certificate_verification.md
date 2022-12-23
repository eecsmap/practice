Assume we have certificate_1.pem signed by issuer with its private key issuer_private_key.pem

When certificate_1.pem was created, pieces of information are filled into the request as the certificate to be signed.

### Then the issuer:
1. verify the information in the request
2. generate a hash of the tbsCertificate
3. encrypt the using issuer's private key as the signature
4. this signature is embedded into the signed certificate_1.pem

## So the verification simply goes in following steps:
1. compute the hash of the tbsCertificate as hash_calculated
2. pull the signature from the certificate
   1. `openssl x509 -in certificate.pem -noout -text`
   2. convert signature from 'FE:ED:..:10' to 0xfeed...10 as integer S
3. pull the public key from the issuer's private key
   1. `openssl rsa -in issuer_private_key.pem -pubout -out issuer_public_key.pem`
   2. get the modulus and exponent(usually 65537) from the pubkey.
      1. `openssl rsa -in issuer_public_key.pem -pubin -noout -text`
      2. convert the modulus into integer M in the form of 0xffff...ff
4. decrypt the signature using the issuer's public key as hash_expected
   1. get the last 40/64 characters from `pow(S, 65537, M)` according to your hash algorithms.
5. compare hash_calculated with hash_expected

