import logging

from Api.api_factory import ApiFactory
import utils


class TestOrder:

    def test_order_list(self):
        res = ApiFactory.get_order_api().order_list_api()
        logging.info("请求地址:{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        utils.common_assert_code(res)
        assert res.json().get("current_page") == 1
        assert len(res.json()) > 0
        assert False not in [i in res.text for i in ["id", "order_no", "total_price"]]

    def test_create_order(self, product_id=7, count=3):
        res = ApiFactory.get_order_api().create_order_api(product_id, count)
        logging.info("请求地址:{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        utils.common_assert_code(res)
        assert len(res.json().get("order_no")) > 0 and len(res.json().get("order_id")) > 0

    def test_query_order(self, order_id=115):
        res = ApiFactory.get_order_api().query_order_api(order_id)
        logging.info("请求地址:{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        utils.common_assert_code(res)
        assert res.json().get("id") == order_id
        assert res.json().get("snap_address").get("name") == "刘锦"
