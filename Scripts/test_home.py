import logging

from Api.api_factory import ApiFactory


class TestHome:
    def test_home_api(self):
        res = ApiFactory.get_home_api().banner_api()
        # 日志打印
        logging.info("请求地址:{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        assert res.status_code == 200
        assert res.json().get("id") == 1 and res.json().get("name") == '首页置顶'
        assert len(res.json().get("items")) > 0

    def test_theme_api(self):
        res = ApiFactory.get_home_api().theme_api()
        logging.info("请求地址:{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        assert res.status_code == 200
        assert 'id":1' in res.text and 'id":2' in res.text and 'id":3' in res.text
        assert False not in [i in res.text for i in ["name", "description", "topic_img", "head_img"]]

    def test_recent_product_api(self):
        res = ApiFactory.get_home_api().recent_product_api()
        logging.info("请求地址:{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        assert res.status_code == 200
        assert len(res.json()) > 0
        assert "id" in res.text and "name" in res.text and "price" in res.text
