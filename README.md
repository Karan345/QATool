# Text QATool
1. A Python script that reads a text file (named data.txt)
2. Summarizes and lets you ask questions just in that context window
3. Used the Gemma 3 (1B) model (You can use your own) (Ref : https://ai.google.dev/gemma/docs/core)
4. Runs locally on machine
5. Built with help from Gemini (Chat)

# Prerequisites 
1. Engine  : Ollama 
2. Model   : Gemma3:1b
   Why? 
    Size    	     :  1 Billion parameters (the smallest in the Gemma 3 family), needed a light one to start with and we are only summarizing txt files 
    Input Type     :  Text-only 
    Context Window :	Supports a large context window of 32K tokens. 
    Local Requirements	Requires at least 2GB of RAM and runs efficiently on CPU or GPU. The quantized version (INT4/Ollama) requires about 1.59 GB of VRAM.
3. Language : Python
4. Hardware : Not a very high end laptop, Linux-based (details later)

# How to run
1. Got to https://ollama.com/ to install ollama (choose Linux/Win/Mac)
2. Pull your model : ollama pull gemma3:1b
3. Install Ollama Python library :  pip install ollama (Disclaimer : you can try a venv to install, I used the --break-system-packages)
4. Create a file named data.txt in the same folder. Paste some text into it (e.g., a news article, a recipe, or a short story)
5. The local_chat.py script has the code, it reads the text file, passes it to the model (be sure to use the one you want and update accordingly) and loops like a chat
6. Run the python script in the cli. python3 local_chat.py 

# Advantages :
1. Quick Learning Project
2. Can chat with the model in the cmd line
3. Sticks to your source

# Limitations:
1. Limited context can give confusing answers
2. Only reads txt files have to copy paste

# Possible improvements :
1. Read PDFs to expand context and also no need to copy
