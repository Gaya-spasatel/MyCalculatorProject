<html>
<head>
    <title>Calculator client page</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="style.css"/>
</head>
<body>
    <h2>Calculator client page</h2>
    <div>
    <h3>Process operands</h3>
    <?php
    $operations = array(
        '+' => 'add',
        '-' => 'sub',
        '*' => 'mul',
        '/' => 'div'
    );
    if (isset($_POST['first']) && isset($_POST['second']) && isset($_POST['operation'])){
        $payload = json_encode( array( "firstOperand"=> array("value"=>(int)$_POST['first']), "secondOperand"=> array("value"=>(int)$_POST['second'])));
        $myCurl = curl_init();
    curl_setopt_array($myCurl, array(
        CURLOPT_URL => 'http://calculatorwebserver/api/'.$operations[$_POST['operation']],
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_HEADER => false,
        CURLOPT_POST => true,
        CURLOPT_POSTFIELDS => $payload,
        CURLOPT_HTTPHEADER => array('Content-Type:application/json'),
    ));
    $response = curl_exec($myCurl);
    $info = curl_getinfo($myCurl);
    curl_close($myCurl);
    
    $result = json_decode($response, true);
    $result_of_operation = NULL;
    if ($info["http_code"] == 200) {
        
        switch($_POST['operation']) {
            case '+':
                $result_of_operation = $result["sum"]["value"];
                break;
            case '-':
                $result_of_operation = $result["difference"]["value"];
                break;
            case '*':
                $result_of_operation = $result["product"]["value"];
                break;
            case '/':
                $result_of_operation = (string)$result["quotient"]["value"]." and ".(string)$result["remainder"]["value"];
                break;
        }
    } else if ($info["http_code"] == 400 || $info["http_code"] == 406){
        $result_of_operation = $result["message"];
    } 
    ?>
    <p>First operand: <?php echo $_POST['first'];?></p>
    <p>Second operand: <?php echo $_POST['second'];?></p>
    <p>Operation: <?php echo $_POST['operation'];?></p>
    <p>Result: <?php echo $result_of_operation;?></p>
    <?php
    }
    ?>
    </div>
    <div>
    <h3>Calculator</h3>
    <form action="index.php" method="post">
    <p><label for="first_operand">First operand </label>
    <input type="number" name="first" id="first" required></p>

    <p><label for="operation">Operation </label>
    <select name="operation" id="operation">
    <option disabled>Choose operation</option>
    <option value="+">Addition</option>
    <option value="-">Subsctraction</option>
    <option value="*">Multiplication</option>
    <option value="/">Division</option>
    </select>
    </p>

    <p><label for="second_operand">Second operand </label>
    <input type="number" name="second" id="second" required></p>

    <input type="submit" value="Count" >
    </form>
</div>
</body>
</html>
