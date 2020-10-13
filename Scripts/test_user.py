import logging

from Api.api_factory import ApiFactory
import app, utils, pytest


@pytest.mark.run(order=0)
class TestUser:
    def test_get_token(self):
        res = ApiFactory.get_user_api().get_token_api()
        logging.info("请求地址:{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        utils.common_assert_code(res)
        assert len(res.json().get("token")) > 0
        app.headers["token"] = res.json().get("token")
        print("app.headers:{}".format(app.headers))

    def test_token_verify(self):
        res = ApiFactory.get_user_api().token_verify_api()
        logging.info("请求地址:{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        utils.common_assert_code(res)
        assert res.json().get("isValid") is True

    def test_user_address(self):
        res = ApiFactory.get_user_api().user_address_api()
        logging.info("请求地址:{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        utils.common_assert_code(res)
        assert False not in [i in res.text for i in ["刘锦", "18756061448", "上海市"]]
