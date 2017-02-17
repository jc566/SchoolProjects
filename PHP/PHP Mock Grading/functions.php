<?php
function grid_status($admin, $user,$password)
{

if (!empty($admin) && empty($user) && !empty($password))return 1;
if (!empty($admin) && !empty($user) && !empty($password))return 2;
if (empty($admin) && !empty($user) && !empty($password))return 3;

die("no valid scenario");

}

function admin ($admin, $password)
{
if (   ($admin == "Joe3") 
    &&  ($password == "67890") ) return ;

die ("invalid");

}

function sql ($c, $user, $pwd)

{
if ($c == 1) return "select * from Students";
if ($c == 2) return "select * from Students where user = '$user'"; 
if ($c == 3) return "select * from Students where user = '$user' and pwd = '$password'"; 
die ("invalid");

}

function get_R($dbh,$s) {


($t=mysqli_query ($dbh,$s))or die (mysql_error());
if(mysqli_num_rows($t)==0) die ("no data");
$out.= "Number of rows retrieved from Students is ".mysqli_num_rows ($t). "<br><br>";
$out.="<table border=2>";
$out.="<tr><th>user</th> <th>email</th> </tr>";

while($r=mysqli_fetch_array($t))
{
$user = $r("user");
$email= $r("email");
$out.="<tr> <td>$user</td> <td>$email</td> </tr>";

}
$out.= "</table>";
}
function EMail (){
    $sentTo = "jchoi1989@gmail.com";
	$subject = "Your Grades for Assignment 01 IT202 Professor McHugh";
	$headers  = 'MIME-Version: 1.0' . "\r\n";
	$headers .= 'Content-type: text/html; charset=iso-8859-1' . "\r\n";
	$headers .= 'From: <jchoi1989@gmail.com>' . "\r\n";
    mail($to,$subject,$out,$headers);

}
function message($name){
    print "<br>MESSAGE: The $name input is not defined ";
}


function get_clean_input($name, &$result, $dbh, $debug=true){
    if(!isset($_GET[$name]) || empty(trim($_GET[$name]))){
        if($debug == true) print "<br>From clean: $name is undefined or empty."; return false;
    }
    $result = mysqli_real_escape_string($dbh,$_GET[$name]);
    if($debug == true) print "<br>From clean: Transformed $name is $result";
    return true;
}

function is_in_R($user,$email,$dbh){
    $s = "select * from Students where user='$user' or email='$email'";
    print "<br>From is_in_R SQL: $s";
    ($t=mysqli_query($dbh,$s)) or die (mysqli_error());
    if(mysqli_num_rows($t) > 0)return true; else{die("<br>user or email already in R. Try again.");}
}

function put_in_R($user,$email,$password,$fullname,$address,$dbh){
    $s = "insert into Students (user,email,pwd,fullname,address,numcourses,registered) 
    values ('$user','$email', sha1('$password'),'$fullname','$address','0','NOW()')";
    print "<br>From put_in_R SQL: $s";
    ($t=mysqli_query($s)) or die (mysqli_error());
}

function put_initial_G($user,$course,$dbh){
	
	$s = "select * from Grades WHERE user='$user' AND course='$course'";
	$t=mysqli_query($dbh,$s);
	if(mysqli_num_rows($t) > 0) return;
	else{

		$g = "INSERT INTO Grades (User, Course, A1, A1S, A2, A2S, PART, TOTAL, PERCENT) VALUES('$user', '$course', '0000', '0000-00-00', '0000', '0000-00-00', '0000', '0000', '0000')";
		mysqli_query($g)or die (mysqli_error());
    echo ("<br>$g<br>");
	}
}
function update_G($segment, $user, $course,$dbh) {
    $a1 = "UPDATE Grades SET $segment WHERE user='$user' AND course='$course'"; echo "$s";
    mysqli_query($a1) or die (mysqli_error());
    echo ("<br>$a1<br>");
}

function clean($n, &$r){
	$r = $_GET[$n];
}
?>