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

# Required Endpoints
1. /api/users - * any one can create account using username, email, and password - this hass been implemented and its working.
2. /api/users/users/me/ - **Displays username and email of the user with a valid token
