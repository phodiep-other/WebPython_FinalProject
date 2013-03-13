<!DOCTYPE html>
<html>

<head>
  <title>CraigsList Apartment Search App</title>
  <style type="text/css">
  body {
    padding-left: 5em;
    padding-right: 5em;}
  ul.menubar {
    position: fixed;
    top: 2em;
    left: 1em;
    display:block;
    width: 9em }
  </style>
</head>

<body style="background-color:#81BEF7";>
<ul id=menubar>
  <li><a href="../search">New Search</a>
</ul>



<h1 style="text-align:center;">Welcome to the CL app</h1>
  
<h2 style="text-align:center;"> {{title or 'No title'}}</h2>
  
<p> 
    %body()
  </p>

</body>

</html>
