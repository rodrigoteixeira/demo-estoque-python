from excecoes import ElementoInexistente, ElementoInvalido


class RepositorioOperacoes:

    def __init__ (self, repositorioProdutos):
        self.repositorioProdutos = repositorioProdutos
        self.operacoes = [
            {
                'id': 1,
                'produto' : 1,
        		'data' : "01/05/2015",
        		'tipo' : 'COMPRA',
        		'quantidade' : 3
            },
            {
                'id': 2,
                'produto' : 1,
        		'data' : "01/05/2015",
        		'tipo' : 'VENDA',
        		'quantidade' : 5		
            },
        	{
                'id': 3,
                'produto' : 4,
        		'data' : "01/05/2015",
        		'tipo' : 'VENDA',
        		'quantidade' : 2				
            },
        	{
                'id': 4,
                'produto' : 3,
        		'data' : "02/05/2015",
        		'quantidade' : 20,			
        		'tipo' : 'COMPRA'
            }            
        ]

    def listar(self):
        return self.operacoes

    def buscarPorId(self, opid):
        resultado = [operacao for operacao in self.operacoes if operacao['id'] == opid]
        if len(resultado) == 0:        
            raise ElementoInexistente
        return resultado        
    
    def remover(self, opid):
        operacao = self.buscarPorId(opid);
        self.operacoes.remove(operacao)
        
    def ehvalido(self, operacao):
        return (not operacao.quantidade or operacao.quantidade >= 0) and \
               (not operacao.preco or operacao.tipo == "COMPRA"  or operacao.tipo == "VENDA") and \
               (not operacao.produto or self.repositorioProdutos.contemProduto(operacao.produto));
               
    def adicionar(self, novaoperacao):
        if not (novaoperacao and all (k in novaoperacao for k in ('tipo', 'quantidade', 'data', 'produto'))) and self.ehvalido(novaoperacao):        
            raise ElementoInvalido
        else:
            operacao = {
                'id': self.operacoes[-1]['id'] + 1,
                'tipo': novaoperacao['tipo'],
                'data': novaoperacao.get('data'),
                'quantidade': novaoperacao.get('quantidade'),
                'produto': novaoperacao['produto']
            }
            self.operacoes.append(operacao)
            return operacao;
            
    def atualizar(self, novaoperacao):
        if novaoperacao and self.ehvalido(novaoperacao):        
            operacao = self.buscarPorId(novaoperacao['id'])
            operacao['tipo'] = novaoperacao.get('tipo', operacao['tipo'])
            operacao['data'] = novaoperacao.get('data', operacao['data'])
            operacao['quantidade'] = novaoperacao.get('quantidade', operacao['quantidade'])
            operacao['produto'] = novaoperacao.get('produto', operacao['produto'])   
            return operacao;
        else:
            raise ElementoInvalido
            
