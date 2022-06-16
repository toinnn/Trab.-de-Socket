from js import document
import js
from pyodide import to_js, create_proxy

pipe = document.querySelector(".pipe")
mario = document.querySelector(".mario")

def if_stop(pos , Pipe):
    if pos <= 120 and float(mario.style.bottom[:-2]) <= 70 and pos >= 0 :
        Pipe.style.animation = "none"
        Pipe.style.left = f"{pos}px"
def jump(entity):
    var =js.window.getComputedStyle( mario).bottom
    pyscript.write('msg',var[:-2])
    
    mario.style.bottom = f"{float(var[:-2]) + 80}px"
    
    var =js.window.getComputedStyle( mario).bottom
    pyscript.write('msg',var[:-2])

# mario.addEventListener("click" , create_proxy(jump) )

class game():
    def __init__(self) -> None:
        
        self.pipe = document.querySelector(".pipe")
        self.mario = document.querySelector(".mario")
        self.velocity = 0
        self.g = 50

    def gravity(self , ms = 1000) -> None :
        """ms == milisegundos entre cada step do loop de movimento """
        var =js.window.getComputedStyle( mario).bottom
        ms = ms/200

        if self.velocity >=0 :
            self.mario.style.bottom = f"{max(float(var[:-2]) - (self.velocity**2)/(2*self.g)*ms ,0 )}px"
        else :
            self.mario.style.bottom = f"{max(float(var[:-2]) + (self.velocity**2)/(2*self.g)*ms ,0 )}px"
        if float(js.window.getComputedStyle( mario).bottom[:-2]) > 0 :
            self.velocity += self.g*ms
        else :
            self.velocity = 0

    def jump(self , entity):
        var =js.window.getComputedStyle( mario).bottom
        pyscript.write('msg',var[:-2])
        
        # mario.style.bottom = f"{float(var[:-2]) + 80}px"
        
        var =js.window.getComputedStyle( mario).bottom
        pyscript.write('msg',var[:-2])
        self.velocity = -110


def main():
    # pyscript.write('msg', 'Hello world')

    mario_pos = mario.getBoundingClientRect()
    pipe_pos = pipe.getBoundingClientRect()
    jogo = game()
    
    js.setInterval(to_js(lambda : if_stop(pipe.offsetLeft , pipe)) , 1 )
    jump(mario)
    jump(mario)
    # js.setInterval(to_js(lambda : js.console.log( f"{mario.offsetLeft }")) , 50 )
    # js.setInterval(to_js(lambda : pyscript.write("msg" ,pipe.offsetLeft )) , 50 )

    mario.addEventListener("click" , create_proxy(jogo.jump) )
    js.setInterval(to_js(lambda : jogo.gravity(50 )) , 50 )
    
    # pipe.style.left = "250px"
    
    # js.setInterval(to_js(lambda : pyscript.write("msg" ,pipe_pos.left)) , 50 )
    
    
main()

print("Meu deus , meu senhor , me ajudaaa.. Por favor !!")

# while True:
#     main()
#     time.sleep(2)