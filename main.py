from app import create_app

# Create an instance of the app using the factory function in __init__.py
app = create_app()

if __name__ == '__main__':
    # If running this script directly, start the Flask development server
    # 'debug=True' helps during development, showing error messages
    app.run(debug=True)
