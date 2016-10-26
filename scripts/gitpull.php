<?php
$output = shell_exec('cd /var/www/capitalOne && /usr/bin/env git pull');
echo $output;
?>