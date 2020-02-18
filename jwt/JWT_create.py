import io
import jwt

# JWT claims
# Modify the aud clain to much the DNS name of your gateway, or remove it
payload = {
    'aud': 'webthings.controlthings.gr'
}

# Read the generated private key
with open('privkey.pem', mode='rb') as file: 
    private_key = file.read()

#J WT generation
token = jwt.encode(payload, private_key, algorithm='RS256')
print(token)