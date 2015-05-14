class ProdutoNaoEncontrado(Exception):
    pass 

class ProdutoInvalido(Exception):
    pass 

class RepositorioProdutos:
    produtos = []
    def __init__ (self, produtos):
        self.produtos = produtos

    def listar(self):
        return self.produtos

    def buscarPorId(self, prodid):
        resultado = [produto for produto in self.produtos if produto['id'] == prodid]
        if len(resultado) == 0:        
            raise ProdutoNaoEncontrado
        return self.produtos        
    
    def remover(self, prodid):
        produto = self.buscarPorId(prodid);
        self.produtos.remove(produto[0])
        
    def adicionar(self, prod):
        if not (prod and all (k in prod for k in ('nome', 'preco', 'categoria'))):        
            raise ProdutoInvalido
        else:
            produto = {
                'id': self.produtos[-1]['id'] + 1,
                'nome': prod['nome'],
                'descricao': prod.get('descricao', ""),
                'preco': prod['preco'],
                'quantidade': prod.get('quantidade', 0),
                'categoria': prod['categoria']
            }
            self.produtos.append(produto)
            return produto;
            
    def atualizar(self, novoprod):
        if novoprod :        
            produto = self.buscarPorId(novoprod['id'])
            produto['nome'] = novoprod.get('nome', produto['nome'])
            produto['descricao'] = novoprod.get('descricao', produto['descricao'])
            produto['preco'] = novoprod.get('preco', produto['preco'])
            produto['quantidade'] = novoprod.get('quantidade', produto['quantidade'])
            produto['categoria'] = novoprod.get('categoria', produto['categoria'])   
            return produto;
        else:
            raise ProdutoNaoEncontrado