<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">

</head>
<body>
  <h1>✅ Task Management App with Django and restapi</h1>
  <p>This project is built using the <strong>Django</strong> framework and is fully containerized with <strong>Docker</strong>. It includes user authentication, task creation/editing, and a RESTful API for superuser-level control.</p>
    <h2>🚀 Setup Instructions</h2>
  <ol>
    <li>Clone repo: <code>git clone https://github.com/Amin-Bajelan/To_Do_App_Django_CBV</code></li>
    <li>Install packages: <code>pip install -r requirements.txt</code></li>
    <li>Run migrations: <code>python manage.py migrate</code></li>
    <li>Start server: <code>python manage.py runserver</code></li>
    <h3>And for docker up</h3>
    <li>build docker: <code>docker-compose build</code></li>
    <li>run container: <code>docker-compose up -d</code></li>
    <li>migrate: <code>docker-compose exec backend python manage.py migrate</code></li>
  </ol>

  <h2>🔧 App Structure</h2>
  <ul>
    <li><strong>accounts</strong>: Handles custom user model and profile creation</li>
    <li><strong>task</strong>: Manages task-related operations</li>
  </ul>

  <h2>🔐 Authentication</h2>
  <ul>
    <li>Custom user model with email login</li>
    <li>User profile automatically created via signals</li>
    <li>Only authenticated users can manage tasks</li>
  </ul>

  <h2>📋 Task Features</h2>
  <ul>
    <li>Create, edit, and view tasks</li>
    <li>Task includes last edit timestamp</li>
  </ul>

  <h2>⚙️ API for Superusers</h2>
  <ul>
    <li>documentation api <strong>Swagger</strong></li> 
    <li>Access all tasks across the system</li>
    <li>Add or delete tasks for any user</li>
    <li>Apply filters to task queries</li>
  </ul>

  <h2>🐳 Docker Support</h2>
  <ul>
    <li>Project includes <code>Dockerfile</code> and <code>docker-compose.yml</code></li>
    <li>Easy containerization for local development or production deployment</li>
    <li>Services include Django backend and PostgreSQL (or other DB of choice)</li>
  </ul>


  <h2>👨‍💻 Developer</h2>
  <p>Created by <strong>Amin</strong></p>
</body>
</html>
