
dicionario_categorias = {
    'frutas': ['melancia', 'kiwi', 'ameixa', 'pitaia', 'morango'],
    'vegetais': ['tomate', 'repolho', 'alface', 'cenoura', 'couver'],
    'bebidas': ['água', 'refrigerante', 'cerveja', 'cachaça']
}


for categoria, itens in dicionario_categorias.items():
    print(f"{categoria.capitalize()}:")
    for item in itens:
        print(" - {item}")
    print()