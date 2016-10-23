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
		$data[0][] = 10;
	}
}

echo json_encode($data);
?>
<!-- for i in xrange(1, len(lines)):
	deaths = 0.0
	if lines[i][26].strip():
		deaths = float(lines[i][26])
	injuries = 0.0
	if lines[i][30].strip():
		injuries = float(lines[i][30])
	nums.append(deaths + injuries)
	data += jFormat(lines[i][8]) + ', ' + jFormat(lines[i][9]) + ', #' + str(t) + ', '
	t += 1

# m = numpy.mean(nums)
# s = numpy.std(nums)
# nums = [(i - m) / s for i in nums]
hi = max(nums)
lo = min(nums)
nums = [(i - lo) / (hi - lo) for i in nums]
count = 0

while '#' in data:
	j = data.find('#' + str(count))
	data = data[:j] + str(nums[count]) + data[j+2:]
	count += 1

data = data[:-2]
data += ']' -->