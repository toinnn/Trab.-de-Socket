from js import document
import js
from pyodide import to_js

def if_stop(pos , Pipe):
    if pos <= 120 :
        Pipe.style.animation = "none"
        Pipe.style.left = f"{pos}px"

def main():
    # pyscript.write('msg', 'Hello world')
    pipe = document.querySelector(".pipe")
    mario = document.querySelector(".mario")
    mario_pos = mario.getBoundingClientRect()
    pipe_pos = pipe.getBoundingClientRect()
    pyscript.write('msg', pipe.offsetLeft)
    js.setInterval(to_js(lambda : if_stop(pipe.offsetLeft , pipe)) , 1 )
    js.setInterval(to_js(lambda : js.console.log( f"{mario.offsetLeft }")) , 50 )
    js.setInterval(to_js(lambda : pyscript.write("msg" ,pipe.offsetLeft )) , 50 )
    # pipe.style.left = "250px"
    
    # js.setInterval(to_js(lambda : pyscript.write("msg" ,pipe_pos.left)) , 50 )
    # msg = document.getElementById("msg")
    # msg.innerHTML = 'Hello world___'
    
main()

print("Meu deus , meu senhor , me ajudaaa.. Por favor !!")

# while True:
#     main()
#     time.sleep(2)