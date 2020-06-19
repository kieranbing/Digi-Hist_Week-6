# Notes
### Initial Thoughts 
I spent a good amount of time browsing the diary listings to see what I might be interested in investigating. Among a few of my top choices was [Operation War Diary]( http://www.operationwardiary.org/#/), a WW1 diary digitisation initiative. Sadly I am unable to access this resource as it seems to have finished and not made its results public. I was also interested in civil war diaries, and the [diary of George Orwell]( https://orwelldiaries.wordpress.com/). I decided that I would like to examine Orwell’s diaries and see what lies inside. Some of my main questions at the beginning of my research are: How did Orwell’s wartime experience shape his later literary works? Did he comment on authoritarianism in his writings? Did Orwell witness anything he did not agree with during the war? 
### Extracting and Refining the Data
I started by using wget to download all the pages on the site that I wanted to analyse. I decided to use entries from March 1942 until the end. This is quite a few entries so I wasn’t surprised when the download took half an hour. 

This didn’t quite work out how I had intended. I got all the code from the website in 35 different files. In order to extract the journal text from this I new it would take a lot of work to comb through each file. Before subjecting myself to that I decided to try something else. I tried the lazy way or just copying all the text on the page, but that didn’t work as it would only copy a certain number of entries. I could copy the entries one page at a time into sublime text then refine them, but that doesn’t feel like the right method to use to show my learning in this course. I could also write a python script to comb through the site data I downloaded and extract the content, but I don’t know if I have time for that. 

After deciding to organize a smaller amount of data myself I decided on a n XML scheme for the data; Date, Content, Comment. I then set to work copying all the data into Sublime and formatting it to CSV (separated by commas). 

After a large amount of manual toiling I have created an Excel workbook from Orwell’s second war diary. Now I can export it to CSV to clean it up for analysis. 

I put the exported CSV file into sublime in order to use REGEX to clean it up a little bit. First I wanted to remove all of the “[1]” markers that were added for reference. With the REGEX line “[[][1-9]]” I was able to find and remove them all at once. 

### Analysis 
I created a new version of the excel document so that I could format it for some data analysis. First I tried to re-import the .csv file I had cleaned up, but was unable to complete the import. Excel wanted to split the data at each new-line as well as comma. So instead of manually deleting all the new lines, I’m going to use the non-clean version of my data for this part of the analysis. 

I want to see how frequently Orwell writes in his diary during these months of the war (March – November, 1942). So the first thing I did was use this formula “=LEN(B2)-LEN(SUBSTITUTE(B2," ",""))+1” to do a wordcount of the content of each diary entry. This should give me a good idea of the volume of writing Orwell did over a specified period. 

I want to be able to organize and analyse my data using dates and time periods, like the months. In order to do this I need to be able to get the date information from my rows. Sadly this is more complicated than it should be. Because of the format of my dates excel does not recognise them. So I need to go and manually replace each date (d.m.y) with excel’s date format (=DATE(y,m,d)). It is going to be tedious, but worth it to properly manipulate my data. 

After changing all of the dates to excel format I created a new column to hold the month the entry was written in. I then created a new table with each of the months to gather and analyse data on a month by month bases. I used a sum formula to add up the wordcount for each moth in it respective cell. I then wanted to know which months Orwell wrote most frequently, so I needed to know how many times he wrote a month as well as how often. I ended up manually counting the number of entries in each month after having some trouble using a counting formula. I noticed that the month of August had the most entries by far, yet not the most words. I then went to each date and subtracted the previous date to get the number of days between entries. I hope getting an average of this will give me insight into the frequency of Orwell’s journaling. 

I realized that an average of time between diary entries wouldn’t provide any more information than the number of entries per month did as average time between entries is equal to number of entries over days in the month. 

### Presentation and Conclusion 
I turned the data into a table combining the wordcount and number of entries. It shows that on months with lots of entries, Orwell wrote little, and vice versa. Perhaps because there was so much going on he needed to write updated but didn’t have the time to go into detail. 

