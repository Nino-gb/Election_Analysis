# Election Analysis

## Overview of Election Audit:

Colorado Board election tasked some employees to create a report for Colorado Election results. This report must include Total Votes, Total votes for each candidate with the percentages and the winner.The Team will be using command line to update GitHub repository, access to local files and folder, and write and run Python programming scripts. Writing algorithms in Python will allow to confirm and analyze the election results. To help with this task the team will also use Visual Studio Code (VS Code) to run Python to edit and save the script while performing the election audit.


### Purpose

Election commission have requested additional data that need to include voter turnout for each county, percentage of votes from each county out of the total count, and the county highest turnout. In order to complete the new task the team must do some modification to the original script without breaking the original codes in VS Code. Election Team new codes need to initialize a county list, county dictionary, empty string and variables. Github repository hold the original script in case the team need to access to the old version spript.

## Election Audit

![Screen Shot 2022-08-31 at 8 55 04 AM](https://user-images.githubusercontent.com/110786136/187740913-b221eb15-6c0c-4c83-9c5d-8c9fe7930719.png)

- 369,711 votes were cast during the Congressional Election

- County Votes breakdown number of votes and percentages

	Denver with 82.8% (306,055 votes)

	Jefferson with 10.5% (38,855 votes)
	
	Arapahoe with 6.7% (24,801 votes)

- Denver county had the largest number of votes

- Total Votes by Candidates breakdown nuber of votes and percentages

	Diana DeGette with 73.8% (272,892 votes

	Charles Casper Stockham with 23.0% (85,213 votes)
	
	Raymon Anthony Doane with 3.1% (11,606 votes)

- Diana DeGette won the Congress Election with 272,892 and 73.8% of the counties votes.


## Election-Audit Summary:

This report present our script proposal for future election audits. Our Script proposal created in VS Code give room to write, execute , saves and edit existing script making possible to adapt the codes into new data. VS Code give us the flexibility to access files and folder through paths. That allow us to change, open and read future election data which provide a way for the program to work with any election results csv file and run it through our script to get new audit elections results analysis in less than a minutes. Furthermore , script customization can be execute upon Board Election request. Customization may include the analysis of the victory margin and candidate total votes by county.


> *Codes in`if` statement get the candidate name from election result candidate row[2], add candidate name to the candidate list, track candidate'voter count and add a vote to the candidate' count.*
> ![Screen Shot 2022-08-31 at 1 26 36 PM](https://user-images.githubusercontent.com/110786136/187752305-37592aaf-7fa7-46c5-b801-fe728c9887b1.png)

> *A `for` loop was created to retrieve vote count and percentage by candidate. 
`if` statement was created to determinate winning vote count, percentage and candidate.*
![Screen Shot 2022-08-31 at 1 19 28 PM](https://user-images.githubusercontent.com/110786136/187751023-cc6e17bb-e0a8-4ede-a4f2-f522c9279400.png)

> *Codes in `if` statement get the county name from election result county row[1], add county name to the county list, track county'voter count and add a vote to the county' count.*
![Screen Shot 2022-08-31 at 1 30 58 PM](https://user-images.githubusercontent.com/110786136/187753114-29144a5a-6a59-428f-a306-bef59b949512.png)


> *A `for` loop was created to retrieve vote count and percentage by county. 
`if` statement was created to determinate the largest county votes and percentages.*

![Screen Shot 2022-08-31 at 1 31 36 PM](https://user-images.githubusercontent.com/110786136/187753211-daaf28cc-21ed-4d76-a1e3-d60466193ff7.png)
