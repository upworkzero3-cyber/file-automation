\# File and Folder Automation



A Python command-line script that organizes files into folders by extension.



\## Features



\- Sorts PDFs, images, spreadsheets, text files, documents, and archives.

\- Places unrecognized file types in an Other folder.

\- Previews planned moves with dry-run mode.

\- Logs successful moves, skipped files, and move errors.

\- Accepts a folder path from the command line.

\- Skips existing destination filenames.

\- Skips subfolders and source-file symbolic links.

\- Excludes the running script and its log file.



\## Requirements



Python 3.9 or newer. No external packages are required.



\## Usage



Preview files in a selected folder:



```powershell

python organize.py "D:\\file-automation\\downloads" --dry-run

```



Move the files:



```powershell

python organize.py "D:\\file-automation\\downloads"

```



Use the default downloads folder beside the script:



```powershell

python organize.py --dry-run

```



Create that folder first if it does not exist.



\## Folder Categories



| Extensions | Destination |

|---|---|

| .pdf | PDFs |

| .jpg, .jpeg, .png | Images |

| .csv | Spreadsheets |

| .txt | Text |

| .docx | Documents |

| .zip | Archives |

| Other extensions | Other |



Files are classified by extension, not by their contents.



\## Logging



Actual runs append entries to organizer.log beside the script.

Each entry includes a timestamp, severity level, and action details.

Dry runs do not write to the log or create destination folders.



\## Safety and Scope



The script moves files; it does not intentionally delete them.

It checks for existing destination filenames and skips those files.



Use a dry run first and test with sample files.

Avoid running multiple organizers on the same folder simultaneously.

Use ordinary local folders without linked destination folders.



Only files directly inside the selected folder are organized.

Sorting by date and automatic undo are not implemented.

