<?php 

#This file will be called using jQuery methodology

#check if the web address was submitted
if(isset($_POST["_id"]) and isset($_POST["rm_"])):
	#clean any extra blank spaces in the user input
	$url = trim($_POST["_id"]);
  
  #validate the url
  if(!filter_var($url, FILTER_VALIDATE_URL) === false):
    #call the python script using a command line form
    #[usage] python [file_name] [webaddress]
	  passthru("python port_scanner_php.py $url");
  else:
    #print error message
    print("<div class='btn btn-danger' style='width:98%'>Sorry! You have entered an invalid URL</div>");
  endif;
  
endif;

?>
