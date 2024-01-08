# AiTHLETES - Capstone Project
#### Fall Semester 2023/2024

##
### Table of contents

1. [Project Description](#proj_desc)
  1.1 [Main Technologies Used](#main_tech)
  1.2 [Main Challenges Faced](#main_chal)
2. [Repository Description](#rep_desc)
3. [How to Use](#proj_use)
   3.1. [How to Interact with our Chatbot](#chat_int)
4. [Credits](#credits)
5. [License](#license)
6. [References](#ref)
##

<a name="proj_desc"></a>
## Project Description

This project comes for the completion of a university course - Capstone Project - in the third year of a Bachelor's Degree in Data Science at Nova IMS.

Our company, AiTHLETES,  was designed to get data insights from the F1 world. The major objective of our company is to help F1 fans all over the globe get a complete perspective on all aspects of Formula 1.  

The project aims to develop an interface specialized in F1 history - the F1 Pilot - as well as being able to predict the drivers' standings with each grand prix data. Also, it is supposed to help any user with their F1 Fantasy Team being able to adapt to any restrictions existing in the fantasy rules and help users build their ideal team.

In addition, a website was also developed, where our F1 Pilot was inserted. There, users can find several pages where they can interact with everyone and even with the developers of this project via the site's F1 Blog; a Data Hub where up-to-date data is powerfully displayed and in a user-friendly manner; and a comment section where everyone can give suggestions via email to the marketing department.

This way, as the fanbase of the sport keeps on growing, we are looking to spread more accessible data insights about everything that is going on weekly on the track! With the power of artificial intelligence, we can be side by side with any question our users might have daily.


<a name="main_tech"></a>
### - What main technologies were used in the development of this project?
For this project, the main goal was to create an AI-powered Conversational System that would engage with any type of potential Formula One fans. This would be the primary communication channel of our business - being able to assist our users in getting to know more facts about historical data, landing some insights about the last race, as well as their fantasy team changing possibilities; and mostly, to help them to have a better possibility of guessing the future race winners with the predictive model implemented that was implemented. All this by using the conversational app - the F1 Pilot. 

With this project, we were able to explore more in-depth how to make use of LLM models, from OpenAI, in different problems (with Python being the chosen programming language) - through the development of a chatbot capable of handling (and reproducing) a smooth conversation about facts and possible doubts that the Pilot's users may have. Furthermore, it was also the objective for the AI to be able to predict which drivers are more likely to win the following races as well as who might be the best fit for their fantasy team, by making use of a Forecasting model that was developed for the utilized time-series data. Furthermore, by making use of the Streamlit package, the group developed a full Web Application with several tabs, filling them with easy-to-understand knowledge making the information available accessible to the most casual fan or even to a new follower of the World's Most Entertaining Motorsport.

<a name="main_chal"></a>
### - What were the main challenges faced? 
The main challenges faced during the development of this project were related with:
- The Team's limited budget in OpenAi made it very hard to use and interact with the chat. Hence, there was a need to become more cautious and restrict some of the parts of the development stage;
- The team's original idea of data to provide to the AI, turned out to be impossible to achieve. There were tons of files, some of them with thousands of rows, which made the code prompt errors on several occasions stating that the tokens could not be embedded;
- As the majority of Formula 1 data is based on tables or comma-separated values files (.csv), it was not always possible for the ChatBot to get new information from those types of files. We were required to change our approach and create new PDFs filled with the previously tabled data;
- The chatbot required very specific instructions to ensure the correct outputs were obtained, which was an extremely time-consuming process (sort of trial and error);


Afterwards, you can have fun interacting on our website alongside our F1 Pilot.

<a name="credits"></a>
## 
#### Project Developed by:
- Afonso Cadete | 20211519@novaims.unl.pt 
- Daniel Kruk | 20211687@novaims.unl.pt 
- Marcelo Junior | 20211677@novaims.unl.pt 
- Martim Serra | 20211516@novaims.unl.pt 
##

<a name="license"></a>
## License
This project is licensed under the [GNU AGPLv3] - see the [LICENSE.md](LICENSE.md) file for details.
##
