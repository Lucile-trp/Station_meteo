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

    <div class="meteonow"> 
        <h3>Actuellement à Saint-Étienne-du-Rouvray il fait :</h3>
        <div class="meteonow-img">
               <?php
               if($last[0][2] >= '60' && $last[0][1] >= '1'){
                   echo "<img src='img/rain_light.png'/>";
               }
               if($last[0][2] <= '60' && $last[0][1] >= '-10' && $last[0][1] <= '5'){
                   echo "<img src='img/partly_cloudy.png'/>";
               }
               if($last[0][2] <= '60' && $last[0][1] >= '6'){
                   echo "<img src='img/sunny.png'/>";
               }
               if($last[0][2] >= '60' && $last[0][1] <= '0'){
                   echo "<img src='img/snow.png'/>";
               }
               ?>
            <div class="temp">
                <?php
                echo'' .$dayData[0][1].'°C';
                ?>
            </div>
            <div class="humidity">
                <?php
                echo'' .$dayData[0][2].'%';
                ?>
            </div>
        </div>
    </div>

    <div class="container-fluid">
      <div class="row">
        <main role="main" class="col-md-9 ml-sm-auto col-lg-10 pt-3 px-4">
          <div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pb-2 mb-3 border-bottom">
              <div class="meteo">

            </div>
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
<!------------------------GRAPHIQUE SEMAINE---------------------------->
<div class="graphique"><canvas id="canvas_graphique" width="700" height="380"></canvas></div> 
<script>
var lineChartData = {
			labels: ["Today","<?php quelJour(1);?>","<?php quelJour(2);?>","<?php quelJour(3);?>","<?php quelJour(4);?>","<?php quelJour(5);?>","<?php quelJour(6);?>"],
			datasets: [{
				label: 'Températures (°C)',
				borderColor: 'rgba(176, 58, 46, 1)',
				backgroundColor: 'rgba(176, 58, 46, 1)',
				fill: false,
				data: [
          <?php
            for($i=0;$i<=6;$i++){
              if($i===6){
                echo $weekData[$i][1];//Afficher temperature
              }
              else {
                echo $weekData[$i][1].',';
              }
            }
          ?>
				],
				yAxisID: 'y-axis-1',
			}, {
				label: 'Humidité (%)',
				borderColor: 'rgba(0, 175, 236, 1)',
				backgroundColor: 'rgba(0, 175, 236, 1)',
				fill: false,
				data: [
          <?php 
            for($i=0;$i<=6;$i++){
              if($i===6){
                echo $weekData[$i][2];//Afficher Humidité
              }
              else {
                echo $weekData[$i][2].',';
              }
            }
          ?>
				],
				yAxisID: 'y-axis-2'
			}]
		};

		window.onload = function() {
			var ctx = document.getElementById('canvas_graphique').getContext('2d');
			window.myLine = Chart.Line(ctx, {
				data: lineChartData,
				options: {
					responsive: true,
					hoverMode: 'index',
					stacked: false,
					title: {
						display: true,
						text: 'Températures et Humidité des 7 derniers jours'
					},
					scales: {
						yAxes: [{
							type: 'linear', // only linear but allow scale type registration. This allows extensions to exist solely for log scale for instance
							display: true,
							position: 'left',
							id: 'y-axis-1',
              ticks: {
                min: -20,
                max: 40,
              }
						}, {
							type: 'linear', // only linear but allow scale type registration. This allows extensions to exist solely for log scale for instance
							display: true,
							position: 'right',
							id: 'y-axis-2',
              ticks: {
                min: 0,
                max: 100,
              },

							// grid line settings
							gridLines: {
								drawOnChartArea: false, // only want the grid lines for one axis to show up
							},
						}],
					}
				}
			});
		};

</script>	
<!------------------------FIN GRAPHIQUE SEMAINE--------------------------->
<!--------------------------TABLEAU SEMAINE------------------------------->
          <h2>Tableau de valeurs</h2>
          <div class="table-responsive">
              <table class="table table-striped table-sm" style="text-align: center;width: 100%;">
                  <thead>
                      <tr>
                          <th>Date</th>
                          <th>Heure</th>
                          <th>Température</th>
                          <th>Humidité</th>
                      </tr>
                  </thead>
                  <tbody>
                      <?php
                      //Affichage ligne tableau pour 1 heure
                      
                      for($i=0;$i<=6;$i++){
                        $olddate=strtotime($weekData[$i][3]);
                        $oldheure=strtotime($weekData[$i][3]);
                        $date=date('l d/m/Y',$olddate);
                        $heure=date('H:i',$oldheure);
                        echo '
                        <tr>
                          <td>'.$date.'</td>
                          <td>'.$heure.'</td>
                          <td>'.$weekData[$i][1].'°C</td>
                          <td>'.$weekData[$i][2].'%</td>
                        </tr>';                          
                      }
                      ?>
                  </tbody>
              </table>
          </div>
<!------------------------FIN TABLEAU MOIS----------------------------->
        </main>
      </div>
    </div>

    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script>window.jQuery || document.write('<script src="../../../../assets/js/vendor/jquery-slim.min.js"><\/script>')</script>
    <!--<script src="../../../../assets/js/vendor/popper.min.js"></script>-->
    <script src="assets/bootstrap-4.0.0/dist/js/bootstrap.min.js"></script>
    <script src="assets/chart-js/Chart.js"></script>
    <script src="assets/chart-js/Chart.min.js"></script>

    <!-- Icons -->
    <script src="https://unpkg.com/feather-icons/dist/feather.min.js"></script>
    <script>
      feather.replace()
    </script>





	
</body>
</html>