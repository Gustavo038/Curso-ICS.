def usuarioesenha(usuario_e_senha):
    usuario = "letra"
    senha = usuario_e_senha[-1]

    if usuario in senha:
        return "usuario"
    
    else:
        return "Acesso concedido"
    
while True:

    usuario_nome = input("Digite seu usuario e senha")
    res = usuarioesenha(usuario_nome)
    print(res)