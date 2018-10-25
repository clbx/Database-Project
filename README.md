# CS309-Project
Project for CS309 Database Systems

An all in one database for storing courses, grades, faculty/staff, and student information

## Databases
### Courses

| Course ID | Department | Course Code | Course Extra | Name of Class | Instructor FName | Instructor LName | Status  | Open Seats | Total Seats | Days Offered | Time Offered | Building | Room | Credits | PreRequisets | CoRequsiets|
|-----------|------------|-------------|--------------|---------------|------------------|------------------|---------|------------|-------------|--------------|--------------|----------|------|---------|--------|--------|
| int       | varchar    | int         | varchar      | varchar       | varchar          | varchar          | varchar | int        | int         | varchar      | varchar      | varchar  | int  | int     | varchar | varchar |

\* May be `int` depending on significance of excess

\** May be some kind of date format assuming it can work correctly

## Why Ours is Better
find out next week on "**This class is a waste of time.**"

## Business Rules
* Filled Seats cannot excede Open Seats
* Student's Cannot excede X amount of credits
* Full Time Students must have 12 credits
* Each Students has to have at least 1 advisor
* Each class name must be unique
* Students must have completed the prerequistets, and take the corequisets
