email_tmpl = """
    Olá, %(nome)s!

    Tem interesse em comprar %(produto)s?

    Este produto é ótimo para %(texto)s

    Clique agora em %(link)s

    Apenas %(quantidade)d disponível!

    Preço promocional R$%(preco).2f
"""

clientes = ["Wallace", "Natalia", "Jaci"]

for cliente in clientes:
    print(
        email_tmpl 
        % {
            "nome": cliente, 
            "produto": "caneta", 
            "texto": "Escrever muito bem",
            "link": "https://google.com",
            "quantidade": 1,
            "preco": 5.9
        }
    )