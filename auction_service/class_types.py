
class Item_base(object):
    def __init__(self, key, name):
        self.key_ = key
        self.name_ = name
    def serialize(self):
        return{
            'key': self.key_,
            'name': self.name_,
        }

class Acknowledgement(object):
    def __init__(self, success):
        self.success_ = success
    def serialize(self):
        return{
            'success':self.success_
        }

class Endpoint(object):
    def __init__(self, domain, ip, port):
        self.domain_ = domain
        self.ip_ = ip
        self.port_ = port
    def get_prefix(self):
        return self.ip_+":"+str(self.port_)+"/" # e.g. http://127.0.0.1:5000/
