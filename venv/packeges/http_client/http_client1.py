""""Module with fixtures for Investment API"""
import requests
import json

class HttpClient(object):
    """"Class to work with HTTP requests"""

    def __init__(self):
        """"Inatalisation variable"""
        self.base_url = "https://fintech-trading-qa.tinkoff.ru/v1/md/"
        self.headers = {'Authorization': 'Basic ZmludGVjaDoxcTJ3M2Uh'}

    def get_subscriptions(self, request_id, system_code):
        """
        Send request for receive the list of subscribers before delete
        """
        url = self.base_url + "contacts/n.kohno/subscriptions?request_id=" + request_id + "&system_code=" + system_code
        response = requests.get(url, headers = self.headers)
        return response

    def add_subscriptions(self, instrument_id, sec_name,sec_type, price, request_id, system_code):
        """
        Add subscriptions
        """
        url = self.base_url + "contacts/n.kohno/subscriptions?request_id=" + request_id + "&system_code=" + system_code
        header = {'Authorization': 'Basic ZmludGVjaDoxcTJ3M2Uh', 'Content-Type': 'application/json'}
        body = {"instrument_id": instrument_id, "sec_name": sec_name, "sec_type": sec_type, "price_alert": price}
        response = requests.post(url, json = body, headers = header)
        return response

    def del_sub(self, request_id, system_code, id):
        """
        Delete subscriptions with some id
        """
        url = self.base_url + "contacts/n.kohno/subscriptions/"+ id +"?request_id=" + request_id + "&system_code=" + system_code
        response = requests.delete(url, headers=self.headers)
        return response
