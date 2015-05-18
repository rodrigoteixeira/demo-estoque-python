(function(){
    var PRODUTOS = [
    {
        "id": 1,
        "nome":  "Blu-ray - O exterminador do Futuro",
        "descricao": "Andróide (Arnold Schwarzenegger) vem do futuro com o objetivo de matar a mãe (Linda Hamilton) de um futuro líder guerrilherio humano.",
        "preco": 22.41,
		"quantidade": 10,
		"categoria" : 'DVD'
    },
    {
        "id": 2,
        "nome": "Arrow - A Segunda Temporada Completa (5 Discos)",
        "descricao": "Depois de se retirar para a ilha onde ficou preso uma vez, Oliver Queen retorna para a proteção de sua mãe, irmã e de sua corporação sitiada", 
        "preco": 84.92,
		"quantidade": 8,
		"categoria" : 'DVD'
    },
    {
        "id": 3,
        "nome": "Exterminador de cupins 400ml",
        "descricao": "O exterminador de cupins", 
        "preco": 19.33,
		"quantidade": 30,
		"categoria" :  'limpeza'
    },	
	{
        "id": 4,
        "nome": "Fantasia Adulto Exterminador John Connor",
        "descricao": "Transforme-se em seu heroi", 
        "preco": 300.85,
		"quantidade": 3,
		"categoria" :  'fantasia'
    }	
];


    angular.module('meuEstoque', [])
        .controller('MainController', MainController)
        .controller('ProdutoController', ProdutoController);
    
    
    
    
    function MainController(){
        
    }
    
    function ProdutoController(){
        var self = this;
        self.produtos = PRODUTOS;
        self.produtoCorrente = null;
        
        self.novo = function(){
            self.produtoCorrente = { id:'' };
        }
        
        self.salvar = function(){
            if(self.produtoCorrente.id){
                var index = -1;
                self.produtos.forEach(function(item, i){
                    if(item.id == self.produtoCorrente.id){
                        index = i;      
                    }
                });
                if(index >= 0 ){
                    self.produtos[index] = self.produtoCorrente;
                }
            }else{
                self.produtoCorrente.id = self.produtos.length;
                self.produtos.push(self.produtoCorrente);
            }
            self.produtoCorrente = null;
        }
        
        self.editar = function(item){
            self.produtoCorrente = angular.copy(item);
        }
        
        self.cancelar = function(){
            self.produtoCorrente = null;
        }
    }
}());