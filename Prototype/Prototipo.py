import copy
import os
class LivroPrototype:
    def clone(self):
        raise NotImplementedError

class Livro(LivroPrototype):
    def __init__(self, titulo, autor, edicao, paginas):
        self.titulo = titulo
        self.autor = autor
        self.edicao = edicao
        self.paginas = paginas
        
    def __str__(self):
        return f"Título: '{self.titulo}' | Autor: {self.autor} | Edição: {self.edicao} | Páginas: {self.paginas}"
        
    def clone(self):
        """
        Cria uma cópia profunda (deep copy) do objeto Livro.
        """
        print(f"Clonando o livro '{self.titulo}'...")
        return copy.deepcopy(self)
    
if __name__ == "__main__":
    livro_modelo = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", "Primeira Edição", 1216)
    print("--- Livro Protótipo Criado ---")
    print(livro_modelo)
    print("-" * 40)

    livro_copia_1 = livro_modelo.clone()
    livro_copia_1.titulo = "O Senhor dos Anéis (Edição de Bolso)"
    livro_copia_1.edicao = "Edição de Bolso (2010)"
    livro_copia_1.paginas = 1500

    livro_copia_2 = livro_modelo.clone()
    livro_copia_2.titulo = "O Senhor dos Anéis (Edição de Colecionador)"
    livro_copia_2.edicao = "Edição de Colecionador"
    
    print("\n--- Catálogo de Livros Criado a partir do Protótipo ---")
    print(f"Livro Original: \n{livro_modelo}")
    print("-" * 20)
    print(f"Cópia 1 (Edição de Bolso): \n{livro_copia_1}")
    print("-" * 20)
    print(f"Cópia 2 (Edição de Colecionador): \n{livro_copia_2}")
    print("-" * 40)
    
    print("\n--- Verificação ---")
    print(f"O livro original é o mesmo objeto que a cópia 1? {livro_modelo is livro_copia_1}")
    print(f"A cópia 1 é o mesmo objeto que a cópia 2? {livro_copia_1 is livro_copia_2}")