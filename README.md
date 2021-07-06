![TASK](.vscode/header.svg)

# Task-Boilerplate :rocket:

- This is a Flask application that is set up and configured to work with a database and nginx. Write a docker-compose.yaml that will bring all these services up and allow the app to run on port `80`.

- The server side of the task management system was developed using SQLAlchemy & Flask For Creating and configuring a deployable boilerplate.

## Setting up Nginx

- Remove the `default` configuration from `sites-enabled` using `$ rm /etc/nginx/sites-enabled/default`.
- Edit `/etc/nginx/sites-available/Task` using your preferred text editor and add the following to the file:

\*Note: Make sure to replace `YOUR_FULLY_QUALIFIED_DOMAIN_NAME` with your [FQDN](https://en.wikipedia.org/wiki/Fully_qualified_domain_name).

```json
events {}
http {
    server {
        listen 80;
        location / {
            proxy_pass http://app:5000;
        }
    }
}

```

- Enable the Nginx config using `$ ln -s /etc/nginx/sites-available/task-boilerplate /etc/nginx/sites-enabled/task-boilerplate`.
- Restart Nginx using `$ systemctl restart nginx`.
