# CanvasManager
Project for cs 8. Intended to help students manage workload and sort out there assignments/homework

Getting your api keys:

for canvas, log in to your canvas account and navigate to account settings and click new access token. Fill the purpose as canvas project and the expirey as never. This is the first api key the project needs

for openai, log into openai and head to the api apps. Under the user, find view api keys and generate a new one. this will be the second input

Installation (kind of jankey):
  
  For mac:
    cd into the documents folder on your computer in terminal by typing cd Documents
    create a venv by typing:
    python3 -m venv VENV_NAME(in this case canvasManager is a good example)
    source VENV_NAME/bin/activate
    type pip install openai
    type pip install canvasapi
    type deactivate
    
To use:
  making sure you are in the venv that you previously created(cd using cd Documents/canvasManager) and type venv/bin/python main.py
  To find the file of your assignemnts and their due dates, go into finder and navigate to Documents, then canvasManager and the file label gpt.txt is what you need
  
    
    
    
  
   

