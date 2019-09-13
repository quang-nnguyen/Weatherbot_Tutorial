# Weatherbot Tutorial (using the latest release of Rasa NLU and Rasa Core)

Forked from https://github.com/JustinaPetr/Weatherbot_Tutorial

### Install

Install the requirements.

Note: rasa version 1.0.9 is mandatory, newer version of rasa won't work.

```pip install -r requirements.txt```

Download and link spaCy's language model.

```python -m spacy download en_core_web_md```

```python -m spacy link en_core_web_md en```

### Training the NLU model

Since the release of Rasa 1.0, the training of the NLU models became a lot easier with the new CLI. Train the model by running:  

```rasa train nlu ```

Once the model is trained, test the model:

```rasa shell nlu```


### Training the dialogue model

The biggest change in how Rasa Core model works is that custom action 'action_weather' now needs to run on a separate server. That server has to be configured in a 'endpoints.yml' file.  This is how to train and run the dialogue management model:  
1. Start the custom action server by running:  

``` rasa run actions```  

Tips: add argument `--vv` for debug mode

``` rasa run -vv actions```

2. Open a new terminal and train the Rasa Core model by running:  

``` rasa train```  
 
3. Talk to the chatbot once it's loaded after running:  
```rasa shell```  


### Starting the interactive training session:

To run your assistant in a interactive learning session, run:
1. Make sure the custom actions server is running:  

```rasa run actions```  

2. Start the interactive training session by running:  

```rasa interactive```  


Latest code update: 13/09/2019

Latest compatible Rasa NLU version: 1.0.9





