<?php
$output = shell_exec('cd /var/www/capitalOne && /usr/bin/env git pull 2>&1 > hook-output.log');
echo $output;
?>