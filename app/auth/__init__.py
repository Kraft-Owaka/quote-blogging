
{% import 'bootstrap/wtf.html' as wtf%}

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>SIGN IN</title>

    <!=-- Bootstrap core CSS -->
    <link href="{{url_for('static', filename='css/bootstrap.min.css')}}" rel="stylesheet">
    <link href="{{url_for('static', filename='css/all.css')}}" rel="stylesheet">

</head>

<body>
    <div class="container">
        <div class="row">
            <div class="col-lg-10 col-xl-9 mx-auto">
                <div class="card card-signin flex-row my-5">
                    <div class="card-img-left d-none d-md-flex">
                        <!-- Background image for card set in CSS! -->
                    </div>
                    <div class="card-body">
                        <h5 class="card-title text-center">Sign in</h5>

                        {% for message in get_flashed_messages()%}
                        <div class ="alert alert-danger">
                            <button type="button" class ="close" data-dismiss="alert">&times;</button>
                            {{message}}   
         
{% import 'bootstrap/wtf.html' as wtf%}

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>SIGN IN</title>

    <!-- Bootstrap core CSS -->
    <link href="{{url_for('static', filename='css/bootstrap.min.css')}}" rel="stylesheet">
    <link href="{{url_for('static', filename='css/all.css')}}" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="{{url_for('static', filename='css/registration.css')}}" rel="stylesheet">

</head>

<body>
    <div class="container">
        <div class="row">
            <div class="col-lg-10 col-xl-9 mx-auto">
                <div class="card card-signin flex-row my-5">
                    <div class="card-img-left d-none d-md-flex">
                        <!-- Background image for card set in CSS! -->
                    </div>
                    <div class="card-body">
                        <h5 class="card-title text-center">Sign in</h5>

                        {% for message in get_flashed_messages()%}
                        <div class ="alert alert-danger">
                            <button type="button" class ="close" data-dismiss="alert">&times;</button>
                            {{message}}   
                        </div>
                        {%endfor%}
                        <!-- Login Form -->
                        {{wtf.quick_form(login_form)}}
                        <p>Don't have an account?<a href="{{url_for('auth.register')}}">Sign up here</a></p>
                        
                    </div>
                </div>
            </div>
        </div>
    </div>
    <script src="{{url_for('static', filename='css/jquery.slim.min.js')}}"></script>
    <script src="{{url_for('static', filename='css/bootstrap.bundle.min.js')}}"></script>

</body>

</html>               </div>
                        {%endfor%}
                        <!-- Login Form -->
                        {{wtf.quick_form(login_form)}}
                        <p>Don't have an account?<a href="{{url_for('auth.register')}}">Sign up here</a></p>
                        
                    </div>
                </div>
            </div>
        </div>
    </div>
    <script src="{{url_for('static', filename='css/jquery.slim.min.js')}}"></script>
    <script src="{{url_for('static', filename='css/bootstrap.bundle.min.js')}}"></script>

</body>

</html>