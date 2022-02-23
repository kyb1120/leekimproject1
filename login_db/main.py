from website import create_app #when you import a __init__.py file, the upper file folder's name can be used to import py file

app = create_app()

if __name__ == '__main__':
    app.run(debug=True) #debug true => allows for modifications in the py files