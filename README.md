# Running the code
The project is built using Python 3.4 and has no non-standard library dependencies. You should be able to download or clone the project and run the code from its parent directory by executing 'python owlstone_test' on the command line. I have tested it on Windows and OSX. 

# What it does
The Python scripts analyse 30 text files, 10 from each of three different news publishers, which are saved as part of the project, and derives a number of statistical results based on their content, including: 

1. The average word count, by article, by publisher
2. A measure of the variation in article length
3. The average length of words used, by publisher
4. The average proportion of words in each article that are included as quotes
5. The average number of words per paragraph per article

Running the code makes the data for the first of these measures available to a basic web page, saved in the root project directory, which uses D3 to display a simple bar chart showing average word count by publisher. 

Python's standard http.server library then makes this page available to the network at your IP address on port 8000. 

# What it doesn't do yet
There wasn't time to visualise any of the other data points collected in the script. A scatterplot of the word length for each article against the paragraph length with dots coloured according to publisher would have provided more insights into the differences between the three publishers. And showing the proportion of words that appear as quotes as a stacked bar chart would have shown that the Atlantic barely makes any use of direct quotes, whereas the Sun relies very heavily on them. 

It also doesn't yet perform any sort of significance test on the derived statistics, which would be worthwhile in a real-world setting. 

# What considerations should be taken into account when building such tools?

1. **Who is going to be using the tool and why?**
I have produced a tool that performs some analysis on pre-prepared articles and surfaces some conclusions about them. 

But it may be that users of the tool would need to submit other articles for analysis via the network and run the analysis again, or filter the conclusions in some way, e.g. by publisher. These are features that could be added were more time available. 

2. **Is the code well documented and comprehensible to other developers who might need to work on it?**
The project will at present work in only one very specific set of circumsances, and would need a significant amount of refactoring if it was required to work in other ways. For example, if we were to enable users of the web interface to submit text over the network, the read_files module would need to be quite different. A system of generic classes that could be inherited from and customised depending on these sorts of requirements would help with this. 

3. **Are there appropriate network security safeguards in place?**
The app exposes data on the user's computer to other computers on a network and caution should always be exercised in such cases. 

4. **How much data will the app be consuming?**
In this instance, there are relatively few files and none of the files is large. But it is possible to imagine similar analysis on a much larger scale, e.g. with many thousands of files, causing problems for the computer running the scripts. To scale this programme up, there would need to be detailed work on optimising the code. 

5. **How might it go wrong?**
There is some basic error handling in the code, but more time would be needed to consider all the ways in which it might go wrong were the code to be opened up to other users, e.g. if text files were encoded badly, or port 8000 was already in use. Adding rigorous unit tests would be essential if the tool were to be used in production. 
