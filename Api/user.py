import logging

import requests, app


class UserApi:
    def __init__(self):
        self.get_token_url = app.base_url + "/token/user"
        self.token_verify_url = app.base_url + "/token/verify"
        # 用户地址
        self.user_addr_url = app.base_url + "/address"

    def get_token_api(self):
        logging.info("用户——获取token")
        data = {"code": app.code}
        logging.info("请求参数:{}".format(data))
        return requests.post(self.get_token_url, headers=app.headers, json=data)

    def token_verify_api(self):
        logging.info("用户——验证token")
        data = {"token": app.headers.get("token")}
        logging.info("请求参数:{}".format(data))
        return requests.post(self.token_verify_url, headers=app.headers, json=data)

    def user_address_api(self):
        logging.info("用户——获取地址信息")
        return requests.get(self.user_addr_url, headers=app.headers)