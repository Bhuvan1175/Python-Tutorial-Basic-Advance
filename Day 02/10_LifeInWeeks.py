'''
Algorithm
1) We have to find the number of days,weeks and months left in our life if we live until 90 years.
2) We have to take the input of age from the user.
3) We have to calculate the number of days,weeks and months left in our life.
4) One year 365 days, 52 weeks, 12 months.
'''
live_Till_Days=90*365
live_Till_Weeks=90*52
live_Till_Months=90*12
Age=int(input("Enter Your Age :"))
Days_Left=live_Till_Days-(Age*365)
Weeks_Left=live_Till_Weeks-(Age*52)
Months_Left=live_Till_Months-(Age*12)
print(f"You Have a {Days_Left} Days , {Weeks_Left} Weeks and {Months_Left} Months Left.")