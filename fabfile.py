from fabric import task
from invoke import Responder
from _credentials import github_password, github_username


def _get_github_auth_responders():
    """
    返回 GitHub 用户名密码自动填充器
    """
    username_responder = Responder(
        pattern="Username for 'https://github.com':",
        response='{}\n'.format(github_username)
    )
    password_responder = Responder(
        pattern="Password for 'https://{}@github.com':".format(github_username),
        response='{}\n'.format(github_password)
    )
    return [username_responder, password_responder]

@task
def deploy(c):
    program_name = "dog_blog"
    # 先停止应用
    c.run(f"~/.local/bin/supervisorctl -c ~/etc/supervisord.conf stop {program_name}")
    # 拉代码
    with c.cd("~/code/dogBlog"):
        cmd = 'git pull'
        responders = _get_github_auth_responders()
        c.run(cmd, watchers=responders)
    # 安装依赖，迁移数据库，收集静态文件
    with c.cd("~/code/dogBlog"):
        c.run("~/.local/bin/pipenv install --deploy --ignore-pipfile")
        c.run("~/.local/bin/pipenv run python manage.py migrate")
        c.run('~/.local/bin/pipenv run python manage.py collectstatic --noinput')
    # 重新启动应用
    c.run(f"~/.local/bin/supervisorctl -c ~/etc/supervisord.conf start {program_name}")

# pipenv run fab -H daigua@149.129.67.128 --prompt-for-login-password -p deploy

