(function(){
     angular.module('meuEstoque', [])
        .controller('ProdutoController', ProdutoController);
    
    function ProdutoController($http, $log){
        var self = this;
        self.produtos = [];
        self.produtoCorrente = null;
        
        
        function buscarProdutos(){
            $http.get('/app/produtos').then(function(request){
                $log.debug('$http.get("/app/produtos")', request);
                self.produtos = request.data.produtos;
            });
        }
        
        self.novo = function(){
            self.produtoCorrente = { id:'' };
        }
        
        self.salvar = function(){
            
            $http.post('/app/produtos', self.produtoCorrente).then(function(resquest){
                self.produtoCorrente = null;
                buscarProdutos();
            });
            
        }
        
        self.editar = function(item){
            self.produtoCorrente = angular.copy(item);
        }
        
        self.cancelar = function(){
            self.produtoCorrente = null;
        }
        
        
        
        buscarProdutos();
    }
}());