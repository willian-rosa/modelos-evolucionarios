angular.module('frameworkDifuso').controller('simular', function($scope, $routeParams, $window, $location) {
    
    $scope.resultadoSimulador = null;
    $scope.inferencia = [];
    $scope.projeto = null;
    var projeto = null;
    
    var id = $routeParams.id;

    var projetos = JSON.parse($window.localStorage.getItem('projetos'));

    if (projetos && projetos[id]) {
        projeto = projetos[id];
    }else{
        alert('Erro ao selecionar o projeto');
        $location.path('');
        return false;
    }
    
    
    if (projeto) {
        for (var kval in projeto.variaveis) {
            var variavel = projeto.variaveis[kval];
            
            projeto.variaveis[kval]._universo = variavel.universo.split(',');
            
            for (var kconfig in variavel.configs) {
                var config = variavel.configs[kconfig];
                
                var suporte = config.suporte.split(',');
                var nucleo = config.nucleo.split(',');
                
                projeto.variaveis[kval].configs[kconfig]._suporte = suporte;
                projeto.variaveis[kval].configs[kconfig]._nucleo = nucleo;
                
                var tipo;
                
                if (suporte[0] === nucleo[0]){
                    tipo = 'esquerdo';
                }else if (suporte[1] === nucleo[1] || (nucleo.length === 1 && suporte[1] === nucleo[0])) {
                    tipo = 'direito';
                }else{
                    tipo = 'meio';
                }
                
                
                projeto.variaveis[kval].configs[kconfig]._tipo = tipo;

                
                
            }
            
        }
                
        $scope.projeto = projeto;
        
    }
    
    $scope.concatenartRegras = function(regra){
        var variaveis = $scope.projeto.variaveis;
        var antecedentes = regra.antecedentes.map(item => variaveis[item.variavel].nome+" é "+variaveis[item.variavel].configs[item.termo].termo);
        
        return antecedentes.join(" "+regra.operador.toUpperCase()+" ");
        
    };
    
    
    
    
    
    $scope.simular = function(simulacao){
        
        var variaveis = $scope.projeto.variaveis;
        var variaveisAlvo = $scope.projeto.variaveis[$scope.projeto.variavelAlvo];
        var regrasInferencia = $scope.projeto.regrasInferencia;
        
        //preparando array de resultado
        var resultadoRegrasInferencia = [];
        
        regrasInferencia.forEach(function (regra, indexRegra){
            
            var saidasAntecedentes = regra.antecedentes.map(function (antecedente, antecedenteRegra){
                var termo = variaveis[antecedente.variavel].configs[antecedente.termo];
                
                var resultado = funcaoPertinencia(termo, simulacao[antecedente.variavel]);
                
                return resultado;
                
            });
            
            var saidaRegra = null;
            
            if(regra.operador === 'e'){
                saidaRegra = Math.min.apply(null, saidasAntecedentes);
            }else{
                saidaRegra = Math.max.apply(null, saidasAntecedentes);
            }
            
            if(!resultadoRegrasInferencia[regra.consequente]){
                resultadoRegrasInferencia[regra.consequente] = [];
            }
            
            resultadoRegrasInferencia[regra.consequente].push(saidaRegra);
            
        });
        
        //Pegando as maiores pertinencia
        resultadoRegrasInferencia = resultadoRegrasInferencia.map(function (item){
            return Math.max.apply(null, item);
        });
        
        
        var tamanhoUniverso = variaveisAlvo._universo[1] - variaveisAlvo._universo[0];
        tamanhoUniverso = tamanhoUniverso > 100 ? tamanhoUniverso : 100;
        
        var dividendo = [];
        
        for (var i = 0; i < resultadoRegrasInferencia.length; i++) {
            
            var grauPertinencia = resultadoRegrasInferencia[i];
            
            if(grauPertinencia > 0){
                                
                var antAscendente = i > 0 && grauPertinencia > resultadoRegrasInferencia[i-1];
                var posAscendente = (!!resultadoRegrasInferencia[i+1] && grauPertinencia < resultadoRegrasInferencia[i+1]);

                
                dividendo[i] = [];
                var termoAlvo = variaveisAlvo.configs[i];
                
                for (var j = 0; j <= tamanhoUniverso; j++) {
                    if ((j == termoAlvo._nucleo[0] || (termoAlvo._nucleo.length === 2 && j >= termoAlvo._nucleo[0] && j <= termoAlvo._nucleo[1])) || 
                        (j >= termoAlvo._suporte[0] && j <= termoAlvo._suporte[1] && (antAscendente === true || posAscendente === false))){
                    
                        dividendo[i].push( j * grauPertinencia );                        
                        
                    }
                }
                
            }
        }
        
        console.log(dividendo, resultadoRegrasInferencia)
        
        var divisor = dividendo.map(function (item, index){
            return item.length * resultadoRegrasInferencia[index];
        });
        
        
        console.log(divisor)
        
        //somando os arrays
        dividendo = dividendo.reduce((a, b) => a + b.reduce((a, b) => a + b, 0), 0);
        divisor = divisor.reduce((a, b) => a + b, 0);
        
        
        console.log(dividendo, divisor)
        
        var resultado = 0;
        
        if (divisor){
            resultado = dividendo/divisor;
        }
        
        
        $scope.resultadoSimulador = Math.round(resultado*100)/100;;
        
    };
    
    
    function funcaoPertinencia(termo, vlEntrada){
        
        var resposta = null;
        
        // = 0
        if ((termo._tipo === 'esquerdo' && vlEntrada >= termo._suporte[1]) ||
            (termo._tipo === 'meio' && (vlEntrada <= termo._suporte[0] || vlEntrada >= termo._suporte[1])) ||
            (termo._tipo === 'direito' && vlEntrada <= termo._suporte[0])) {
            resposta = 0;
        // = 1
        }else if(vlEntrada >= termo._nucleo[0] && vlEntrada <= termo._nucleo[1]){
            resposta = 1;            
        // funcao
        }else{
            if (termo._tipo === 'esquerdo'){
                resposta = (termo._suporte[1] - vlEntrada)/(termo._suporte[1] - termo._nucleo[1]);
            }else if(termo._tipo === 'direito'){
                resposta = (vlEntrada - termo._suporte[0])/(termo._nucleo[0] - termo._suporte[0]);
            }else{
                if (vlEntrada <= termo._nucleo[0]) {
                    resposta = (vlEntrada - termo._suporte[0])/(termo._nucleo[0] - termo._suporte[0]);
                }else if(termo._nucleo.length === 1){
                    resposta = (termo._suporte[1] - vlEntrada)/(termo._suporte[1] - termo._nucleo[0]);
                }else{
                    resposta = (termo._suporte[1] - vlEntrada)/(termo._suporte[1] - termo._nucleo[1]);
                }
            }
        }

        return Math.round(resposta*10)/10;
    }
    
    
});