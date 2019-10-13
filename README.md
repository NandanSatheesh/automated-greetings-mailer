# automated-greetings-mailer

[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/check-it-out.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)  
Some experiments with SMTP (YAGMail - Yet Another Gmail Client) for automating birthday and anniversary wishes.


## Setting up 
Libraries used in this project are 
- yagmail 
- pymongo
- dnspython 
- keyring 
- entrypoints 


## MongoDB Setup
MongoDB Atlas was used for this project.  
Document Format - 
```
{
  _id:Object("..."),
  name:"Alex",
  birthday:"13/10",
  anniversary:"12/5"
  .
  .
  .
  .
}
```


## Customize 
You can also send your own customized fancy wishes in HTML too. 

## Usage 
Make a cron job to check and send greetings once a day using a cron job.   
Add this line in the crontab   
`* 10 * * * python main.py > output.txt`

## Contribute 

Want to contribute? Great!  

## Links 

https://realpython.com/python-send-email/   
https://help.dreamhost.com/hc/en-us/articles/215767047-Creating-a-custom-Cron-Job
