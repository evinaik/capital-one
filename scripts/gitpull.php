<?php
$output = shell_exec('cd /var/www/capitalOne && /usr/bin/env git pull 2>&1>/var/www/capitalOne/scripts/hook-output.log');
echo $output;
?>