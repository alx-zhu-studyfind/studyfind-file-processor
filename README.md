# **Studyfind File-Processor**

### Code by: Alexander Zhu

---

<br />

## **Description**

This file processor was implemented as a part of Studyfind in order to automate the process of downloading csv files from **clinicaltrials.gov**, webscraping for researcher emails, and sending outreach emails from these files.

<br />

---

<br />

## **Files you will have to run:**

- fileProcessor_client 

<br />

---

<br />

## **Files you should have downloaded:**

- fileProcessor_client -- *(client to run these functions)*
- fileProcessor_emailer -- *(function for sending emails)*
- fileProcessor_cloud -- *(processing functions)*
- fileProcessor_globals -- *(for global variables such as folder names, emails, etc.)*
- fileProcessor_drive -- *(for linking to Google Drive)*
- fileProcessor_webscraper -- *(for webscraping of researcher emails)*
- fileProcessor_autofill -- *(for automatic downloading of files from clinicaltrials.gov)*
- credentials.json -- *(to allow use of the Google Console, see the next section for instructions)*

<br />

---

<br />

## **How to Install credentials.json**:

1. Log in to the Business Intelligence email (ask Andrew for login information)
3. Navigate to <a href="https://cloud.google.com/">cloud.google.com</a>
4. Click **Console** on the top right, and ensure you have selected the project titled "Studyfind File Processor"
5. Click the three lines on the top left (next to the Google Cloud logo) to open the sidebar menu if it is not already open.
6. Select **APIs & Services -> Credentials**
7. Click **+ Create Credentials -> OAuth client ID**
8. Set **Application type** as **Desktop App** and name the application with the format **name_desktop**
9. Click **DOWNLOAD JSON** on the pop-up that follows, ensure the file is named **credentials.json**, and in the same directory as the other files of the fileProcessor library.
10. If the credentials.json file needs to be downlaoded again, navigate to the Credentials page, and click the download button of your credentials in the list under **OAuth 2.0 Client IDs**. 

<br />

---

<br />

## **Python Libraries to Install**:
1. Ensure Python and pip are installed on your computer
2. Install a code editor (VSCode is a good one, which is already compatible with Python)
3. **pip install pandas**
4. **pip install selenium**
5. **pip install beautifulsoup4**
6. **pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib**  

<br />

---

<br />

## **To Run the File Processor:**

1. Ensure that all files are downloaded and in the same folder.
2. Make sure that your files are in their **own directory**, as the fileprocessor will be manipulating this folder.
3. Make sure you have your **credentials.json** file also in the same directory (see Google Cloud setup to get this)
4. Make sure **Python** and all other libraries have been installed.
5. Run **python fileProcessor_client** in your terminal, or just run the **fileProcessor_client** in VSCode. 
6. Select the option you want to perform. 

<br />

---

<br />

## *Optional:* **Setting up Google Cloud**:
If you would like to set up a Google Cloud workspace to link to (again, this is optional, only if you would like to link your own Google Drive to the file processor), visit **https://console.cloud.google.com/**. 

1. On the top left, there is a dropdown menu that should say **Select a Project**. Click this drop down, and select **New Project** on the top right of the pop-up. Fill out the information for this project.
2. Click the three lines on the top left (next to the Google Cloud logo) to open the sidebar menu if it is not already open.
3. Select **APIs & Services -> Library**
4. Search for **Google Drive API**, click on the card, and enable the API. The Google Drive API should not be enabled for your project. 
5. Now, go to **APIs & Services -> OAuth consent screen**.
6. Click create (select **Internal User** if prompted) and fill out the form that follows. 
7. After clicking **Save and Continue**, click **Add or Remove Scopes**, and search for the **Google Drive API** scope. It should have the following description: **See, edit, create, and delete all of your Google Drive files.**
8. Save and continue (you do not need to add test users, unless there are other users you would like to allow to use this project). 
9. Now, go to **APIs & Services -> Credentials**.
10. Click **Create Credentials -> OAuth Client ID**. Select **Desktop App** for application type and give it a name.
11. Click **Download JSON** and download the file into the *SAME DIRECTORY* as the file processor. You can access the file again if you need it by clicking the name of the client you created (it is listed in the OAuth 2.0 Client IDs section on the Credentials page). 

<br />

---

<br />

# Function Documentation

<br />

## **fileProcessor_client**

<br />

## *get_menu*  

**Description:**  
Gets the menu text to print in the terminal

**Args:**
None

<br />

## *main*  

**Description:**  
Repeatedly prompts the user to choose from options 1-3 based on the task to complete.

**Args:**
None

<br />

---

<br />

## **fileProcessor_cloud**

<br />

## *process_files*  

**Description:**  
Downloads files from the BASE_FOLDER_NAME folder in Google Drive, processes the files using the function provided. Duplicate rows are removed using the function provided, then the files are split according to the split sizes, and uploaded into the EMAIL_FOLDER_NAME folder on Google Drive. Old files are moved into the 'processed' folder in Google Drive.  
***NOTE**: The function creates folders automatically locally and in Google Drive if they do not exist!*

**Args:**
>processingFn=None 
  - Function used to process csv files, if None, files will just be split according to the following parameters.
>fileType='.csv' 
  - File type of files to be processed (only .csv supported for now)
>splitSizes=[] 
  - Array of split sizes if specific sizes are needed (program splits the file into one file of each size specified)
>defaultSplitSize=1000 
  - Once there are no split sizes remaining, all files are split using this default size
>removeDuplicatesFn=None 
  - Function to remove duplicate rows from a csv file
>processedFolderName='processed' 
  - Name of the folder to store files that have been processed (old files)
>togglePrint=True
  - True to print helpful messages, False to disable printing.
>emails=[]
  - List of emails to share processed files with on Google Drive

<br />

## *send_emails*  

**Description:**  
Downloads *ONE* file from the EMAIL_FOLDER_NAME folder in Google Drive, sends emails from  the files using the function provided. Old files are moved into the 'emailed' folder on Google Drive. 

**Args:**
>from_email
  - Email to send from. MUST BE INCLUDED IN THE EMAIL_DICT in the global variables.
>fileType='.csv' 
  - File type of files to be processed (only .csv supported for now)
>processedFolderName='emailed' 
  - Name of the folder to store files that have been processed (old files)
>togglePrint=True
  - True to print helpful messages, False to disable printing.
>emails=[]
  - List of emails to share processed files with on Google Drive

<br />

## *getDirectoryPath*  

**Description:**  
Gets the path of a folder using the current working directory. 

**Args:**
>baseFolderName
  - The name of the folder in the current working directory
>togglePrint=True
  - True to print helpful messages, False to disable printing.

<br />

## *getDirectoryPath*  

**Description:**  
Gets the path of a folder using the path specified. 

**Args:**
>path
  - The path to look for the folder on
>folderName
  - The name of the folder in the path specified

<br />

## *processFile*  

**Description:**  
Processes a file using a function provided.

**Args:**
>filePath
  - Path of the file to process
>processingFn
  - Function to use to process the file. The function MUST take only the filePath as an argument, and must return the filePath of the processed file.

<br />

## *moveFileToFolder*  

**Description:**  
Moves a file into a specified folder.

**Args:**
>filePath
  - Path of the file to move
>folderPath
  - Path of the destination folder

<br />

## *splitCSV*  

**Description:**  
Splits one file into a several files based on the splitSizes and defaultSize provided.

**Args:**
>creds
  - Google OAuth credentials to interact with the Google Drive API
>filePath
  - Path of the file to split
>parentFolderPath
  - Path of the folder to hold the split files
>parentFolderId
  - Google Drive folder ID of the folder to hold the split files when uploaded
>splitSizes
  - A list of specific split sizes (number of rows) to split files into. If the list is empty, the defaultSize will be used to split the file. If there are still remaining rows after all split sizes have been used, the defaultSize will be used to split the remaining rows of the file.
>defaultSize=None
  - The default split size, used when there are no remaining splitSizes. If defaultSize=None, no splitting will be done, and the remaining rows in the file will be included in one file instead of being split.

<br />

## *studyfind_removeDupEmails_inPlace*  

**Description:**  
Removes rows that contain duplicate emails.

**Args:**
>filePath
  - Path of the file to process

<br />

## *fixFileName*  

**Description:**  
Removes spaces and replaces them with '\_'s. 

**Args:**
>filePath
  - Path of the file to process

<br />

## *clearFolder*  

**Description:**  
Clears all files from the folder specified. Does not delete folders.

**Args:**
>folderPath
  - Path of the folder to clear.

<br />

---

<br />

## **fileProcessor_emailer**

<br />

## *studyfind_removeDupEmails_inPlace*  

**Description:**  
Removes rows that contain duplicate emails.

**Args:**
>filePath
  - Path of the file to process

<br />

## *studyfind_fix_columns*  

**Description:**  
Adjusts column names to match the emailer function expectations.

**Args:**
>filePath
  - Path of the file to process

<br />

## *studyfind_sendEmails*  

**Description:**  
Sends emails from a file. 

**Args:**
>filePath
  - Path of the file to email from
>from_email
  - Email to send messages from (MUST BE IN THE EMAIL_DICT)
>num_emails=50
  - The number of emails to send every 70 seconds (to avoid spamming)

<br />

---

<br />

## **fileProcessor_globals**

<br />

## *BASE_FOLDER_NAME*  

**Description:**  
Destination folder for file downloads. This folder holds files *to be processed*.

<br />

## *EMAIL_FOLDER_NAME*  

**Description:**  
Destination folder for *processed* files. This folder holds files that will be used to *send emails*.

<br />

## *EMAIL_DICT*  

**Description:**  
Dictionary that holds email information. Must be of the format:  
> EMAIL_DICT = {  
&nbsp;&nbsp;&nbsp;&nbsp;"email@email.com": {  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"app_password": "",     (str)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"subject_lines": [],    (str list)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"body": []              (str list)  
&nbsp;&nbsp;&nbsp;&nbsp;},  
}

<br />

---

<br />

## **fileProcessor_drive**

<br />

## *google_get_creds*  

**Description:**  
Gets the Google OAuth credentials from the credentials.json file. 

**Args:**
None

<br />

## *google_fetch_folder*  

**Description:**  
Gets a folder with the specified name from Google Drive. Error if there are more than one found. Returns the ID of the folder.

**Args:**
>creds
  - OAuth credentials obtained from get_google_creds
>folderName
  - Name of the folder to get

<br />

## *google_create_folder*  

**Description:**  
Creates a folder with the specified name in Google Drive. Returns the ID of the folder.

**Args:**
>creds
  - OAuth credentials obtained from get_google_creds
>folderName
  - Name of the folder to create

<br />

## *google_upload_file*  

**Description:**  
Uploads a file into Google Drive. Returns the file's ID.

**Args:**
>creds
  - OAuth credentials obtained from get_google_creds
>filePath
  - File path of the file to upload
>mimeType='text/csv'
  - Mime type of the file to upload

<br />

## *google_upload_into_folder*  

**Description:**  
Uploads a file into a Google Drive folder. Returns the file's ID.

**Args:**
>creds
  - OAuth credentials obtained from get_google_creds
>filePath
  - File path of the file to upload
>googleFolderId
  - ID of the destination folder in Google Drive
>mimeType='text/csv'
  - Mime type of the file to upload

<br />

## *google_share_file*  

**Description:**  
Shares a Google Drive file with the emails provided.

**Args:**
>creds
  - OAuth credentials obtained from get_google_creds
>fileId
  - ID of the file to share
>emails
  - list of emails to share with

<br />

## *google_download_file*  

**Description:**  
Downloads a specified file from Google Drive.

**Args:**
>creds
  - OAuth credentials obtained from get_google_creds
>fileId
  - ID of the file to download

<br />

## *google_get_files_from_folder*  

**Description:**  
Fetches all files from a Google Drive folder.

**Args:**
>creds
  - OAuth credentials obtained from get_google_creds
>folderId
  - ID of the folder to fetch from
>mimeType='text/csv'
  - mimeType of files to fetch

<br />

## *google_get_n_files_from_folder*  

**Description:**  
Fetches n files from a Google Drive folder.

**Args:**
>creds
  - OAuth credentials obtained from get_google_creds
>folderId
  - ID of the folder to fetch from
>numFiles
  - Number of files to fetch
>mimeType='text/csv'
  - mimeType of files to fetch

<br />

## *google_download_from_folder*  

**Description:**  
Downloads files from a Google Drive folder.

**Args:**
>creds
  - OAuth credentials obtained from get_google_creds
>folderId
  - ID of the folder to download from
>localFolderPath
  - Local folder to download into

<br />

## *google_download_n_from_folder*  

**Description:**  
Downloads n files from a Google Drive folder.

**Args:**
>creds
  - OAuth credentials obtained from get_google_creds
>folderId
  - ID of the folder to download from
>localFolderPath
  - Local folder to download into
>numFiles
  - Number of files to download

<br />

## *google_move_to_folder*  

**Description:**  
Moves a Google Drive file to a Google Drive folder.

**Args:**
>creds
  - OAuth credentials obtained from get_google_creds
>fileId
  - ID of the file to move
>folderId
  - ID of the folder to move to

<br />

## *google_add_parent*  

**Description:**  
Adds a Google Drive folder as the parent of a Google Drive file. (similar to moving that file into the folder specified)

**Args:**
>creds
  - OAuth credentials obtained from get_google_creds
>fileId
  - ID of the file to move
>parentId
  - ID of the parent to add to the file

<br />

---

<br />

## **fileProcessor_webscraper**

<br />

## *runWebscraper*  

**Description:**  
Runs the studyfind webscraper to get email addresses for each study in the file provided. (Written by Etna Ozkara)

**Args:**
>filePath
  - file path of the file to use for webscraping

<br />

---

<br />

## **fileProcessor_autofill**

<br />

## *download_all_files*  

**Description:**  
Downloads one file for each keyword term provided. These files are downloaded from clinicaltrials.gov.

**Args:**
>disease_terms=[]
  - List of terms to search for on clinicaltrials.gov that will be filled into the "Condition or disease" field.
>other_keys=[]
  - List of terms to search for on clinicaltrials.gov that will be filled into the "Other terms" field. This will include ALL NON-DISEASE RELATED TERMS such as ethnicity, gender, sex, etc.
>directory_name="to_upload"
  - Folder name to download into
>default_filename="SearchResults.csv"
  - default name of files downloaded to facilitate renaming and moving of files.
>upload_to_drive=False
  - True if files should be uploaded to the BASE_FOLDER_NAME folder in Google Drive

<br />

## *download_file*  

**Description:**  
Downloads one file with the terms provided. The query includes ALL OF THE TERMS, NOT ONE AT A TIME. The file is downloaded from clinicaltrials.gov. Terms will be either only one term, or of the format "TERM1 OR TERM2 AND TERM3 NOT TERM4" (in any order). Refer to clinicaltrials.gov to understand how queries can be modified using AND/OR/NOT.

**Args:**
>disease_terms=""
  - Terms to search for on clinicaltrials.gov that will be filled into the "Condition or disease" field. 
>other_keys=""
  - Terms to search for on clinicaltrials.gov that will be filled into the "Other terms" field. This will include ALL NON-DISEASE RELATED TERMS such as ethnicity, gender, sex, etc.
>directory_name="to_upload"
  - Folder name to download into
>default_filename="SearchResults.csv"
  - default name of files downloaded to facilitate renaming and moving of files.
>upload_to_drive=False
  - True if files should be uploaded to the BASE_FOLDER_NAME folder in Google Drive

<br />

## *upload_file_to_drive*  

**Description:**  
Uploads a file to the BASE_FOLDER_NAME folder in Google Drive

**Args:**
>creds
  - OAuth credentials obtained from get_google_creds
>file_path
  - Path of the file to upload

<br />

## *update_file_name*  

**Description:**  
Creates a file name based on the terms used in the queries.

**Args:**
>disease_terms
  - Condition/Disease terms used in the query
>other_keys
  - Other Terms used in the query
>country
  - Country used in the query

<br />

## *autofill_clinicaltrials*  

**Description:**  
Autofills the query form on clinicaltrials.gov based on the inputs provided, and clicks download after results are received.

**Args:**
>browser
  - browser opened by the selenium webdriver
>disease_terms=""
  - Terms to search for on clinicaltrials.gov that will be filled into the "Condition or disease" field. 
>other_keys=""
  - Terms to search for on clinicaltrials.gov that will be filled into the "Other terms" field. This will include ALL NON-DISEASE RELATED TERMS such as ethnicity, gender, sex, etc.
>country=""
  - Country to use in the query (MUST BE THE FULL COUNTRY NAME SPELLED CORRECTLY)
>default_filename="SearchResults.csv"
  - default name of files downloaded to facilitate renaming and moving of files.

<br />

---
