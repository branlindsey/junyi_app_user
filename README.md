# junyi_app_user
Can we predict who will be using the site in the next week? In addition to provide valuable educational content.  Education apps and website use a variety of strategies like points, badges, personalized learning plans, and leaderboards to keep learners engaged in the content.  

## What is the story? 

As public schools have shut down across the country, students and educators at all levels have been forced to develop new strategies.  One of the primary strategies has been educational apps.  

In my case my 7 year old son, his teachers have directed us towards Splash Math for Math and Epic Books for reading practice. Because the teachers are connected to these apps, they are able to see our son's progress. On top of this we have been using two additional apps to help him keep up with his studies. We are using Duolingo for Chinese and Khan Academy for Math.   

As the school closure persists and the possibility of an even longer closure persists. I wonder how long will we stick with these apps.  Typically with educational apps, I stick with them for a little while, but I get bored and then stop.  With a long term school closure, the stakes seem much higher. As parents are working and have less time than a clasroom teacher, we are relying on apps to teach and engage our students more and for longer than ever.  

Unfortunately, the apps that we are using don't make their data publicly available.  

Finding a good set of education app/website data was not easy! After a lot of searching across of a variety of open data platforms.  I found 

https://pslcdatashop.web.cmu.edu/Project?id=244

Number of data points (rows, pages scraped): 259259

## What is Junyi Academy
Junyi Academy is a Chinese platform that was started with the help of Khan Academy, and uses many of the same strategies and metrics to teach students.   In this way, it will provide an approximation of the applications that many students around the world are currently using.  

https://www.junyiacademy.org/

<img src='https://github.com/branlindsey/junyi_app_user/blob/master/images/Screen%20Shot%202020-05-14%20at%2011.07.56%20AM.png', width='200' height='200'> 

<img src='https://github.com/branlindsey/junyi_app_user/blob/master/images/Screen%20Shot%202020-05-14%20at%2011.08.25%20AM.png', width='200' height='200'> 

This data focuses on Geometry and Algrebra lessons in the platform from October 2013 to January 2015. The entire dataset was used to complete EDA.  For modelling and predictions, the 2014 calendar year was used.   


## Process

#EDA
To get a better sense of the entire data set, I performed exploratory data analysis.  I used the exploratory data analysis to get a sense of what feature engineering would be necessary.  

Days Active Graph
Around 2/3 of the users in the dataset were only active a single day.    

Activities Graph
There is a large spike at 10 activities.  This could be attributed to the fact that 10 correct activities in a row are needed to earn a proficiency in a topic.   Nearly half of all of the users in dataset got to this level of activities and then stopped using the site.   

Days Active vs. Activities 
This plot demonstrates that most of the usage clusters toward the bottom right, but there is also a wide variety of usage that extends beyond a hundred days and many thousands of activities.   

Months? 
It is possible to see that usage varies by month, especially during July and August. Schools in China take a break during this season too, but usage ramps up in the fall.   

Can I get a turnover graph? 
There is a lot of turnover! 

#Data Preparation 
The data set contains activities 
- Show columns 

#Modeling
The initial model was a Logistic Regression performed using the mean statistics of users over the first 6 months of 2014 and then trying to predict whether these users would be active in the second part of the year. 

I reviewed the beta-coefficients to get a sense of which features were impacting the prediction. 
It looked like correct answers, whether hints were used, and the amount hints used were the most impactful.  



