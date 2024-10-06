from . import user_input

class save_restaurant:
    '''
    This class saves user's favorite restaurants into logging table and service table
    '''
    def __init__(
            self,
            user_rest_input: dict = user_input,
            db_con = None
    ):
        self.userId = user_rest_input['userId']
        self.restaurantId = user_rest_input['restaurantId']
        self.db_con = db_con
    def process_db(self):
        #process dictionary/json to db
        return None
    def save_logging(self,con=None):
        #code for save to logging db
        return None

    def save_restaurant(self,con=None):
        import datetime
        self.userId
        self.restaurantId
        createdOn = datetime.datetime.now()
        #connect to db
        return None