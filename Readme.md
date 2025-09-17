# Quiz App


**Live version:** [click here](quiz-app-lake-gamma.vercel.app)


## Technologies
- **Frontend**: React, Bootstrap
- **Backend**: Python, Flask, Sqlite


## Run locally


#### Clone the repo
First of all you need [Git](https://git-scm.com/downloads) on your system to be able to clone 
the repository.

The following instructions assume that [Git](https://git-scm.com/downloads)\
is installed:

- Open your terminal
- navigate to the folder where you want to clone the repository
- clone the repository to your local machine by running:
```bash
git clone https://github.com/Romulad/quiz-app.git
```
- then navigate to the newly created directory to follow the next instructions:
```bash
  cd quiz-app
```


### By setting up the dev environment
To run this app locally make sure you have the following prerequisites on your system:
- [Node.js](https://nodejs.org/en/download/current), this include `npm` (Node Package Manager) will be used to run the [React app](https://react.dev) (Front-end). 
- [Python intepreter](https://www.python.org/downloads/), will be used to run the [Flask app](https://fastapi.tiangolo.com/) (API). 


#### Install dependencies and run the Flask app
In a terminal :
- Navigate to the `back-end` subdirectory under the project root directory:
```bash
  cd back-end
```
- Create a virtual environment:
```bash
  python -m venv venv
```
- Activate the virtual environment:
1. On windows
```bash
  .\venv\Scripts\activate
```
2. On macOS/Linux:
```bash
  source venv/bin/activate/
```
- Install the required packages:
```bash
  pip install -r requirements.txt
```
- once the installation is completed start the app with:
```bash
  flask --app app.server run
```
Next step to see the full app.


#### Install dependencies and run the front-end :
In a new terminal :
- Navigate to the `front-end` directory by running:
```bash
  cd front-end
```
- install the necessary packages by running this command:
```bash
  npm install
```
- once the installation is completed start the app with:
```bash
  npm start
```
  
And you're done! Visit `localhost:3000` to view the app.
