class User(object):
    def __init__(self, email, password):
        self.email_ = email
        self.password_ = password

    def serialize(self):
        return {
            'email': self.email_,
            'password': self.password_
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