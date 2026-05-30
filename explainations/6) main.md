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