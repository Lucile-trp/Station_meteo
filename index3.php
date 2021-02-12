<html>
<head>
    <meta charset="utf-8" />
    <link href="css/style.css" rel="stylesheet" />
	<title>Station météo</title>
</head>
<body>
<nav class="navbar navbar-dark sticky-top bg-dark flex-md-nowrap p-0">
	<?php
	require ("includes/header.php");
  require_once('meteo.php');
    ?>
    </nav>

    <div class="container-fluid">
      <div class="row">
        <main role="main" class="col-md-9 ml-sm-auto col-lg-10 pt-3 px-4">
          <div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pb-2 mb-3 border-bottom">
            <h1 class="h2">Graphique</h1>
            <div class="btn-toolbar mb-2 mb-md-0">
              <div class="btn-group mr-2">
                   <?php /*        
                  <div>
                    <!-- Facebook -->
                      <a target="_blank" title="Facebook" href="https://www.facebook.com/sharer.php?u=https://tontonduweb.com/previews-warc/genieCivil/article1.html" rel="nofollow" onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=500,width=700');return false;"><img src="plugins/iconrs/facebook_icon.png" alt="Facebook" /></a>
                    <!-- //Facebook -->

                    <!-- Twitter -->
                      <a target="_blank" title="Twitter" href="https://twitter.com/share?url=https://bit.ly/2sI7H3v" rel="nofollow" onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=400,width=700');return false;"><img src="plugins/iconrs/twitter_icon.png" alt="Twitter" /></a>
                    <!-- //Twitter -->
                    
                    <!-- Email -->
                      <a target="_blank" title="Envoyer par mail" href="mailto:?Subject=Regarde ça c'est cool !&amp;Body=regarde%20cet%20article%20c'est%20super !%20 https://tontonduweb.com/previews-warc/genieCivil/article1.html" rel="nofollow"><img src="plugins/iconrs/email_icon.png" alt="email" /></a>
                    <!-- //Email -->
                  </div>
                    <button class="btn btn-sm btn-outline-secondary">Partager</button>
                    <!--<button class="btn btn-sm btn-outline-secondary">Export</button>-->
                  </div>
     */?>             
                <span data-feather="calendar"></span>
                <div class="btn-calendar">
                <button class="btn btn-sm btn-outline-secondary dropdown-toggle active" style="border-radius: 8px" name="day" type="button" onclick="window.location.href='index.php';">Aujourd'hui</button>
                <button class="btn btn-sm btn-outline-secondary dropdown-toggle" style="border-radius: 8px" name="week" type="button" onclick="window.location.href='index2.php';">Cette semaine</button>
                <!--<button class="btn btn-sm btn-outline-secondary dropdown-toggle" style="border-radius: 8px" name="month" type="button"onclick="window.location.href='index3.php';">Ce mois</button>-->
                </div>
            </div>
            
          </div>   
<!----------DECLARATION VARIABLE=FONTION------------------>
<?php

  $last=getLastData();
    //$last[0][0]=id     $last[0][1]=temperature    $last[0][2]=humidité     $last[0][3]=date
  $weekData=getWeekData();
    //$week[$i][0]=id     $week[$i][1]=temperature    $week[$i][2]=humidité     $week[$i][3]=date
  $dayData=getDayData();
    //$day[$i][0]=id     $day[$i][1]=temperature    $day[$i][2]=humidité     $day[$i][3]=date  

?>
<!----------FIN DECLARATION VARIABLE=FONTION------------->
<?php
/**********************TRAVAIL SUR LES DATES************************/
/* 
$j=0;
  $olddate1=strtotime($weekData[$j][3]);
  $date1=date('d/m/Y',$olddate1);
  $temp1=$weekData[$j][1];

  $i=1;
  $olddate2=strtotime($weekData[$i][3]);
  $date2=date('d/m/Y',$olddate2);
  $temp2=$weekData[$i][1];
  if($date1===$date2){
    while($date1===$date2){
      $temp1=+$temp2;
      $i++;
    }
  }
  echo $date1.' : '.$temp1.'°C et $i='.$i;
                         
    

    $oldheure=strtotime($dayData[0][3]);
    $heure=date('H',$oldheure);  
    $h=intval($heure);

      for($h=intval($heure);$h>=0;$h--){
          echo $dayData[$i][1].',';
        }
      }*/
      $sonde=getSonde();
      echo $sonde[4];


/********************FIN TRAVAIL SUR LES DATES**********************/
?>
	
</body>
</html>