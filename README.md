# junyi_app_user
Can we predict who will be using the site in the next week? In addition to provide valuable educational content.  Education apps and website use a variety of strategies like points, badges, personalized learning plans, and leaderboards to keep learners engaged in the content.  

## What is the story? 

As public schools have shut down across the country, students and educators at all levels have been forced to develop new strategies.  One of the primary strategies has been educational apps.  

In my case my 7 year old son, his teachers have directed us towards Splash Math for Math and Epic Books for reading practice. Because the teachers are connected to these apps, they are able to see our son's progress. On top of this we have been using two additional apps to help him keep up with his studies. We are using Duolingo for Chinese and Khan Academy for Math.   

As the school closure persists and the possibility of an even longer closure persists. I wonder how long will we stick with these apps.  Typically with educational apps, I stick with them for a little while, but I get bored and then stop.  With a long term school closure, the stakes seem much higher. As parents are working and have less time than a clasroom teacher, we are relying on apps to teach and engage our students more and for longer than ever.  

Unfortunately, the apps that we are using don't make their data publicly available.  

Finding a good set of education app/website data was not easy! After a lot of searching across of a variety of open data platforms.  Fortunately, I found the [DataShop](https://pslcdatashop.web.cmu.edu/index.jspat) Carnegie Mellon University.  The website has datasets specifically targeted towards learing science. Here I was able to locate the [Junyi Academy Math](https://pslcdatashop.web.cmu.edu/Project?id=244) dataset. 


## What is Junyi Academy
[Junyi Academy](https://www.junyiacademy.org/) is a Chinese platform that was started with the help of Khan Academy, and uses many of the same strategies and metrics to teach students.   In this way, it will provide an approximation of the applications that many students around the world are currently using.  



<table> 
<tr>
<td>
<img src='https://github.com/branlindsey/junyi_app_user/blob/master/images/Screen%20Shot%202020-05-14%20at%2011.07.56%20AM.png'> 
    </td>
<td> 
  
</td>    
<td>
 <img src='https://github.com/branlindsey/junyi_app_user/blob/master/images/Screen%20Shot%202020-05-14%20at%2011.08.25%20AM.png'> 
    </td>
</table> 
    
This data focuses on Geometry and Algrebra lessons in the platform from October 2013 to January 2015. The entire dataset was used to complete EDA.  For modelling and predictions, the 2014 calendar year was used.   


## Process

### EDA
To get a better sense of the entire data set, I performed exploratory data analysis.  I used the exploratory data analysis to get a sense of what feature engineering would be necessary.  

**Days Active **
![Graph 1](https://github.com/branlindsey/junyi_app_user/blob/master/images/users_vs_active_days.png)

Around 2/3 of the users in the dataset were only active a single day. Looking at 10 days of usage, the curve flattens out, so I decided to use users with more than 10 days of usage for my prediction.    

*Activities Graph*
![Graph 2]
There is a large spike at 10 activities.  This could be attributed to the fact that 10 correct activities in a row are needed to earn a proficiency in a topic.   Nearly half of all of the users in dataset got to this level of activities and then stopped using the site.   

*Days Active vs. Activities*
![Graph 3]
This plot demonstrates that most of the usage clusters toward the bottom right, but there is also a wide variety of usage that extends beyond a hundred days and many thousands of activities.   

*Months?* 
It is possible to see that usage varies by month, especially during July and August. Schools in China take a break during this season too, but usage ramps up in the fall.   

Can I get a turnover graph? 
There is a lot of turnover! 

### Data Preparation 
The data was loaded into a Pandas DataFrame and cleaned by removing unneeded columns, and changing boolean values to integers.   
- Show columns 



### Modeling
The initial model was a Logistic Regression performed using the mean statistics of users over the first 6 months of 2014 and then trying to predict whether these users would be active in the second part of the year. 

Because the churn rate is so high on this user set, the target value is heavily weighted. This made predicting a churn very easy and in general the accuracy score was high. For the purposes of predicting who will remain a user, the recall and precision scores are much more valuable.  

I reviewed the beta-coefficients in the initial logistic regression. to get a sense of which features were impacting the prediction. 
It looked like the features of correct answers, whether hints were used, and the amount hints used were the most impactful.  
After getting a basic idea of the prediction ability of logistic regression model.  I moved to a Random Forest Classifier.  This improved both my recall and precision scores.  I used a GridSearch to settle on the hyperparameters to use on the Random Forest. 

I tried a Gradient Boosting Classifier as well. I used a GridSearch to settle on the hyperparameters to use on the Random Forest.  This improved my recall, but lowered the precision.  


After each round of modelling, I engineered additional columns. For example, I added columns to determine the amount activities completed, the days active before the prediction date.  I also made the decision to cut the data set to users who had more than 10 days of active use.  



Confusion Matrix 

## Add an ROC curve 
## Add a Feature importance graph


-Accuracy  of best:  0.7778
-Precision of best:  0.7381684081130916
-Recall    of best:  0.6367974549310711


|     |  Actual+   |  Actual-   |
|----:|:-----------|:-----------|
|Pred+|    2500    |    793     |
|Pred-|    1290    |   5417     |
    </td>
<td> 
|     |  Score  |   
|----:|:-----------|
|Precision|   TBD  
|Accuracy|    TBD     
Recall|    TBD 
    </td>



Additional Data Points of Interest
Some additional data points may have increased the ability to predict who would stay active. 
- Logged-in vs. Guest User
