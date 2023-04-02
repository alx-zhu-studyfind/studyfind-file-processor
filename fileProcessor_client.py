from fileProcessor_globals import *
from fileProcessor_cloud import process_files, send_emails
from fileProcessor_autofill import download_all_files
from fileProcessor_webscraper import runWebscraper

def get_menu():
    menu = '''
----------------------------------------------------
Studyfind File Processor: Choose an option (1-3) 
to perform the desired action, or type 'q' to quit.
----------------------------------------------------
1. Download files from clinicaltrials.gov.
2. Process csv files to prepare for emailing.
3. Send emails from a processed csv file.
----------------------------------------------------
'''
    return menu

if __name__ == "__main__":
    print(get_menu())
    while True:
        option = input(">>> ")
        if option == '1':
            print("DOWNLOADING FILES")
            download_all_files(disease_terms=TERMS, upload_to_drive=True)
            print(get_menu())
        elif option == '2':
            print("PROCESSING CSV FILES")
            process_files(processingFn=runWebscraper, )
            print(get_menu())
        elif option == '3':
            print("SENDING EMAILS")
            for email in EMAIL_DICT:
                send_emails(email)
            print(get_menu())
        elif option == 'q':
            break
        else:
            continue


    
