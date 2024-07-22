def _distc_task():
    watch_details={
        'Title':12345,
        'omega':12345678,
        'rolex':987652123,
        'Title':120000
    }
    print(len(watch_details))
    print(type(watch_details))
    print(watch_details['Title'])
# _distc_task()


def exampel_dict():
    watch_details = {
        'Title':120000,
        'omega':12345678,
        'rolex':987652123,
        'saiko':120000
    }
    print(len(watch_details))
    print(type(watch_details))
    print(watch_details['Title'])
    print(watch_details['omega'])
    print(watch_details['rolex'])
    print(watch_details['saiko'])
# exampel_dict()

def mutble_test():
    watch_details = {
            'Title':120000,
            'omega':12345678,
            'rolex':987652123,
            'saiko':120000
        }
    watch_details['saiko'] = 123456789
    print(watch_details['saiko'])
    watch_details['bugati'] = 97654321
    print(watch_details)
# mutble_test()

def food_list():
    food_menu = {
        'biriyani':300,
        'vadai': 100,
        'ice_cream':400
    }
    print(food_menu)
    food_menu['biriyani']= 10000
    print(food_menu['biriyani'])
    print(food_menu)
    food_menu['mandi'] = 9000
    print(food_menu)
# food_list()

def _nested_dicts():
    user = {
    'basil ahamed':{
        'name':"basil",
        "age":21,
        'location':"chennai"
    },
    'basilahamed':{
        'name':"ahamed",
        "age":22,
        'location':"usa"
    },
    'ahamedbasil':{
        'name':"ahamed basils",
        "age":20,
        'location':"canada"
    }            
}
    keys = user.keys()
    values = user.values()
    print("using for loop")
    for trash in keys:
        print(f'{trash}: {user[trash]}')
        print(user[trash]['name'],user[trash]['location'])
        
    print(user['basil ahamed']['name'],user['basil ahamed']['location'])
# _nested_dicts()   
  
def _method_dicts():
    pass