from hello import hello 
import gradio

print("TESTING")

io = gradio.Interface(fn=hello, inputs='text', outputs='text', verbose=True, title='Hello World', 
    description='Hello World Description', thumbnail='https://github.com/gradio-app/gradio_static/blob/master/static/img/logo.png?raw=true', analytics_enabled=False)

io.launch(debug=True)
