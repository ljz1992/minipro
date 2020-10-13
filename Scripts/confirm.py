from Api.home import HomeApi
from Api.api_factory import ApiFactory
# 实例化homeApi

ha = HomeApi()

# 调用轮播图api
# print("轮播图:{}".format(ApiFactory.get_home_api().banner_api().json()))
#
# print("主题:{}".format(ApiFactory.get_home_api().theme_api().json()))
#
# print(f"最近新品:{ApiFactory.get_home_api().recent_product_api().json()}")

# print("分类:{}".format(ApiFactory.get_product_api().product_classify_api().json()))
# print("分类下商品:{}".format(ApiFactory.get_product_api().classify_product_api().json()))
# print("商品信息:{}".format(ApiFactory.get_product_api().product_detail_api().json()))

print("返回值:{}".format(ApiFactory.get_user_api().get_token_api().json()))

print("查看订单:{}".format(ApiFactory.get_order_api().order_list_api().json()))

print("创建订单:{}".format(ApiFactory.get_order_api().create_order_api(8, 1).json()))

print("查看订单:{}".format(ApiFactory.get_order_api().query_order_api(50).json()))
