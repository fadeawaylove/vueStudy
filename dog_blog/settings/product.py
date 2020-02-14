import time
from .common import *

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
DEBUG = False
ALLOWED_HOSTS = ['dog.fadeaway.ltd']


# django的日志配置
log_path = os.path.join(BASE_DIR, 'logs')
if not os.path.exists(log_path):
    os.makedirs(log_path, exist_ok=True)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        # 日志格式
        'standard': {
            'format': '[%(asctime)s] [%(filename)s:%(lineno)d] [%(module)s:%(funcName)s] '
                      '[%(levelname)s]- %(message)s'},
        'simple': {  # 简单格式
            'format': '%(levelname)s %(message)s'
        },
    },
    # 过滤
    'filters': {
    },
    # 定义具体处理日志的方式
    'handlers': {
        # 默认记录所有日志
        'default': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(log_path, 'all-{}.log'.format(time.strftime('%Y-%m-%d'))),
            'maxBytes': 1024 * 1024 * 5,  # 文件大小
            'backupCount': 5,  # 备份数
            'formatter': 'standard',  # 输出格式
            'encoding': 'utf-8',  # 设置默认编码，否则打印出来汉字乱码
        },
        # 输出错误日志
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(log_path, 'error-{}.log'.format(time.strftime('%Y-%m-%d'))),
            'maxBytes': 1024 * 1024 * 5,  # 文件大小
            'backupCount': 5,  # 备份数
            'formatter': 'standard',  # 输出格式
            'encoding': 'utf-8',  # 设置默认编码
        },
        # 控制台输出
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        # 输出info日志
        'info': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(log_path, 'info-{}.log'.format(time.strftime('%Y-%m-%d'))),
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'standard',
            'encoding': 'utf-8',  # 设置默认编码
        },
    },
    # 配置用哪几种 handlers 来处理日志
    'loggers': {
        # 类型 为 django 处理所有类型的日志， 默认调用
        'django': {
            'handlers': ['default', 'console'],
            'level': 'INFO',
            'propagate': False
        },
        # log 调用时需要当作参数传入
        'log': {
            'handlers': ['error', 'info', 'console', 'default'],
            'level': 'INFO',
            'propagate': True
        },
    }
}




# LOGGING = {
# 'version':1,
# 'disable_existing_loggers': False,
# 'loggers':{
#     "gunicorn.error": {
#         "level": "DEBUG",# 打日志的等级可以换的，下面的同理
#         "handlers": ["error_file"], # 对应下面的键
#         "propagate": 1,
#         "qualname": "gunicorn.error"
#     },
#
#     "gunicorn.access": {
#         "level": "DEBUG",
#         "handlers": ["access_file"],
#         "propagate": 0,
#         "qualname": "gunicorn.access"
#     },
# },
# 'handlers':{
#     "error_file": {
#         "class": "logging.handlers.RotatingFileHandler",
#         "maxBytes": 1024*1024*1024,# 打日志的大小，我这种写法是1个G
#         "backupCount": 1,# 备份多少份，经过测试，最少也要写1，不然控制不住大小
#         "formatter": "generic",# 对应下面的键
#         # 'mode': 'w+',
#         "filename": os.path.join(BASE_DIR, "error.log")# 打日志的路径
#     },
#     "access_file": {
#         "class": "logging.handlers.RotatingFileHandler",
#         "maxBytes": 1024*1024*1024,
#         "backupCount": 1,
#         "formatter": "access",
#         "filename": os.path.join(BASE_DIR, "access.log"),
#     }
# },
# 'formatters':{
#     "generic": {
#         "format": "'[%(process)d] [%(asctime)s] %(levelname)s [%(filename)s:%(lineno)s] %(message)s'", # 打日志的格式
#         "datefmt": "[%Y-%m-%d %H:%M:%S %z]",# 时间显示方法
#         "class": "logging.Formatter"
#     },
#     "access": {
#         "format": "'[%(process)d] [%(asctime)s] %(levelname)s [%(filename)s:%(lineno)s] %(message)s'",
#         "class": "logging.Formatter"
#     }
# }
# }