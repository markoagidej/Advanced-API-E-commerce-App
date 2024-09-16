This app is a fully fuctional API.

to install all requirements, enter the following command into you terminal:
pip install -r requirements.txt

Using a program like Postman, you will be able to interact with a local database on your machine to see how it works.

Remember to first login! All enpoints require a token, and any involving Custoemrs or CustomerAccounts require an Admin.

After running the app, if you put in your local address followed by "/api/docs", you will be able to review the documentation to see the structure, syntax, and formats of HTTP requests and responses.

To run the tests, enter the following command into your terminal:
python -m unittest discover tests