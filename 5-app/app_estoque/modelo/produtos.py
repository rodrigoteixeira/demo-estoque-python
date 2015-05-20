from app_estoque.modelo.excecoes import ElementoInexistente, ElementoInvalido

class RepositorioProdutos:
    produtos = []
    def __init__ (self):
        self.produtos = [
            {
                'id': 1,
                'nome':  u"Blu-ray - O exterminador do Futuro",
                'descricao': u"Androide vem do futuro com o objetivo de matar a mae de um futuro lider guerrilhero humano.",
                'preco': 22.41,
        		'quantidade': 10,
        		'categoria' : "DVD"
            },
            {
                'id': 3,
                'nome': u"Exterminador de cupins 400ml",
                'descricao': u"O exterminador de cupins", 
                'preco': 19.33,
        		'quantidade': 30,
        		'categoria' :  "limpeza"
            },	
        	{
                'id': 4,
                'nome': u"Fantasia Adulto Exterminador John Connor",
                'descricao': u"Transforme-se em seu heroi", 
                'preco': 300.85,
        		'quantidade': 3,
        		'categoria' :  "fantasia"
            }	
        ]

    def listar(self):
        return self.produtos

    def buscarPorId(self, prodid):
        resultado = [produto for produto in self.produtos if produto['id'] == prodid]
        if len(resultado) == 0:        
            raise ElementoInexistente
        return resultado[0]        
    
    def remover(self, prodid):
        produto = self.buscarPorId(prodid);
        self.produtos.remove(produto[0])
        
    def adicionar(self, prod):
        if not (prod and all (k in prod for k in ('nome', 'preco', 'categoria'))):        
            raise ElementoInvalido
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
            raise ElementoInexistente