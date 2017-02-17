<?php
include (  "account.php"     ) ;
include ( "functions.php") ;

( $dbh = mysqli_connect ( $hostname, $username, $password ) )
            or die ( "Unable to connect to MySQL database" );
print "Connected to MySQL<br><br>";
mysqli_select_db( $dbh, $project );


$OK = true;
if(!get_clean_input("password",$password,$dbh)) {message("password");$OK = false;}
if(!get_clean_input("user",$user,$dbh)){message("user");$OK=false;}
if(!get_clean_input("course",$course,$dbh)){message("course");$OK=false;}

//Gatekeepers
if(!$OK) die("<br>Bad data. Badbye. ");
admin("Joe3",$password);
if(! is_in_R($user,"",$dbh)) die(" ");

//Get Grades & Dates
get_clean_input("A1", $A1,$dbh);
get_clean_input("A2", $A2,$dbh);
get_clean_input("A1S", $A1S,$dbh);
get_clean_input("A2S", $A2S,$dbh);

put_initial_G($user,$course); 

//Conditional Grade Change
if (isset ($_GET["A1C"])) {
    update_G("A1 = '$A1' ", $user, $course,$dbh);
    update_G("A2 = '$A2' ", $user, $course,$dbh);
	update_G("A1S = '$A1S' ",$user,$course,$dbh);
	update_G("A2S = '$A2S' ",$user,$course,$dbh);
	
}

if (get_clean_input("participation", $Part)) {
    mysqli_query("UPDATE Grades SET `PART`= PART+'$Part' 
                WHERE user='$user' AND course='$course'");
}
mysqli_close($dbh);
?>

