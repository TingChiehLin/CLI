# Yummy Sweet Restaurant CLI App

This project is for users who are able to browser menu and book a table with CRUD operations, such as `Add a booking`, `Search a booking`, `Update a booking` and `Cancel a booking`

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
- Initial Options
	- View restaurant menu
	 - Go back to input your email again
	- View booking details
	 	- Please input your email
	 	 - Correct?
	 	  - YES
		 	  - Show the booking result
		 	  - Exit?
			 	  - YES
			 	   - Go back to main page
	 	  - NO
	 	   - go back to input your email again
	- Make a new booking?
		 - Ask whether it is existing user or not 
		  - if existing user, please Input your email
	        - Show the user booking result
	        - and Ask whether need to book a new?
	         - YES
	          - Input your name, phone number and note
	          - Return to main page
	      - NO
	      - Sign up a new member and ask to book
	      - Input Time & Date & name & phone number & note
	      - Show the result 
	      - Return to main page
	 - Delete a booking
	  - Ask to input user e-mail to confirm
	   - Show booking result
	    - Chose to confirm which users want to delete
	     - YES
	      - DELETE the booking
	       - Exit & go back to main page
	 - Exit & close
```

***

## Learning Resources

- [Click API](https://pypi.org/project/click/)
- [Create a repo- GitHub Docs](https://docs.github.com/en/get-started/quickstart/create-a-repo)
- [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)
