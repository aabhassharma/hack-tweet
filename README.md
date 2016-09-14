This is a simple multi step experiment to see if I can get increased Twitter traction using some simple software.

Here are the steps to collect the data:
* Write a script that runs periodically, finds the most popular hashtags trending on Twitter
* From the most popular hashtags, find the most popular tweets that meet some criteria related to those hashtags.
* Save most popular tweet data to file

Now that we have the data, here's the tweet part:
* Use simple NLP to see if we can determine some sentiment about this text
* If the NLP returns a negative sentiment, throw the data away
* If neutral or positive, store in a file for further processing

Now that we have a file of neutral and/or positive data, multiple approaches we can take:
* Simply retweet what was said (Phase 1)
* What I'm more excited for : Take the trending word, make a simple sentence from it using NLP, tweet that

STATUS:
We're almost done with the data collection parts! 
