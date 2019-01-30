

"""
def process( n):
    u = []
    t = 0
    _n = list(n.encode())
    while 1:
        if not(t < len(_n)):
            break
        i = _n[t]
        if t % 3 == 1:
            r = i
            i = 57 if r == 65 else (70 if r == 48 else r - 1)
        u.append(i)
        t += 1
    return bytes(u).decode('gbk')
"""

import rsa

# 生成测试密匙
(pubkey, privkey) = rsa.newkeys(1024)

e = hex(pubkey.e).replace('0x', '')
e =  '00000' + e
e = e[-6:]
n = hex(pubkey.n).replace('0x', '')


d = hex(privkey.d).replace('0x', '')
p = hex(privkey.p).replace('0x', '')
q = hex(privkey.q).replace('0x', '')
print('pubkey')
print(e)
print(n)

print('privkey')
print(d)
print(p)
print(q)

# ------ 以下密匙预生成  -------
# 公钥(预生成)
e = '010001'
e = int(e, 16)
n = '85ec922f28cc33e35b78461cb69aac204d576f14b41f6431f0503f4c0e1d617166ceb475b4124b46d72006cc1955a422492572282aaa6b7b6c20f039a1c834bcc75e1212688eb35d6e990d9b8ebe720eed724870cfcd8498f7983cac696a9132d06a908eee010ebd26ad1aab2bedea4af77eb2905a251f078c59fa958205f491'
n = int(n, 16)

# js代码（公钥加密）
"""
e = '010001'
n = '85ec922f28cc33e35b78461cb69aac204d576f14b41f6431f0503f4c0e1d617166ceb475b4124b46d72006cc1955a422492572282aaa6b7b6c20f039a1c834bcc75e1212688eb35d6e990d9b8ebe720eed724870cfcd8498f7983cac696a9132d06a908eee010ebd26ad1aab2bedea4af77eb2905a251f078c59fa958205f491'

setMaxDigits(129)
p = new RSAKeyPair(e, '', n)
console.log(encryptedString(p, '789789'))
"""

# 私钥(预生成)
d = int('3812c5625982a6771b655075d53f0db2b8af53232807bcbbec12ad6dfabaf281b8b9f37514e05404652e53aa41314a77d0888d33a42996b7269ee3f5e13d47c157261d28f475d837390cee8682587dc2841eacea4391575c882dd955febf41222bde7e2a9b47f236bb50c174260084267f7ea13cbc1ebe8ea7365f947ab57d01', 16)
p = int('dc4450d031ba6de145adc6f63d05649bcf48f2390483525341e082580a9d7260e0fd6cd490793ede238040623749dcb914ffc42d33c2e48cb47bc884434fcc528e1ce6d5', 16)
q = int('9ba670af47a15289f6ff468fe25ab9b9fc6d6de5dfe56e28ad6587c4f9eda499b712f7449146e91d28cc9e10983f747eabd2e28dae32de4cdba2accd', 16)


pub_key = rsa.PublicKey(e=e, n=n)
priv_key = rsa.PrivateKey(e=e,n=n, d=d, p=p, q=q)

m = rsa.encrypt('789789'.encode(),pub_key)

print(m.hex())

# 解密(上面js使用公匙加密后的密文)
# 如果解密失败，一般可能是 RSAKeyPair 内把公匙，2次加解密了
m = '0dba37b7302faf0d9c156eef247b7cab853aed75e10ed41f85cd49313e372f73aff6baf30df4c06763ec5acfbd6fa335e4267070eb04120414acf4c954d7312bec444745f7f7b8f888a3e1018813cbcf4deb299bfea9bfff8c48e166b45600283aedf53ea068fff31d76b70a297767621cb08e3be4c19d9016f621c700bc1ae2'
mm = rsa.decrypt(bytes.fromhex(m), priv_key)
print(mm)