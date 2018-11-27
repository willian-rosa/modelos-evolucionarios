<!DOCTYPE html>
<html lang="pt-br">
    <head>
        <meta charset="utf-8">
        <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/angularjs/1.7.5/angular.min.js"></script>
        <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/angularjs/1.7.5/angular-route.js"></script>
        <script type="text/javascript" src="src/framework/main.js"></script>
        <script type="text/javascript" src="src/framework/projeto.js"></script>
        <script type="text/javascript" src="src/framework/simular.js"></script>
        
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="Description" lang="en" content="ADD SITE DESCRIPTION">
        <meta name="author" content="ADD AUTHOR INFORMATION">
        <meta name="robots" content="index, follow">

        <!-- icons -->
        <link rel="apple-touch-icon" href="src/img/apple-touch-icon.png">
        <link rel="shortcut icon" href="favicon.ico">

        <!-- Bootstrap Core CSS file -->
        <link rel="stylesheet" href="src/css/bootstrap.min.css">

        <!-- Override CSS file - add your own CSS rules -->
        <link rel="stylesheet" href="src/css/styles.css">
        
        
             <!-- JQuery scripts -->
        <script src="src/js/jquery-1.11.2.min.js"></script>

        <!-- Bootstrap Core scripts -->
        <script src="src/js/bootstrap.min.js"></script>
        
    </head>

    <body ng-app="frameworkDifuso">
        <!-- Navigation -->
        <nav class="navbar navbar-fixed-top navbar-inverse" role="navigation">
            <div class="container-fluid">
                <!-- Brand and toggle get grouped for better mobile display -->
                <div class="navbar-header">
                    <a class="navbar-brand" href="#">Framework</a>
                </div>
                <!-- /.navbar-header -->

                <!-- Collect the nav links, forms, and other content for toggling -->
                <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                    <ul class="nav navbar-nav">
                        <li><a href="#!">Dashboard</a></li>
                        <li><a href="#!projeto">Cadastro de Projeto</a></li>
                    </ul>
                </div>
                <!-- /.navbar-collapse -->
            </div>
            <!-- /.container-fluid -->
        </nav>
        <!-- /.navbar -->

        <!-- Page Content -->
        <div class="container-fluid">
            <div class="row">
                <div class="col-sm-12">

                    <div ng-view></div>

                </div>
            </div>
            <!-- /.row -->
        </div>
    </body>
</html>

