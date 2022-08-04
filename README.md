# God of Avalon Backend

## Project config

Copy `/projectRoot/goa_backend/config-sample.py` to `/projectRoot/goa_backend/config.py`. Edit `/projectRoot/goa_backend/config.py` according to the instructions in `config.py`

## Project setup

After cloning, use:

```bash
pip install -r requirements.txt
```

to install all requirements.

Use:

```bash
python manage.py migrate
```

to migrate database.

Use:

```bash
python manage.py runserver
```

to start server.

To deploy, checkout [this post](https://zijunhz.github.io/2022/04/27/How-to-Deploy-Django/).
