# JWT-based authorization for Mozilla's WebThings Gateway
**Disclaimer**
The code included in this repository is for demonstation purposed only. Further steps have to be made in order to make it secure.

The following README assumes a Mozilla's WebThings Gateway running at port 8080

## Prerequisites
* Apache2 web server at the same maching as Mozilla's WebThings Gateway
* mod_authnz_jwt (see the following sections)
* mod_proxy (sudo a2enmod proxy sudo a2dismod proxy_http)
* mod_headers (sudo a2enmod headers)

After installing all modules do not forget to restart apache by invoking `systemctl restart apache2`

### Installing mod_authnz_jwt
mod_auth_jwt can be retreived by https://github.com/AnthonyDeroche/mod_authnz_jwt However, with this code requires JWT to include some mandatory claims (see issue https://github.com/AnthonyDeroche/mod_authnz_jwt/issues/39) If you do not want to use these claims you can alternatively install mod_auth_jwt from https://github.com/controlthingsopensource/mod_authnz_jwt 

**The JWT generation script provided in this repository does not use these claims**

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

Alternatively you can use the JWT below which can be verfied using the public key included in the file `apache\pubkey.pem`

## Setup
* Login to your webthings gateway, navigate to "menu, Settings, Developer" and select "Create local authorization". Select "Allow for all things" or choose a more fine-grained policy. Then press allow and copy the generated JSON web token in the appropriate location of webthings-gw.conf (replace `JWTToken` at line 2 with your token)
* Replace example.controlthings.gr with your server name in webthings-gw.conf
* add webthings-gw.conf in /etc/apache2/sites-available
* add a link to webthings-gw.conf in /etc/apach2/sites-enabled (sudo ln -s ../sites-available/webthings-gw.conf .) 

## Using
Execure the following command by replacing `token` with the token generated in the previous step. If you have used the example public key provided in this repository then you can use the following token
> eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJ3ZWJ0aGluZ3MuY29udHJvbHRoaW5ncy5nciJ9.RW74j7Fs473wvvQ5cl-3ggjWrhoXXpfhH5hOomEUDvSQaWBGEcnbaUX8JfLeKnEOfot3NOYrikVyHP7OVKBa1obp5tcVT5Kw7ntbSM1It0H1HhMp4aqWAMTyZI-Unz3qZus2gkQqpobB2q1Ib7AzjnMO1gc4rKtWyMKArotN14XZ0UyczyGS0S4nUU9U1ZV9cFknANzINaMHc-KnprZQDZovb0OnLK6zezhHevk3McGXLWOEoIXGIavGBTMBf2LHyrqzvsRWhplZJ2-_rCDQuvu70HdghqU1ai5C3G5BrdpIAiaYWS4Q8orMbkk4sWkBv8gezxfFbt3631VSESfbYQ

* curl -H "Authorization: Bearer token" -H "Accept: application/json" http://example.controlthings.gr/things



