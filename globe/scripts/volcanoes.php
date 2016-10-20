<?php
$data = file_get_contents('https://www.ngdc.noaa.gov/nndc/struts/results?type_0=Exact&query_0=$HAZ_EVENT_ID&t=102557&s=50&d=54&dfn=volerup.txt');
$temp = explode("\n", $data);
$data = [];
$data[] = [];
for ($i = 1, $size = count($temp); $i < $size; $i++) {
	if (!empty($temp[$i])) {
		$erupt = explode("\t", $temp[$i]);
		$lat = floatval($erupt[8]);
		$lon = floatval($erupt[9]);
		$deaths = 0.0;
		$injuries = 0.0;
		if (!empty($erupt[26]))
			$deaths = floatval($erupt[26]);
		if (!empty($erupt[30]))
			$injuries = floatval($erupt[30]);
		$data[0][] = $lat;
		$data[0][] = $lon;
		$data[0][] = $deaths + $injuries;
	}
}

echo json_encode($data);
?>
