import  requests

def get_user():
    url = "https://www.geeksforgeeks.org/courses?source=google&medium=cpc&device=c&keyword=geeksforgeeks&matchtype=e&campaignid=20039445781&adgroup=147845288105&gad_source=1&gclid=CjwKCAjw4ri0BhAvEiwA8oo6F4oAKweust_o2fCgvxpOrUg5OFcwhBnSSnjpw9Ha0-juLYjg0YaTyBoCcJ0QAvD_BwE"

    response = requests.get(url)

    if response.text == "":
        print( "response :", 'sorry its empty')

    else:
        print("response", response.text)

ob1 = get_user()

