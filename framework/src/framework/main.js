angular.module('frameworkDifuso', ['ngRoute']);

angular.module('frameworkDifuso').config(function($routeProvider) {
    $routeProvider
    .when("/", {
        templateUrl : "src/tpl/main.html"
    })
    .when("/projeto", {
        templateUrl : "src/tpl/projeto.html"
    })
    .when("/projeto/:id", {
        templateUrl : "src/tpl/projeto.html"
    })
    .when("/simular/:id", {
        templateUrl : "src/tpl/simular.html"
    });
});


angular.module('frameworkDifuso').controller('main', function($scope, $window) {
    
    $scope.projetos = [];
    
    if (!$window.localStorage.getItem('projetos')) {
        $window.localStorage.setItem('projetos', '[{"variaveis": [{"nome": "Temperatura", "universo": "0,50", "configs": [{"termo": "Fria", "suporte": "0,20", "nucleo": "0,10"}, {"termo": "Média", "suporte": "10,30", "nucleo": "20"}, {"termo": "Alta", "suporte": "20,50", "nucleo": "30,50"} ] }, {"nome": "Umidade", "universo": "0,100", "configs": [{"termo": "Baixa", "suporte": "0,50", "nucleo": "0,25"}, {"termo": "Média", "suporte": "25,75", "nucleo": "50"}, {"termo": "Alta", "suporte": "50,100", "nucleo": "75,100"} ] }, {"nome": "Irrigação", "universo": "0,120", "configs": [{"termo": "Pequena", "suporte": "0,60", "nucleo": "0,30"}, {"termo": "Média", "suporte": "30,90", "nucleo": "60"}, {"termo": "Grande", "suporte": "60,120", "nucleo": "90,120"} ] } ], "regrasInferencia": [{"operador": "e", "antecedentes": [{"variavel": 0, "termo": 0 }, {"variavel": 1, "termo": 2 } ], "consequente": 0 }, {"operador": "e", "antecedentes": [{"variavel": 0, "termo": 1 }, {"variavel": 1, "termo": 1 } ], "consequente": 1 }, {"operador": "e", "antecedentes": [{"variavel": 0, "termo": 0 }, {"variavel": 1, "termo": 1 } ], "consequente": 1 }, {"operador": "e", "antecedentes": [{"variavel": 0, "termo": 2 }, {"variavel": 1, "termo": 0 } ], "consequente": 2 } ], "nome": "Irrigação", "id": "1", "variavelAlvo": "2"} ]');
    }
    
    $scope.projetos = JSON.parse($window.localStorage.getItem('projetos'));
    
    
    
});