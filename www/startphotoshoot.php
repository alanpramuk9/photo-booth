<?php
  // Execute the python script with the JSON data
  // // $result = shell_exec('python /path/to/myScript.py ' . escapeshellarg(json_encode($data)));
  $result = shell_exec('python3 camera.py ' . escapeshellarg(json_encode($_POST)));

  // // Decode the result
  $resultData = json_decode($result, true);

  echo json_encode($result);
?>