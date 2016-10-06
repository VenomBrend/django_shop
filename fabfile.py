from fabric.api import run, local, env, settings, lcd, task, puts
from fabric.contrib.files import exists
from fabric.context_managers import cd, settings

# CHANGEME:
WSGI_USER = 'sashadubovyk_pythonanywhere_com'
ARCH = "Cats Shop-0.1.linux-x86_64.tar.gz"
VENV_DIR = '/home/sashadubovyk/.virtualenvs/myvirtualenv35/'
PYTHON_BIN = "python3.5"
STATIC_ROOT = ''


def source_targz(archive):
    local("tar -zxvf  %s" % archive)


def virtualenv(venv_dir):
    """
    Context manager that establishes a virtualenv to use.
    """
    return settings(venv=venv_dir)


def run_venv(command, **kwargs):
    """
    Runs a command in a virtualenv (which has been specified using
    the virtualenv context manager
    """
    local("source %s/bin/activate" % env.venv + " && " + command, **kwargs)


def install_dependencies():
    ensure_virtualenv()
    with virtualenv(VENV_DIR):
        run_venv("python  setup.py install")


def ensure_virtualenv():
    if exists(VENV_DIR):
        return
    local("workon myvirtualenv35  --python=%s" % PYTHON_BIN)


@task
def webserver_restart():
    """
    Restarts the webserver that is running the Django instance
    """
    local("touch /var/www/ %s_wsgi.py " % WSGI_USER)


def build_static():
    with virtualenv(VENV_DIR):
        run_venv("python manage.py collectstatic -v 0 --noinput --clear")
    run("chmod -R ugo+r %s" % STATIC_ROOT)


def update_database():
    with virtualenv(VENV_DIR):
        run_venv("python manage.py migrate --noinput")


def test():
    pass


def create_superuser():
    local("python manage.py  createsuperuser")
 # local('echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'pass')" | ./manage.py shell')




@task
def install_app():
    """
    Deploy project.
    """
    source_targz(ARCH)
    install_dependencies()
    update_database()
    build_static()
    webserver_restart()
    test()
    create_superuser()
    puts("Don't worry, be happy!")


@task
def prepare():
    local("python setup.py sdist")
