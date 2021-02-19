# Next Word Predictor
It's Harry Potter and the Repo of terrible models! I didn't know what to call the project so I just named it U lol. This application uses the Tensorflow Universal Sentence Encoder and a Dense Neural Network to predict the next word of a phrase. I trained it using the text from Harry Potter and the Philosopher's Stone [URL to source here](https://github.com/formcept/whiteboard/blob/master/nbviewer/notebooks/data/harrypotter/Book%201%20-%20The%20Philosopher's%20Stone.txt) by breaking the text into ngrams of various sizes. To preprocess the text, I removed punctuation and then used ScraPy to tokenize the text.

To make the software more accessible, I hosted it on a simple Rest API Flask server and also wrote (more like speedran) a React application.
I tried hosting on Heroku but couldn't get it to work because the model is too large.

Model: [Google drive link](https://drive.google.com/file/d/1q22zTA4T0v0WcjAMbVTmA35cDirsUJ52/view?usp=sharing)
To run:
1. Pull repo
2. Install Node.js
3. Open virtual environment
4. pip install -r requirements.txt
5. Download model and unzip it to root folder of project
6. Run the backend server with the command: ``` python server.py ```
7. Using a different terminal, enter into the frontend directory with: ``` cd predictor-app ```
8. Run ``` npm install ```
9. Start the application with ``` npm start ```
10. Test the model with the input box

### Sample keywords for the model:
Harry Potter,
One day,
Dumbledore
