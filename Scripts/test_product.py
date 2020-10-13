import logging

from Api.api_factory import ApiFactory


class TestProduct:
    def test_product_classify_api(self):
        res = ApiFactory.get_product_api().product_classify_api()
        logging.info("请求地址:{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        assert res.status_code == 200
        assert False not in [i in res.text for i in ["id", "name", "description"]]

    def test_classify_product_api(self):
        res = ApiFactory.get_product_api().classify_product_api()
        logging.info("请求地址:{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        assert res.status_code == 200
        assert len(res.json()) > 0

    def test_product_detail_api(self):
        res = ApiFactory.get_product_api().product_detail_api()
        logging.info("请求地址:{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        assert res.status_code == 200
        assert False not in [i in res.text for i in ["id", "name", "price"]]
        assert res.json().get("id") == 2
        assert res.json().get("price") == '0.01'
