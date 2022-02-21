import webbrowser

def try_me():
    name = input("Enter your first name: ")
    name = name.strip()
    webbrowser.open(f'https://www.behindthename.com/name/{name}')
    return 'Interesting name!!!'