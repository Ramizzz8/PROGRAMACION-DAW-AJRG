<?php
session_start();

// Check if user is logged in
$isLoggedIn = isset($_SESSION['admin_logged_in']) && $_SESSION['admin_logged_in'] === true;

// Handle login
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['login'])) {
    $username = $_POST['username'] ?? '';
    $password = $_POST['password'] ?? '';
    
    // Simple authentication (replace with database query in production)
    if ($username === 'admin' && $password === 'admin123') {
        $_SESSION['admin_logged_in'] = true;
        $_SESSION['admin_username'] = $username;
        header('Location: admin.php');
        exit;
    } else {
        $loginError = 'Invalid credentials';
    }
}

// Handle logout
if (isset($_GET['logout'])) {
    session_destroy();
    header('Location: admin.php');
    exit;
}

?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin Panel</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 20px; background-color: #f5f5f5; }
        .container { max-width: 1000px; margin: 0 auto; }
        .login-form { background: white; padding: 30px; border-radius: 5px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); max-width: 300px; }
        input { display: block; width: 100%; padding: 10px; margin: 10px 0; }
        button { padding: 10px 20px; background-color: #007bff; color: white; border: none; cursor: pointer; }
        .dashboard { background: white; padding: 20px; border-radius: 5px; }
        .error { color: red; margin-bottom: 10px; }
        .header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; }
    </style>
</head>
<body>
    <div class="container">
        <?php if (!$isLoggedIn): ?>
            <div class="login-form">
                <h2>Admin Login</h2>
                <?php if (isset($loginError)): ?>
                    <p class="error"><?php echo htmlspecialchars($loginError); ?></p>
                <?php endif; ?>
                <form method="POST">
                    <input type="text" name="username" placeholder="Usuario" required>
                    <input type="password" name="password" placeholder="Contraseña" required>
                    <button type="submit" name="login">Ingresar</button>
                </form>
            </div>
        <?php else: ?>
            <div class="dashboard">
                <div class="header">
                    <h1>Panel de Administración</h1>
                    <a href="?logout=true" style="color: #007bff; text-decoration: none;">Logout</a>
                </div>
                <p>Bienvenido, <?php echo htmlspecialchars($_SESSION['admin_username']); ?></p>
                <!-- Add your admin content here -->
            </div>
        <?php endif; ?>
    </div>
</body>
</html>