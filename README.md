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
For this project, the main goal was to create an AI-powered Conversational System that would engage with potential F1 fans. This would be the primary communication channel of our business - being able to assist our users (getting to know more facts about historical data, landing some insights about the last race, as well as their fantasy team changing possibilities; and mostly, help them to have a better understanding of future possible race winners with the predictive model implemented) through a conversational app. 

With this project, we were able to explore more in-depth how to make use of LLM models, from OpenAI, in different problems (with Python being the chosen programming language) - through the development of a chatbot that can perform smooth facts and doubts conversations, predict which drivers are more likely to win the following races as well as who might be the best fit for their fantasy team. Furthermore, the team learned how to create an application using Streamlit.

<a name="main_chal"></a>
### - What were the main challenges faced? 
The main challenges faced during the development of this project were related with:
- Team's limited budget in OpenAi - using and interacting with the chat. Hence, there was a need to become more cautious and restrict some of the parts of the development stage;
- As the majority of Formula 1 data is based on tables or comma-separated values files (.csv), it was not always possible for the ChatBot to get new information from those types of files. We were required to change our approach and create new PDFs filled with the previously tabled data;
- The chatbot required very specific instructions to ensure the correct outputs were obtained, which was an extremely time-consuming process (sort of trial and error);
- The data provided to feed the bot as big as it was, needs to go through a lot of embedding steps to get a smaller dimensionality which consumed a lot of the precious and small time existing to train the chatbot;

<a name="rep_desc"></a>
##
## Repository Description
This repository contains all the files created during the development of our project. In the following paragraphs will be a short description of how the repository is organized and what each file contains:
- [Prompts folder](Prompts): contains all the links that lead to the chats where the prompts were fed into the LLM (in our case, ChatGPT) to obtain - company definition (company name, problem, value proposition, core values, mission, vision, tag line, personas), marketing (discussion of pros and cons of reviews from competitor companies, blog posts creation, pitch script, 5-post social media campaign, Instagram post captions), timetable scheduling and patient data generator prompts.
- [No Show Prediction](No_show_prediction): this is a folder that contains two Jupyter notebooks, one containing the development of a predictive model for no-show appointments and another where the data needed for this task are properly treated.
- [Website](Website): this folder contains all the needed files for the chatbot application, on Streamlit, to work properly.
- [Prompt Template](Website/info_files/prompt_list.py):  this file contains the template prompts fed into the model (it is stored inside of info_files in the Website folder). 
- [Requirements](requirements.txt): file that specifies the dependencies and the versions that need to be installed in the environment for the project to be run.
- [Use Cases](use_cases.pdf): this file contains practical examples of scenarios in which our chatbot application can be helpful to clients of our company - appointment scheduling, appointment rescheduling, appointment cancellations, clarifying medical doubts, and predictive model.
- [Five Questions](five_questions.md): this file contains practical examples of questions that can be asked to our chatbot, in which it requires it to go retrieve the information to our text data (pdf file with the medicine information leaflets).
- [Data Description](data_description.txt): this text file contains the description and the metadata of all the used data in our project.
- [Git Ignore](.gitignore): this file specifies patterns of files and directories that should be excluded from the version control of our repository.
- [README](README.md): file that contains the basic instructions of how to run the project, the motivations behind it and its features.
- [LICENSE](LICENSE.md): this is a file that contains the chosen license for this project.

##
<a name="proj_use"></a>
## How To Use the Project. How to Install and Run the Project
Our project was divided into two main parts: informative website on WIX (https://docitrightcp.wixsite.com/doc-it-right) and the Streamlit app. Hence, the following steps need to be taken to ensure that the chatbot interface can be correctly accessed:
- Retrieve code from this GitHub Repository (`Fork` and then `Git Clone`)
- Download the folder (data.zip), sent by email, with the credentials (credentials to be able to use the Google Calendar platform) and tokens (contains authorization tokens used to authenticate and authorize access when declaring the specified scope). Please unzip this folder before moving on to the next step.
- Download the .env file (should be stored inside of the Capstone folder only), sent by email (which also contains our `API-key` - it is advisable to change to your own OpenAI API-key; the `DATA_PATH` should also be substituted to the local path of the data folder you just downloaded from the email. Please note that the end of the path should be `//`).
- Afterwards, inside the `No-show prediction` folder - in this GitHub repository, there is a need to change in both notebooks the path for your local path to the data (Please note that the end of the path should be `//`).
- There's also a need to run the requirements.txt file so that the environment is in the same conditions as the development environment was.

Finally, to run the Streamlit app: go inside the terminal, and open the [`Website`](Website) folder  (which is inside the capstone folder/repository). When that is done, run the following command `streamlit run main.py`.

<a name="chat_int"></a>
### How to interact with our chatbot
Our chatbot is capable of handling different formats of inputs. However, in order to obtain the most correct result the following structure of inputs shall be followed (the format presented will be "question that the chatbot will ask" | "your answer format"):
- Date | YYYY-MM-DD (e.g.: 2024-01-07)
- Time | HH:MM:SS (e.g.: 10:30:00)
- Email | Needs to be in email format, but other than that it does not have restrictions (e.g.: doc.it.right.cp@gmail.com)
- Doctor | The name needs to be correctly written - the names of the available doctors can be seen in the schedule tab of our chatbot application (e.g.: Dr. José Dias).
- Parking Spot | `Yes` or `No` answers only
- Special Requests | Either `No` or state any special request that you desire (e.g.: "I want a wheelchair")
- Payment in Advance | Integer Number between 0 and 100

The results of the predictive model for each appointment can be verified in the event scheduled in the clinic's calendar. Furthermore, they are also stored at Doc-IT-Right's database (along with the patient's personal information and the remaining appointment data).

Afterwards, you can have fun interacting with our Dr. Chatbot.

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
