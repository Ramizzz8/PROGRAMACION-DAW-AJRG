<?php
session_start();

/**
 * ----------------------------------------------------
 * Language handling
 * ----------------------------------------------------
 */
$defaultLang = 'es';

if (!isset($_SESSION['idioma'])) {
    $_SESSION['idioma'] = $defaultLang;
}

if (isset($_GET['idioma']) && in_array($_GET['idioma'], ['es', 'en'])) {
    $_SESSION['idioma'] = $_GET['idioma'];
}

$lang = $_SESSION['idioma'];

/**
 * ----------------------------------------------------
 * Language strings (scalable & clean)
 * ----------------------------------------------------
 */
$idioma = [
    'es' => [
        'inicio'     => 'Inicio',
        'sobremi'    => 'Sobre mí',
        'proyectos'  => 'Proyectos',
        'contacto'   => 'Contacto',
        'rol'        => 'Desarrollador Full Stack',
        'bio'        => 'Apasionado por crear soluciones digitales modernas y eficientes.',
        'stack'      => 'PHP, JavaScript, HTML, CSS, MySQL',
        'proyecto1'  => 'Sistema de Gestión',
        'proyecto2'  => 'Portafolio Web',
        'contactMsg' => 'Disponible para proyectos freelance y colaboraciones.'
    ],
    'en' => [
        'inicio'     => 'Home',
        'sobremi'    => 'About Me',
        'proyectos'  => 'Projects',
        'contacto'   => 'Contact',
        'rol'        => 'Full Stack Developer',
        'bio'        => 'Passionate about building modern and efficient digital solutions.',
        'stack'      => 'PHP, JavaScript, HTML, CSS, MySQL',
        'proyecto1'  => 'Management System',
        'proyecto2'  => 'Web Portfolio',
        'contactMsg' => 'Available for freelance projects and collaborations.'
    ]
];
?>
<!doctype html>
<html lang="<?= $lang ?>">
<head>
    <meta charset="utf-8">
    <title>Andrés Ramírez | Portfolio</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <style>
        :root {
            --primary: #4f46e5;
            --secondary: #6366f1;
            --bg: #f4f6fb;
            --text: #1f2937;
            --muted: #6b7280;
            --card: #ffffff;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: "Segoe UI", system-ui, sans-serif;
            background: var(--bg);
            color: var(--text);
            line-height: 1.6;
        }

        header {
            background: var(--card);
            padding: 24px 40px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 10px 20px rgba(0,0,0,.05);
        }

        header h1 {
            font-size: 24px;
            font-weight: 700;
        }

        select {
            padding: 8px 12px;
            font-size: 15px;
            border-radius: 6px;
            border: 1px solid #ddd;
            cursor: pointer;
            display: flex:
            justify-content: center;
            align-items: center;
            gap: 8px;
        }

        nav {
            display: flex;
            justify-content: center;
            gap: 30px;
            padding: 20px;
        }

        nav a {
            text-decoration: none;
            font-weight: 600;
            color: var(--primary);
        }

        nav a:hover {
            text-decoration: underline;
        }

        main {
            max-width: 1000px;
            margin: 0 auto;
            padding: 40px 20px;
            display: grid;
            gap: 30px;
        }

        section {
            background: var(--card);
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 8px 16px rgba(0,0,0,.05);
        }

        h2 {
            margin-bottom: 12px;
            color: var(--primary);
        }

        .muted {
            color: var(--muted);
        }

        .projects {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 20px;
        }

        .project-card {
            border: 1px solid #eee;
            padding: 20px;
            border-radius: 10px;
        }

        footer {
            text-align: center;
            padding: 30px;
            color: var(--muted);
            font-size: 14px;
        }
    </style>
</head>

<body>

<header>
    
    <h1>Andrés Ramírez</h1>
        <nav>
    <a href="#home"><?= $idioma[$lang]['inicio'] ?></a>
    <a href="#about"><?= $idioma[$lang]['sobremi'] ?></a>
    <a href="#projects"><?= $idioma[$lang]['proyectos'] ?></a>
    <a href="#contact"><?= $idioma[$lang]['contacto'] ?></a>
</nav>
    <select id="langSelector">
        <option value="es" <?= $lang === 'es' ? 'selected' : '' ?>>🇪🇸 Español</option>
        <option value="en" <?= $lang === 'en' ? 'selected' : '' ?>>🇬🇧 English</option>
    </select>



</header>


<main>
    <!-- ABOUT -->
    <section id="about">
        <h2><?= $idioma[$lang]['sobremi'] ?></h2>
        <p class="muted"><?= $idioma[$lang]['rol'] ?></p>
        <p><?= $idioma[$lang]['bio'] ?></p>
        <p><strong>Tech Stack:</strong> <?= $idioma[$lang]['stack'] ?></p>
    </section>

    <!-- PROJECTS (MOCKUP DATA) -->
    <section id="projects">
        <h2><?= $idioma[$lang]['proyectos'] ?></h2>
        <div class="projects">
            <div class="project-card">
                <h3><?= $idioma[$lang]['proyecto1'] ?></h3>
                <p class="muted">PHP · MySQL · Bootstrap</p>
            </div>
            <div class="project-card">
                <h3><?= $idioma[$lang]['proyecto2'] ?></h3>
                <p class="muted">HTML · CSS · JavaScript</p>
            </div>
        </div>
    </section>

    <!-- CONTACT -->
    <section id="contact">
        <h2><?= $idioma[$lang]['contacto'] ?></h2>
        <p><?= $idioma[$lang]['contactMsg'] ?></p>
        <p><strong>Email:</strong> andres@email.com</p>
        <p><strong>LinkedIn:</strong> linkedin.com/in/andresramirez</p>
    </section>
</main>

<footer>
    © <?= date('Y') ?> Andrés Ramírez — Portfolio Mockup
</footer>

<script>
    document.getElementById("langSelector").addEventListener("change", function () {
        window.location = "?idioma=" + this.value;
    });
</script>

</body>
</html>
