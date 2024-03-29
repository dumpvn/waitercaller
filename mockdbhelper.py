
MOCK_USERS = [{
    'email': 'test@example.com',
    'salt': '8Fb23mMNHD5Zb8pr2qWA3PE9bH0=',
    'hashed': '1736f83698df3f8153c1fbd6ce2840f8aace4f200771a46672635374073cc876cf0aa6a31f780e576578f791b5555b50df46303f0c3a7f2d21f91aa1429ac22e',
}]

class MockDBHelper(object):
    """docstring for MockDBHelper"""
    def __init__(self, arg):
        super(MockDBHelper, self).__init__()
        self.arg = arg
    
    def get_user(self, email):
        user = [x for x in MOCK_USERS if x.get("email") == email]
        if user:
            return user[0]
        return None
