<!DOCTYPE>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta http-equiv="expires" content="Sun, 01 Jan 2014 00:00:00 GMT"/>
<meta http-equiv="pragma" content="no-cache" />

<title>Mercado libre, detecta autos</title>
</head>

<body>
<?php
	$picture=filter_input(INPUT_GET, 'picture');
	$level=filter_input(INPUT_GET, 'level');

	$command = 'ML/app/detect_AutoNivel.py ' . '-n ' . $level . ' -o ' . 'galeria/1.jpg' . ' -u ' . $picture;

	passthru($command);
	echo "Imagen";
	echo '<img src=galeria/1.jpg width="400" >'."\n";
?>

