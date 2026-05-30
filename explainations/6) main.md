## The main backend file: which accepts the request from frontend, triggers the pipeline, gets the answer and sends back to the frontend.

### imports:
- as we use the fastapi as backend, we import that.
- now a import concept of fasatapi comes here, the pydantic, used for data validation.
    - this concept is like a bouncer for backend, which only allows specific format of things from the frontend.
    - how it works:
        - from pydantic we import base model, which acts as a bouncer for us.
        - we then customize add whatever things we want to have some rule to enter, we initialize that.
        - as we needed prompt to be strictly a string, we used that.
        - later we point our request to the class, so that the request comes thorough the class for verification. 

- import the generate answer function from the rag_pipeline.py.

### fastapi app initialization:
- we initialize the app and give it a title

### pydantic class:
- this can also called schema.
- we create data validation for prompt (query) to be a string.
- when interviewer asks, how did you validate you data, you can say, i used the pydantic model to validate my data coming from the frontend, as i only send query from the frontend, i strictly gave it to be string.

### endpoint.
- if you have a bit of knowledge about fastapi, you would know what a endpoint is. in simple words is a room in a building, which has some specific work to do.
- as the frontend is requesting some output from the backend, we use the post method (another main concept of fastapi), and keep the endpoint as chat.
- create the function which takes request from the frontend.
- as the request contains some prompt, which is the query, we send that to the generate_answer function, which is inside the rag_pipeline script. result variable stores the answer given by the function, and finally we get the result and store that inside a dictionary as a value for the key answer. later this is picked up by the frontend.

### flow:

```text
frontend sends request
        |
        v
request hits the chat endpoint
        |
        V
the request goes through the pydantic class to get verified
        |
        v
generate answer function is triggered and the result of it is stored inside teh result variable.
        |
        v
result is packed inside a dictionary to get picked by frontend
```