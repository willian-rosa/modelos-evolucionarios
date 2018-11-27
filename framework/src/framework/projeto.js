angular.module('frameworkDifuso').controller('cadastro', function($scope, $routeParams, $location, $window) {
    
    $scope.cadastro = {
        variaveis: [],
        regrasInferencia: []
    };
    
    clearCadastroNovaRegra();
    
    var variavelSelecionada = {};
    
    
    this.$onInit = function () {
        var id = $routeParams.id;

        if(id){
            var projetos = JSON.parse($window.localStorage.getItem('projetos'));

            if (projetos && projetos[id]) {
                var projeto = projetos[id];
                projeto.id = id;
                $scope.cadastro = projeto;
            }else{
                alert('Erro ao selecionar o projeto');
                $location.path('');
                return false;
            }
        }
    };
    
    function clearCadastroNovaRegra(){
        $scope.cadastroNovaRegra = {
            operador: null,
            antecedentes: [{}],
            consequente: null
        };
    }
    
    $scope.clearCadastroNovaRegra = function (){
        clearCadastroNovaRegra();
    };
    
    $scope.cadastroVariavel = function (nomeVariavel, universo){
        
        if(nomeVariavel){
            var variavel = {
                nome: nomeVariavel,
                universo: universo,
                configs: []
            };

            $scope.cadastro.variaveis.push(variavel);
            
        }
        
        $scope._nomeVariavel = '';
        
    };
    
    $scope.setOperador  = function (novaRegra, operador){
        novaRegra.operador = operador;
        novaRegra.antecedentes.push({});
    };
    
    $scope.cadastrarNovaRegra = function (novaRegra){
        $scope.cadastro.regrasInferencia.push(novaRegra);
        clearCadastroNovaRegra();
    };
    
    $scope.selecionaVariavel = function (variavel){
        
        if(variavel){
            variavelSelecionada = variavel;
        }
        
    };
    
    $scope.cadastroConfig = function (){
        
        if($scope.configVariavel.termo){
            variavelSelecionada.configs.push($scope.configVariavel);
        }
        
        $scope.configVariavel = {};
        
        return true;
        
    };
    
    $scope.deleteVariavel = function(item){
        var index = $scope.cadastro.variaveis.indexOf(item);
        if (index > -1) {
          $scope.cadastro.variaveis.splice(index, 1);
        }
    };
    
    
    $scope.concatenartRegras = function(regra){
        var variaveis = $scope.cadastro.variaveis;
        var antecedentes = regra.antecedentes.map(item => variaveis[item.variavel].nome+" é "+variaveis[item.variavel].configs[item.termo].termo);
        
        return antecedentes.join(" "+regra.operador.toUpperCase()+" ");
        
    };
    
    $scope.salvarProjeto = function(projeto){
        
        if (projeto.nome){
            
            var projetos = [];
            
            if ($window.localStorage.getItem('projetos')){
                projetos = JSON.parse($window.localStorage.getItem('projetos'));
            }
            
            if(projeto.id){
                projetos[projeto.id] =projeto;
            }else{
                projetos.push(projeto);
            }
            
            $window.localStorage.setItem('projetos', JSON.stringify(projetos));
            
            $location.path(''); 
        }
        
    };
    
});