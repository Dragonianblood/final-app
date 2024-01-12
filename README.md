Tuesday, January 2, 2024
Python 3 Final 
Rubric
- For your final, you will submit two links:
• One link will be a repo for your API
• The second link will be for the TTKBootstrap app you built
- The repo for the API should be from the API we built in class which means the 
following things should be present:
• Data persistence through the use of SQLite
• Authentication through the use of JSON Web Tokens
• Routes requiring the validation/authentication of the JWT’s
• The Data models: One for the users table, tasks table and a third model should 
be a custom one you built from previous exercises
• The custom model’s router should also require authentication in order to access 
the routes
- The TTKBootstrap app should meet the following requirements:
• It should require authentication using the requests library
• Each view should be properly built out incorporating all the elements from the 
API by consuming at least one of the routers (either the tasks or the custom 
one you built)
• All elements of the Crud Operations should be represented
- Create) A way to add a new row to the database table
- Read) A way to get all the rows of the table and a way to see details on just 
one
- Update) A way to update a row in the table
- Delete) A way to delete a row in the database
1
