import python_jwt as jwt, Crypto.PublicKey.RSA as RSA, datetime





key = RSA.generate(2048)
payload = { 'foo': 'bar', 'wup': 90 };
token = jwt.generate_jwt(payload, key, 'PS256', datetime.timedelta(minutes=5))
header, claims = jwt.verify_jwt(token, key, ['PS256'])
for k in payload: assert claims[k] == payload[k]