# Description

OverlyPieShaper is designed to filter traffic from Destiny 2 matchmaking. 
By creating a whitelist of SteamID64s, only traffic from those allowed individuals is allowed through.
If you're creative, there's a lot of potential uses for this kind of tool.

The <b><i>only</i></b> traffic being manipulated can be described by the below:

    [inbound/outboud] where [27000 <= UDP port <= 27200]

Inspiration for this project can be found in the references folder

# Environment Setup
## Windows

1. Clone the repo and cd into the root of it
2. Run the following commands:

    `python -m venv venv`
   
    `venv\Scripts\activate.bat`

    `pip3 install -r requirements.txt`
3. Verify everything is working by running the following:
    
    `python main.py`
    
    note: You'll see some output in a terminal and then the message "Now filtering"
4. Fire up the game and load into the tower. You should be alone.

# Packaging (building the .exe)
## Windows

1. Be in the root of the repo
2. Run the builder script: `build-exe.bat`
3. You'll now have a release folder containing "OverlyPieShaper.exe" and "steamids.txt"
4. (Optional) Zip the release folder and distribute

# Usage Instructions

1. Add the desired SteamID64s to "steamids.txt", following the format already present
2. Run `OverlyPieShaper.exe` while you need filtered matchmaking
3. Close the terminal window when finished