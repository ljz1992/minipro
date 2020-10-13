def common_assert_code(res, code=200):
    assert res.status_code == code
