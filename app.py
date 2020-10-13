import logging.handlers
import os


def log_conf():
    # 日志文件位置
    logPath = "./log"
    # 日志器
    logger = logging.getLogger()
    # 日志级别
    logger.setLevel(logging.INFO)
    # 处理器 - 控制台
    sh = logging.StreamHandler()
    # 处理器 - 文件
    file_path = logPath + os.sep + "mini.log"
    fh = logging.handlers.TimedRotatingFileHandler(file_path, when="midnight",
                                                   interval=1, backupCount=7, encoding="utf-8")
    # 格式化字符串
    fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
    # 格式化器
    formatter = logging.Formatter(fmt)
    # 处理器添加格式化器
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)

    # 日志器添加处理器
    logger.addHandler(sh)
    logger.addHandler(fh)


# 请求通用接口地址
base_url = "http://e.cn/api/v1"

# 微信code
code = "001bG40005QdsK11Lp300H2PS82bG40Z"

# 请求头
headers = {
    "Content-Type": "application/json",
    "token": "118a95906aa8355a8176647c21c8b273"
}
