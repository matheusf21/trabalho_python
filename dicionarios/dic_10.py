livro = {
    "título": "O Senhor dos Anéis",
    "autor": "J.R.R. Tolkien",
    "ano de publicação": 1954
}

print("Informações do livro:", livro)
livro["ano de publicação"] = int(input("Digite o novo ano de publicação: "))
print("Informações do livro atualizadas:", livro)
