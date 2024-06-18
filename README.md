# Yummy Sweet Restaurant CLI App

This project is for users who are able to browser menu and book a table with CRUD operations, such as `View bookings`, `Add a booking`, `Search a booking`, `Update a booking` and `Cancel a booking`

## Technical use

I develop an application use skills below:

```console

- Python 
- SQL
- SQLAlchemy
- SQLite
- Migration with Alembic
```

***

## Getting Started

- First of all, you need to install dependency

```
pipenv install
```

- Run the application, you need to start a main entry point. You will see some of questions to ask you to do next step

```
python3 main.py 
```

***


## User Workflow

```
Welcome Screen
	- View booking details
		- Please input your booking email
			- Check user's email whether exist
				- YES
					- Show the booking results including name, time and restaurant
						- Make a new booking
						- Update a booking
						- Delete a booking
						- Exit current page
					- Go back to main page
				- NO
					- Ask to re-try email again
					- Go back to main page
	- Exit & Close application
	- Make a new booking?
	    - Grab a list of restuarants from database and show
		- Ask which restaurants are you going to book?
			- Select the restaurant
			- Find the user whether exist by eamil? or Create a new user
			- YES
				- Using the user to make a new booking 
	          	- Input your name, phone number and note
	         	- Return to main page
	    	- NO
				- Create a new member
				- Ask to Input Time & Date & name & phone number & note
	    		- Show the result 
	      		- Return to main page
		- Update a booking
			- Search a certain user by email
			- Check the user whether exist 
				- YES
					- Show all of booking details
					- Let a user select which booking that need to update
					- Update the booking details(name, time, date)
					- Return to main page
				- NO
					- Ask to re-try email again
					- Go back to main page
	 	- Delete a booking
	  		- Ask to input user e-mail
				- YES
	   				- Show booking result
	    			- Chose to confirm which user want to delete
	      			- DELETE the booking
				- No
					- Ask to re-try email again
	       			- Exit & go back to main page
	 - Exit & close
```

***

## Learning Resources

- [Faker](https://pypi.org/project/Faker/0.7.4/)
- [Create a repo- GitHub Docs](https://docs.github.com/en/get-started/quickstart/create-a-repo)
- [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)
