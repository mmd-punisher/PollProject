## Excel Settings To Set On Your Device

This is a problem I face frequently with Microsoft Excel when opening CSV files that contain Arabic characters. Try the
following workaround that I tested on latest versions of Microsoft Excel on both Windows and MacOS:

1. Open Excel on a blank workbook
2. Within the Data tab, click on From Text button (if not activated, make sure an empty cell is selected)
3. Browse and select the CSV file
4. In the Text Import Wizard, change the File_origin to "Unicode (UTF-8)"
5. Go next and from the Delimiters, select the delimiter used in your file e.g. comma
6. Finish and select where to import the data