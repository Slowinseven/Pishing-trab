<?php
// Configuração da conexão
$servername = "localhost";
$username = "seu_usuario";
$password = "sua_senha";
$dbname = "seu_banco";

// Conectar ao banco
$conn = new mysqli($servername, $username, $password, $dbname);

// Verificar conexão
if ($conn->connect_error) {
    die("Conexão falhou: " . $conn->connect_error);
}

// Obter o e-mail do formulário
$email = $_POST['email'];

// Inserir no banco de dados
$sql = "INSERT INTO usuarios (email) VALUES (?)";
$stmt = $conn->prepare($sql);
$stmt->bind_param("s", $email);

if ($stmt->execute()) {
    echo "Dados estão ok";
} else {
    echo "Erro ao salvar: " . $stmt->error;
}

$stmt->close();
$conn->close();
?>
