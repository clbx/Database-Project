# CS309-Project
Project for CS309 Database Systems

An all in one database for storing courses, grades, faculty/staff, and student information

## Databases

[database diagram](https://i.imgur.com/am9DGNm.png)
### Courses

| Course ID | Department | Course Code | Course Extra | Name of Class | Instructor FName | Instructor LName | Status  | Open Seats | Total Seats | Days Offered | Time Offered | Building | Room | Credits | PreRequisets | CoRequsiets|
|-----------|------------|-------------|--------------|---------------|------------------|------------------|---------|------------|-------------|--------------|--------------|----------|------|---------|--------|--------|
| int       | varchar    | int         | varchar      | varchar       | varchar          | varchar          | varchar | int        | int         | varchar      | varchar      | varchar  | int  | int     | varchar | varchar |

\* May be `int` depending on significance of excess

\** May be some kind of date format assuming it can work correctly

## Why Ours is Better
Find out next week on "**This class is a waste of time.**"

## Business Rules
* Filled Seats cannot excede Open Seats and cannot be lower than 0 seats.
* Students cannot excede X amount of credits
* Full Time Students must have between 12 and 16 credits.
* Students are allowed up to 20 credits total, but will be charged an overload fee for all credits over 16.
* Each Students has to have at least 1 advisor, and may have multiple advisors if they have multiple majors.
* Each class course code must be unique, class names may be duplicates if they have multiple offerings.
* Each class must have a professor, classes may have multiple professors (but only 1 will be listed?).
* Students must have completed the prerequistets, and must take the corequisets for a course.
* Class times must not overlap (but a student can make special arrangements to complete a lab on their own time).
