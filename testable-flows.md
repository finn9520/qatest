#Testable Workflows

###Possible app states and user actions

1) User loads the page 
- Initial page is loaded with app name in title
- Search Bar is displayed for text entry
- Go Button is displayed to execute a new search
- Results Table is displayed with `No Repos` as the initial value (*)

2) User enters a text into the 
- Text is shown in search bar, but no immediate change

3) User presses enter button while focused in the search bar
- API search of Github is performed looking for the username in the search bar and results returned
- If user is found, the top 30 repositories and descriptions are displayed in a table
- The repository names should be displayed as clickable links to the actual repository
- `Success` is briefly displayed if the search is successful
- `User not found` is displayed if the user is not found with the search
- `Something went wrong` is displayed if another error occurred

4) User clicks the "Go" button (AC)
- The same exact results as action #3 should be expected

5) User can repeat steps 2 and 3 to execute a new search
- Previous results should be replaced with the new results
- The new status of the search should replace the previous status

5) User can click a repository link displayed in the table
- A new browser tab is open and that user's Github repository is loaded

###Considerations

Loading the app:
- Different OS/Browser combinations
- Mobile/Tablet/Web view
- Accessibility options
- Localization

Executing the search:
- Waiting for the search to finish
- Users that have a large number of repositories (30+)
- Users that exist but have no repositories
- Users that have special characters in their project names or descriptions
- Connectivity problems during search
- Stress and performance testing

###Displaying the results:
- Special characters in the names or descriptions
- Extremely long results
- Potential Security or injection attacks

## Not currently considered:
- API: appears to be 100 leveraged from github, we can assume that has been properly tested

## Acceptance Criteria
1.	The UI consists of a header, a search form and a search result section
2.	The header displays the title of the app
3.	The search form accepts a text input as a search term. Search is activated by clicking the "Go" button, or by pressing the "Enter" key
4.	For each repo found, the search result section displays a row with basic info about that repo: name and description. Clicking on the repo name takes the user to the repo's URL. In case of a missing value, `–` is displayed
5.	The user sees feedback about the result of the search action. Either a success or error message are shown above the search field at the completion of a search action, for a short amount of time. If the error is due to a user not found on Github, a specific error message is displayed. Otherwise, a generic error message is displayed

## Testable Workflows

Based on the acceptance criteria as well as the potential user states and actions of the tool, these are the best testable workflows that would cover most of the application in a smoke test:

### Workflow #1 - standard user experience

1) Page is loaded
2) Search is executed
3) Successful result is displayed
4) Second search is executed
5) Successful result is displayed
6) Item in the results list is clicked

Additional items that can be checked in this flow:
- International characters
- Execute search with both ENTER and button press
- Single item in results list

### Workflow #2 - poor user experience
1) Page is loaded
2) Empty search is performed
3) Proper error message is displayed
4) Non-existent user search is performed
5) Proper error message is displayed
6) Search with invalid characters is performed 
7) Proper error message is displayed

Additional items that can be checked in this flow:
- All possible error messages
