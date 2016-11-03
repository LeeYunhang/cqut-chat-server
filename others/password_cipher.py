from Crypto.Hash import MD5

def encrypt_password(password):
    password = password = '#@$^%%&@#' + password + '!@#$%^&*(%#'
    m = MD5.new()
    m.update(bytes(source=password, encoding='utf8'))

    password = m.hexdigest()
    m = MD5.new()
    m.update(bytes(source=password, encoding='utf8'))

    return m.hexdigest()