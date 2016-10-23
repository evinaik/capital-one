<?php
// $data = file_get_contents('https://www.ngdc.noaa.gov/nndc/struts/results?type_0=Exact&query_0=$HAZ_EVENT_ID&t=102557&s=50&d=54&dfn=volerup.txt');
// $temp = explode("\n", $data);
// $data = [];
// for ($i = 1, $size = count($temp); $i < $size; $i++) {
// 	if (!empty($temp[$i])) {
// 		$erupt = explode("\t", $temp[$i]);
// 		$lat = floatval($erupt[8]);
// 		$lon = floatval($erupt[9]);
// 		$deaths = 0.0;
// 		$injuries = 0.0;
// 		if (!empty($erupt[26]))
// 			$deaths = floatval($erupt[26]);
// 		if (!empty($erupt[30]))
// 			$injuries = floatval($erupt[30]);
// 		$data[] = $lat;
// 		$data[] = $lon;
// 		$data[] = $deaths + $injuries;
// 	}
// }

// echo json_encode($data);
<?php
ini_set('display_errors', 1);
require "twitteroauth/autoload.php";

use Abraham\TwitterOAuth\TwitterOAuth;

$ckey = 'VTiKXADVTl6WR1r0d3I28VD4y';
$csec = 'owYftIYKzxdYvSUEdEWkM88emP4SMay61AsXhEnroKRY8NlvsC';
$access_token = '86003535733194752-ZA7oCmdpKxVuTWM9yPZGvKwmiRzpkZ9';
$access_token_secret = 'YZbwWkV6pRHEfO7dQ8HtOJFw5ZNdy3WV1uCp0r6Kkwma1';

$connection = new TwitterOAuth($ckey, $csec, $access_token, $access_token_secret);
$content = $connection->get("account/verify_credentials");

echo $content;
?>