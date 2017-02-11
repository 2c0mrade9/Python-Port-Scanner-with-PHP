<!DOCTYPE html>
<html lang="en">
  <head>
  <meta charset="utf-8">
  <title>My Website - Socket Checker</title>
  <meta name="Description" content="">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/css/bootstrap.min.css" integrity="sha384-rwoIResjU2yc3z8GV/NPeZWAv56rSmLldC3R/AZzGRnGxQQKnKkoFVhFQhNUwEyJ" crossorigin="anonymous">
  <script src="https://code.jquery.com/jquery-3.1.1.min.js"></script>
  </head>

  <body>
  
  <nav class="navbar navbar-inverse navbar-static-top">
      <div class="container">
        <div class="navbar-header">
          <a href="" class="navbar-brand"><img alt="" width="300px" height="90" src="mylogo.jpg"></a>
        </div><Br>
        <p class="navbar-text navbar-right hidden-xs">Ports Scanner</p>
      </div><!-- container -->
    </nav>
    <div id="main-container">
    <div class="container">
    
    <div class="col-md-7 col-sm-12">
      <div class="panel panel-default">
        <div class="btn btn-info" style="width:100%;border-radius:0px;height:35px;">
          <h4 class="panel-title">Enter the Website Domain Name</h4>
        </div>
        <div class="panel-body">
          <p class="lead"></p>
		  <div class="form-group">
			<label for="webaddress">Website Address:</label>
			<input type="url" class="form-control" id="webaddress"><br>
			<small><em>http://www.websitesite.com</em></small>
		  </div>
		  <button id="run_checks" type="submit" class="btn btn-default">Run Checks</button>
		
        </div>
      </div>
	  </div>
    
    <!-- UserAgent -->
	  <div class="col-md-7 col-sm-12">
      <div class="panel panel-default">
        <div class="btn btn-info" style="width:100%;border-radius:0px;height:35px;">
          <h4 class="panel-title">Checking the ports of the Website Provided by you</h4>
        </div>
        <div class="panel-body">
          <div class="display_results"></div>
        </div>
      </div>
	  </div>
    
     <footer class="sitefooter">
      <div class="container">
        <div class="row">
          <div class="btn btn-info" style="width:100%;border-radius:0px;height:35px;">
            <p>Checking the Opened Ports on a Network</p>
          </div>
        </div>
      </div>
    </footer>
    
    </div>
    </div>
    
    <script>
    $("#run_checks").click(function() {

      //set the display to null
      $(".display_results").html('');
      //set a variable for the user input
      var url = $("#webaddress").val();
      //regular expression for website address
      var RegExp = /(ftp|http|https):\/\/(\w+:{0,1}\w*@)?(\S+)(:[0-9]+)?(\/|\/([\w#!:.?+=&%@!\-\/]))?/;
      //check if the value matches the pattern provided
      if(!RegExp.test(url)){
        //alert errror
        alert("Sorry! Enter a valid URL");
        $("#webaddress").focus();
      } else {
        $.ajax({
            type: "POST",
            data: "rm_&_id="+url,
            url: "checking_ports.php",
            beforeSend: function() {
              $(".display_results").html('<br clear="all"><div align="center">Loading information <img src="loadings.gif" align="absmiddle" title="Loading..." /></div><br clear="all">');
            },success: function(response) {
              $(".display_results").html(response);
            }
          });
        }
    });
    </script>
    
  </body>
  </html>
