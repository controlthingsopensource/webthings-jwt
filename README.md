# JWT-based authorization for Mozilla's WebThings Gateway
## Prerequisites
* Apache2 web server
* mod_authnz_jwt (https://github.com/AnthonyDeroche/mod_authnz_jwt)
* mod_proxy (sudo a2enmod proxy sudo a2dismod proxy_http)
* systemctl restart apache2

## Create an authorization service (optional)
You can create an authorization serivce and issue JWT tokens yourself in order to test your setup. For this you will need
* PyWJT (pip install pyjwt[crypto])
* Openssl

Generate the private and public keys used for signting and verifying the JWT token. Note that the private key must be kept secret
* openssl genrsa -out privkey.pem 2048
* openssl rsa -in privkey.pem -pubout -out pubkey.pem

Place privkey.pem in the jwt folder, make the appropriate modifications to the JWT creation script, and run it:
* cd jwt
* python3 JWT_create.py

The script outputs a token that can be used for accessing the GW. 

## Setup
* add webthings-gw.conf in /etc/apache2/sites-available
* add a link to webthings-gw.conf in /etc/apach2/sites-enabled (sudo ln -s ../sites-available/webthings-gw.conf .)