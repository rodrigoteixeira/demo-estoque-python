from app_estoque.visao.APIBasica import APIBasica

def registrar_api(app, endpoint, rep, url):
    visao = APIBasica.as_view(endpoint, repositorio=rep)
    app.add_url_rule(url, defaults={'elem_id': None},
        view_func=visao, methods=['GET'])
    app.add_url_rule(url, view_func=visao, methods=['POST','PUT'])
    app.add_url_rule(url+'/<int:elem_id>', view_func=visao, 
        methods=['GET', 'DELETE'])

def plug_views(app, repProdutos, repOperacoes):
    registrar_api(app, 'produto_api', repProdutos, '/app/produtos')
    registrar_api(app, 'operacao_api', repOperacoes, '/app/operacoes')