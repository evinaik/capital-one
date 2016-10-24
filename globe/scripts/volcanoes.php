<?php
ini_set('display_errors', 1);
require "twitteroauth/autoload.php";

use Abraham\TwitterOAuth\TwitterOAuth;

$ckey = 'VTiKXADVTl6WR1r0d3I28VD4y';
$csec = 'owYftIYKzxdYvSUEdEWkM88emP4SMay61AsXhEnroKRY8NlvsC';
$access_token = '786003535733194752-ZA7oCmdpKxVuTWM9yPZGvKwmiRzpkZ9';
$access_token_secret = 'YZbwWkV6pRHEfO7dQ8HtOJFw5ZNdy3WV1uCp0r6Kkwma1';

$connection = new TwitterOAuth($ckey, $csec, $access_token, $access_token_secret);
$content = $connection->get("account/verify_credentials");
$statuses = $connection->get("search/tweets", ["q" => "twitterapi", "lang" => "en"]);

echo json_encode($statuses);
?>