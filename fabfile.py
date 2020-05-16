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
    c.run(f"~/.local/bin/supervisorctl -c ~/etc/supervisor/supervisord.conf stop {program_name}")

    # 拉代码
    with c.cd("~/code/dogBlog"):
        cmd = 'git pull'
        responders = _get_github_auth_responders()
        c.run(cmd, watchers=responders)
    # 构建镜像
    with c.cd("~/code/dogBlog"):
        c.run('docker-compose -f production.yml build')
        c.run(f"~/.local/bin/supervisorctl -c ~/etc/supervisor/supervisord.conf start {program_name}")
    # 删除为none的镜像
    c.run("docker images | grep none | awk '{print $3}' | xargs docker rmi")

# fab -H daigua@149.129.67.128 --prompt-for-login-password -p deploy


def _get_certbot_responders():
    enter_email = Responder(
        pattern="Enter email address (used for urgent renewal and security notices) (Enter 'c' to cancel):",
        response="1032939141@qq.com\n"
    )
    agree_policy = Responder(
        pattern="(A)gree/(C)ancel:",
        response="A\n"
    )
    share_email_address = Responder(
        pattern="(Y)es/(N)o:",
        response="Y\n"
    )
    select_server = Responder(
        pattern="blank to select all options shown (Enter 'c' to cancel):",
        response="1\n"
    )
    select_redirect = Responder(
        pattern="Select the appropriate number [1-2] then [enter] (press 'c' to cancel):",
        response="2\n"
    )
    return [enter_email, agree_policy, share_email_address, select_server, select_redirect]

@task
def autossl(c):
    with c.cd("~"):
        c.run("docker exec -it dog_blog_nginx certbot --nginx", watchers=_get_certbot_responders())
# fab -H daigua@149.129.67.128 --prompt-for-login-password -p autossl