from . import user_input

class recom_menu:
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
    def recommend(self):
        #if user has ordered similar cuisine, then find what they like and recommend
        #else recommend most popular items in the restuarnt
        #We can use two types; 1. experienced 2. popular

        #Placeholder
        output = {
            'recommendedMenus':
                [
                    {
                        'restaurantId':'restid1',
                        'menuId': 'menu1',
                        'name': 'taco',
                        'price': 15,
                        'imageUrl':'None'
                    },
                    {
                        'restaurantId': 'restid2',
                        'menuId': 'menu2',
                        'name': 'burger',
                        'price': 11.5,
                        'imageUrl': 'None'
                    }
                ]
                  }
        return output #Return list of menues
