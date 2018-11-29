from plugin.plugin import http_client

def test_add_sub(http_client):
    """Add subscriptions"""
    response1 = http_client.add_subscriptions('AAPL_SPBXM', 'AAPL', 'equity', 10, request_id =  '1', system_code = '1')
    response2 = http_client.add_subscriptions('GAZP_TQBR', 'GAZP', 'equity', 10, request_id='1', system_code='1')
    response3 = http_client.add_subscriptions('LKOH_TQBR', 'LKOH', 'equity', 10, request_id =  '1', system_code = '1')
    response4 = http_client.add_subscriptions('TCS_SPBXM', 'TCS', 'equity', 10, request_id =  '1', system_code = '1')
    """Check status_code"""
    assert response1.status_code == 200
    assert response2.status_code == 200
    assert response3.status_code == 200
    assert response4.status_code == 200


def test_get_sub_before_delete(http_client):
    """
    Send request for receive the list of subscribers before delete
    """
    response = http_client.get_subscriptions(request_id = '1', system_code = '1')
    print(response.status_code)
    print("before delete:")
    print(response.json())
    data =  response.json()
    visitors = data[0]['id']
    print(visitors)
    assert response.status_code == 200
    return visitors

def test_del_sub(http_client):
    """Delete subscriptions with some id"""
    response = http_client.del_sub(request_id='1', system_code='1', id = test_get_sub_before_delete(http_client))
    print(response.status_code)

def test_get_sub(http_client):

    """Send request for receive the list of subscribers after delete"""
    
    response = http_client.get_subscriptions(request_id = '1', system_code = '1')
    print(response.status_code)
    print("after delete:")
    print(response.json())
    assert response.status_code == 200
