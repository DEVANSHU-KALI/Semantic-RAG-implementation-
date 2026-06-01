## The front end part of the project

### imports
- Streamlit framework is a great framework for building front end Because here you donate to write some HTML or CSS codes or separately, you simply get a simple front end design where you can add elements using that framework related things like using that dot ST or that spinner text input elements all these things are simply possible using this stream with front end and it's your choice to use this I recommend this because it's simpler than building a HTML and CSS page
- We are using Fast API as a back end We import the request module from Python request something from the back end which will be understandable when you see the code below

### api url
- The local of sport mentioned there is actually the back end port which has that chat endpoint and we are hitting that using this API URL.

### box to enter query
- That st.text_input function creates a simple box which can take your query.

### if function and its inner part.
- We are simply starting an if function there which checks whether there is query in the input box or not, And if yes it runs it's below code.
- Now the line which you are seeing there like st.spinner simply means that you're getting a spinner element in your front end which spins until the answer is retrieved from your back end. 
- Now here comes the concept of serialization and deserialization in the frontend part. We are creating a payload which contains a query inside a dictionary and this will be to the back end by converting that into a jason string in the next line.
- line 17:
    - requests.post: a method do send some data to the backend and get some data back again, here its the response.
    - we give the url there to let it connect to that url and send data to that url, where the backend lives.
    - the next part is called serialization, you are taking you data which is in the dict format and converting that into a json string to send through the internet.
- a simple if and else block
    - if the status code = 200, which means ok in the terms of web tech.
    - deserialization here, the response from the backend gets deserialized here using that .json() function.
    - get the data and write it down in the frontend.
    - else block, any error, return it.

- forgot to mention that, this small part of the code is inside the try block which ends with the except block again.