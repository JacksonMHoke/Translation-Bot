# Translation-Bot

# Description
This bot takes my brothers tweets(@HapaGucci) and translates them through a random number of languages with the final language being back to english. It then
takes the translated tweet and posts it to the twitter account @BotsonHoke

![](https://github.com/JacksonMHoke/Translation-Bot/blob/main/thomas1.PNG)      ![](https://github.com/JacksonMHoke/Translation-Bot/blob/main/botson1.PNG)

![](https://github.com/JacksonMHoke/Translation-Bot/blob/main/thomas2.PNG)      ![](https://github.com/JacksonMHoke/Translation-Bot/blob/main/botson2.PNG)

# How It Works
This bot uses the Tweepy api in python to check if a new tweet has been made by comparing the past 20 tweets the bot has parsed to the 20 tweets fetched by the api
from my brothers twitter. If a difference is seen, the bot translates the new tweet using the Translators api on python to translate the tweet through random languages
and finally back into english. The bot runs on an AWS EC2 Ubuntu instance using Docker images so I don't have to run the bot off my computer 24/7.
