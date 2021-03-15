# CS_338_ListenToMe

ListenToMe is a project developed for our CS_338 class at Northwestern. The main purpose of this project is to allow Zoom users to have the ability to control Zoom functionality using voice commands. This would provide more accessibility for impaired users, as well as more general ease-of-use for all users. It will also be useful for teachers and professors who have a difficult time navigating Zoom. Throughout a Zoom call, Listen to Me will use speech recognition as well as Natural Language Processing to listen for cues for when to execute a function. This allows not only for keyword-based commands (‘Zoom, share my screen’  → screen share), but also for more natural command flows (‘Now I’m going to share my screen’  → screen share). Some functions that users are able to execute using Listen to Me include:

* mute/unmute audio
* start/stop video
* share/unshare screen
* send message in text chat
* raise/lower hand
* leave meeting

## Setup/Installation

Open terminal, navigate to desired location, and clone the GitHub repository for CS_338_ListenToMe. Download requirements from requirements.txt*

*There may be an issue with the Pyaudio requirement (in 3.7), so you might have to create a Conda environment with python version 3.6. Instructions for that [here](https://stackoverflow.com/questions/48174935/conda-creating-a-virtual-environment).

Also, you must configure the terminal to control inputs. You can do this by going to System Preferences > Security and Privacy > Privacy > Accessibility > Allow Terminal


## Usage

Enter this command in appropriate directory to run the program:
```python
python basic.py
```

## Contributors 
Jeffrey Brewer, Felipe Caldeira, Rhea Ramaiya, Kathryne Tao
