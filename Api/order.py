import logging

import app, requests


class OrderApi:
    def __init__(self):
        self.order_list_url = app.base_url + "/order/by_user"
        self.create_order_url = app.base_url + "/order"
        self.query_order_url = app.base_url + "/order/{}"

    def order_list_api(self, page=1):
        logging.info("订单-获取订单列表")
        data = {"page": page}
        logging.info("请求参数:{}".format(data))
        return requests.get(self.order_list_url, params=data, headers=app.headers)

    def create_order_api(self, product_id, count):
        logging.info("订单-创建订单")
        data = {"products": [{"product_id": product_id, "count": count}]}
        logging.info("请求参数:{}".format(data))
        return requests.post(self.create_order_url, json=data, headers=app.headers)

    def query_order_api(self, order_id):
        logging.info("订单-查看订单")
        return requests.get(self.query_order_url.format(order_id), headers=app.headers)
