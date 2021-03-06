# Journal 
## Subject search and data extraction
I have had a much harder time with this than I thought I would. It took me much longer than I thought it would to find good data that I could analyse. Once I found that data I realised that extracting what I wanted from it was also much more time consuming than I had anticipated. The source I had chosen, Orwell’s war diaries, was in the form of a WordPress site. This caused issues for me as downloading it’s pages using wget had unexpected results. It ended up downloading the whole page’s HTML. This would mean I would need to comb through 35 large HTML documents in order to extract the data I need. I could write a python script to use REGEX and extract the text between certain HTML tags. However, I didn’t believe I would have time for that. I want to spend most of my time on analysis and presentation, so I didn’t have as much time to spend on data extraction as I was doing. 

In the end I decided that although I think the best solution would be to make a python script to parse the HTML files into the data I need, I don’t know python well enough to do that in the scope of this assignment. So I am going to copy the entries I need and modfy them manually. This means I need to reduce the scope of my analysis, but this is necessary with my current time restraints. 

I turned Orwell’s second war diary into an excel worksheet. It took a lot of time, but I think it was worth it. Now I can both export it to CSV, or use excel to analyse it. It still needs to be refined a bit, there are ‘[1]’ reference markers that I don’t want affecting my analysis. Those should be easy enough to remove with REGEX. 

I removed all of the markers, but wasn’t able to re-import that version of the data back into excel without removing all the new lines. It’s a shame, but it reinforces the lesson I’m learning this week, sometimes it’s the small parts of the project that take the most time and effort. 
## Analysis 
I found this part of the process to be both satisfying and frustrating so far. It’s satisfying looking at my data, thinking of a question, then trying to find an answer to that question. What is frustrating is when the software fights me. Sometimes I find that there is no easy way (that I know of) to do something that I think should be simple. Or there is a way to do it, but a formatting problem or something like that gets in the way. I had to do a lot more manual analysis in excel than I though I would. Still, I found it all rather enjoyable, I just wish I had more time to play around with the data and come to meaningful conclusions. 

I think I did a good job with my excel analysis. If I had more time I know I could add more to it and answer more questions. With the time I had though I think I at least answered one question. It’s also all very nicely organized and I think there is lots of ways to make the data work for me even better. There is lots of potential in analysis like this, I just don’t have any more time in the scope of this last week to capitalise on it. 

I plugged the data into Voyant-tools to see if there was any pattern in the wording. The word cloud was surprising. Terms I expected showed up like german and atrocities, but the most popular word was india. This makes sense as Orwell was often in contact with people about Indian affairs. Voyant also links the word government with people, which shows a bit of what Orwell thinks the government should be. I really wish I had a bit longer to dig deeper into this, but sadly I don't. 

## Presentation and Conclusion
I decided to present my data in a combined graph, with the wordcount as a bar graph and the number of entries as a line graph. I think it really highlights the comparison I wanted to make, and the difference between how much Orwell wrote and how often. 
![Graph of Orwell's writting habits](https://github.com/kieranbing/Digi-Hist_Week-6/blob/master/Images/Orwell%20Diary%20Analysis%20v2.PNG "Graph of Orwell's writting habits")

![Word-cloud of Orwell's second war diary](https://github.com/kieranbing/Digi-Hist_Week-6/blob/master/Images/WordCloud.PNG "Word-cloud of Orwell's second war diary")
