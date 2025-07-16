# CMDQ - Musculoskeletal Health Survey System

CMDQ is a survey-based project designed to help supervisors and employers monitor musculoskeletal complaints reported by their workforce. The system collects self-reported data regarding muscle discomfort, pain, and related issues, providing useful insights to assist with occupational health management.

## Features

- **Employee Health Monitoring:** Enables tracking of musculoskeletal issues reported by workers.
- **Survey-Based Data Collection:** Based on the standard CMDQ (Cornell Musculoskeletal Discomfort Questionnaire).
- **User-Friendly Interface:** Simple and accessible UI for participants.
- **Admin Dashboard:** 
  - View aggregated and individual reports.
  - Powerful filtering options to analyze specific groups of workers.
  - Export reports and filtered data to CSV files.
  - Comprehensive data management tools for supervisors.

## Tech Stack

- **Frontend:** Developed by [Alireza Esmaeili](https://github.com/BAADEH)
- **Backend:** Developed by [Mohammad Moosapour](https://github.com/mmd-punisher)

## Project Repository

[PollProject on GitHub](https://github.com/mmd-punisher/PollProject)

## Purpose

This project aims to support occupational health initiatives by providing a streamlined way to collect and analyze workers' musculoskeletal discomfort reports.


## Project Shots

<img width="1456" height="657" alt="image" src="https://github.com/user-attachments/assets/9eb56ef2-390b-4c50-b909-0656977caffb" />

<img width="1451" height="658" alt="image" src="https://github.com/user-attachments/assets/9874a07f-4a3d-47bf-aabb-af6e34099e5c" />

<img width="1449" height="712" alt="image" src="https://github.com/user-attachments/assets/dda06677-fe87-4a86-998d-e87a1e3104e0" />


## License

This project is open-source and available under the MIT License.



## Excel Settings To Set On Your Device

This is a problem I face frequently with Microsoft Excel when opening CSV files that contain Arabic characters. Try the
following workaround that I tested on latest versions of Microsoft Excel on both Windows and MacOS:

1. Open Excel on a blank workbook
2. Within the Data tab, click on From Text button (if not activated, make sure an empty cell is selected)
3. Browse and select the CSV file
4. In the Text Import Wizard, change the File_origin to "Unicode (UTF-8)"
5. Go next and from the Delimiters, select the delimiter used in your file e.g. comma
6. Finish and select where to import the data
