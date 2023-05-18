# LittleLemon
 LittleLemon Restaurant API using DRF
 
When you submit your assignment, other learners in the course will review and grade your work. These are the criteria they’ll use to evaluate your APIs.

In this project, my  APIs endpoint need to make it possible for  end-users to perform certain tasks .

1.	The admin can assign users to the manager group

2.	You can access the manager group with an admin token

3.	The admin can add menu items 

4.	The admin can add categories

5.	Managers can log in 

6.	Managers can update the item of the day

7.	Managers can assign users to the delivery crew

8.	Managers can assign orders to the delivery crew

9.	The delivery crew can access orders assigned to them

10.	The delivery crew can update an order as delivered

11.	Customers can register

12.	Customers can log in using their username and password and get access tokens

13.	Customers can browse all categories 

14.	Customers can browse all the menu items at once

15.	Customers can browse menu items by category

16.	Customers can paginate menu items

17.	Customers can sort menu items by price

18.	Customers can add menu items to the cart

19.	Customers can access previously added items in the cart

20.	Customers can place orders

21.	Customers can browse their own orders

##  Required Project Endpoints
** User registration and Token generation endpoints **
1. /api/users - * any one can create account using username, email, and password - this hass been implemented and its working.
  **This has been implemeted and is woking just fine**
2. /api/users/users/me/ - **Displays username and email of the user with a valid token.
  **This has been implemeted and is woking just fine**
3. /token/login/ - * Anyone with a valid username and password can generate a token to be used with other API'calls.
  **This has been implemeted and is woking just fine**

### Menu Item endpoints 
4. /api/menu-items - * in the delivery crew group and customers can view all items using the 'GET' method. all other operations/requests{POST, PUT, PATCH, DELETE} to this end point by delivery crew and customers will be denied.
  **This has been implemeted and is woking just fine**
5. /api/menu-items/{menuItem} - using the GET  method the customer and delivery crew can view a single item. All other calls using {POST, PUT, PATCH, DELETE} to this end point by delivery crew and customers will be denied.
  **This has been implemeted and is woking just fine**
6. /api/menu-items - using the methods below the manager can view and create menu items.
    1. GET, List all mune items
    2. POST, Create a new menu item
  **This has been implemeted and is woking just fine** 
7. /api/menu-items/{menuItem} - using the methods below the manager can
    1. GET, list a single menu item.
    2. PUT,PATCH, update a single menu item.
    3. DELETE,  delete a singl menu item.
  **This has been implemeted and is woking just fine**
### User group management endpoints

8. /api/groups/manager/users -  Using the methods listed below the manager can perform different actions
    1. GET , views all members of the manager user group.
    2. POST, Assigns the a user to the manager group and returns 201-Created

9. /api/groups/manager/users/{userId} - Using the DELETE method the manager can remove a member of the managers user group.
10. /api/groups/delivery-crew/users - Using the methods listed below the manager can  perform different actions
    1. GET, view all memebers of the delivery crew user group.
    2. POST, assign users to delivery crew user group
11. /api/groups/delivery-crew/users/{userId} - using the DELETE method the manager can remove a user from the delivery cred usergroup.






