<?php   
//getAllData();

/***********SECTION VALIDE
 $data= getTemp4Day();
             foreach($data['list'] as $key => $value){
                echo $key."<br>";
                if(is_array($value)){
                    foreach($value['main'] as $key => $value){
                         echo $key." : ".$value."<br>";
                    }
                }
            }
*************************/             
function quelleHeure(){
    $h= date('H');
    return $h;
}

function quelJour($i){
    $hier=strtotime('-'.$i.' day');
    $jour = date('l',$hier);
    $date=date('d/m',$hier);
    echo $jour.' '.$date;
}
function quelDate($i){
    $demain = date('d-m', strtotime('+'.$i.' day'));
    echo $demain;
}

//GOOD avec API Zeus
    $uri='http://192.168.43.103:5000'; //URI du local de Lucille à modifier dans CHAQUE fonction
    $uri='http://192.168.43.60:5000'; //URI du Raspberry à mettre dans CHAQUE fonction
    //console.log($uri);

function getLastData(){
    $urlZeus='http://192.168.43.60:5000/api/v1/mesure/last';
    //connexion à l'API
    $curl=curl_init($urlZeus);
        //SETUP  
        curl_setopt($curl,CURLOPT_CAINFO,__DIR__ . DIRECTORY_SEPARATOR . 'cert.cer');//vérifier le certificat https téléchargé en amont
        curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);//Activation de l'option CURLOPT_RETURNTRANSFER de curl_exec => $data contient le resultat
        curl_setopt($curl,CURLOPT_TIMEOUT,2);//définir le temps de chargement
    $last=curl_exec($curl);
    //test si la connexion à l'API fonctionne
    if ($last ===false){
        var_dump(curl_error($curl));
    }else {
        if(curl_getinfo($curl,CURLINFO_HTTP_CODE)===200){//Si code HTTP = 200, alors continuer normalement
            $last=json_decode($last,true);
            /*echo'<pre>';
            echo var_dump($last);
            echo'</pre>';*/
        }
    } 
    curl_close($curl);
    return $last;

}
function getAllData(){
    $urlZeus='http://192.168.43.60:5000/api/v1/mesures';
    //connexion à l'API
    $curl=curl_init($urlZeus);
        //SETUP  
        curl_setopt($curl,CURLOPT_CAINFO,__DIR__ . DIRECTORY_SEPARATOR . 'cert.cer');//vérifier le certificat https téléchargé en amont
        curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);//Activation de l'option CURLOPT_RETURNTRANSFER de curl_exec => $data contient le resultat
        curl_setopt($curl,CURLOPT_TIMEOUT,2);//définir le temps de chargement
    $allData=curl_exec($curl);
    //test si la connexion à l'API fonctionne
    if ($allData ===false){
        var_dump(curl_error($curl));
    }else {
        if(curl_getinfo($curl,CURLINFO_HTTP_CODE)===200){//Si code HTTP = 200, alors continuer normalement
            $allData=json_decode($allData,true);
            /*echo'<pre>';
            echo var_dump($allData);
            echo'</pre>';*/
        }
    } 
    curl_close($curl);
    return $allData;

}
function getDayData(){
    $urlZeus='http://192.168.43.60:5000/api/v1/mesures/day';
    //connexion à l'API
    $curl=curl_init($urlZeus);
        //SETUP  
        curl_setopt($curl,CURLOPT_CAINFO,__DIR__ . DIRECTORY_SEPARATOR . 'cert.cer');//vérifier le certificat https téléchargé en amont
        curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);//Activation de l'option CURLOPT_RETURNTRANSFER de curl_exec => $data contient le resultat
        curl_setopt($curl,CURLOPT_TIMEOUT,2);//définir le temps de chargement
    $dayData=curl_exec($curl);
    //test si la connexion à l'API fonctionne
    if ($dayData ===false){
        var_dump(curl_error($curl));
    }else {
        if(curl_getinfo($curl,CURLINFO_HTTP_CODE)===200){//Si code HTTP = 200, alors continuer normalement
            $dayData=json_decode($dayData,true);
            /*echo'<pre>';
            echo var_dump($dayData);
            echo'</pre>';*/
        }
    } 
    curl_close($curl);
    return $dayData;
}
function getWeekData(){
    $urlZeus='http://192.168.43.60:5000/api/v1/mesures/week';
    //connexion à l'API
    $curl=curl_init($urlZeus);
        //SETUP  
        curl_setopt($curl,CURLOPT_CAINFO,__DIR__ . DIRECTORY_SEPARATOR . 'cert.cer');//vérifier le certificat https téléchargé en amont
        curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);//Activation de l'option CURLOPT_RETURNTRANSFER de curl_exec => $data contient le resultat
        curl_setopt($curl,CURLOPT_TIMEOUT,2);//définir le temps de chargement
    $weekData=curl_exec($curl);
    //test si la connexion à l'API fonctionne
    if ($weekData ===false){
        var_dump(curl_error($curl));
    }else {
        if(curl_getinfo($curl,CURLINFO_HTTP_CODE)===200){//Si code HTTP = 200, alors continuer normalement
            $weekData=json_decode($weekData,true);
            /*echo'<pre>';
            echo var_dump($weekData);
            echo'</pre>';*/
        }
    } 
    curl_close($curl);
    return $weekData;

}
function getSonde(){
    $urlZeus='http://192.168.43.60:5000/api/v1/sonde/1';
    //connexion à l'API
    $curl=curl_init($urlZeus);
        //SETUP  
        curl_setopt($curl,CURLOPT_CAINFO,__DIR__ . DIRECTORY_SEPARATOR . 'cert.cer');//vérifier le certificat https téléchargé en amont
        curl_setopt($curl,CURLOPT_RETURNTRANSFER,true);//Activation de l'option CURLOPT_RETURNTRANSFER de curl_exec => $data contient le resultat
        curl_setopt($curl,CURLOPT_TIMEOUT,2);//définir le temps de chargement
    $last=curl_exec($curl);
    //test si la connexion à l'API fonctionne
    if ($last ===false){
        var_dump(curl_error($curl));
    }else {
        if(curl_getinfo($curl,CURLINFO_HTTP_CODE)===200){//Si code HTTP = 200, alors continuer normalement
            $last=json_decode($last,true);
            /*echo'<pre>';
            echo var_dump($last);
            echo'</pre>';*/
        }
    } 
    curl_close($curl);
    return $last;

}
//END API Zeus



?>