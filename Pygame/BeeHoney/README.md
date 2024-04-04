## <span style="color:#0070c0">03 - Desenvolvendo BeeHoney - POO</span>

<img src="https://github.com/alexandre-ferreira-1986/Python_learning/blob/main/Pygame/BeeHoney/assets/print_beehoney.png" 
     width="150" 
     height="300" />

### 02 - Criando um Obj mais inteligente

- Nós criamos o  "self.group": Recebe uma forma de armazenar um objeto. Cada grupo pode ter diversos elementos nele.
- O Sprite vai dizer a qual grupo cada elemento pertence. Por exemplo uma bola, pertence ao grupo bola. Uma abelha pertence ao grupo das abelhas
- a função no "self.group.draw()", já pertence ao group. Agora não precisaremos chamar o window.blit
- Com essa parte de group e sprite conseguimos ter muito mais controle sobre os objetos.
---
- Group
	- "pygame.sprite.group" is a container class provided by Pygame for holding and manageing mutiple sprites;
	- It provide methods for efficiently updating and drawing all the sprites it contains.
	- Using groups helps in organizing sprites, especially when you have many sprites that need similar oprations.
- Sprite
	- "self.sprite.Sprite" is a base class for visible game objects in Pygame
	- You can create custom sprite classes by subclassing "pygame.sprite.Sprite" and adding attributes and methods specific to you game objects.
- ---
- Overall, 'Group" and "Sprite" provide a convenient way to manage and draw multiple sprites efficiently in a Pygame-based game.

```python
import pygame  
  
  
class Obj:  
  
    def __init__(self, image, x, y):  
  
        self.group = pygame.sprite.Group()  
        self.sprite = pygame.sprite.Sprite(self.group)  
  
        self.sprite.image = pygame.image.load(image)  
        self.sprite.rect = self.sprite.image.get_rect()  
        self.sprite.rect[0] = x  
        self.sprite.rect[1] = y  
  
    def drawing(self, window):  
        self.group.draw(window)
```



### 03 - Adicionando uma tela de Start Game

- Inserindo a tela de inicio no programa

```python
class Main:  
  
    def __init__(self, sizex, sizey, title):  
  
        self.window = pygame.display.set_mode([sizex, sizey])  
        self.title = pygame.display.set_caption(title)  
  
        self.loop = True  
  
        self.start_screen = Obj("assets/start.png", 0, 0)  
  
    def draw(self):  
        self.start_screen.drawing(self.window)
```



### 04 - Criando a cena Menu

- Antes nós só fizemos um teste, e vamos agora apagar o que estava no drawing

```python
class Main:  
  
    def __init__(self, sizex, sizey, title):  
  
        self.window = pygame.display.set_mode([sizex, sizey])  
        self.title = pygame.display.set_caption(title)  
  
        self.loop = True  
  
  
    def draw(self):  
        pass
```

- Criar um novo arquivo Menu.py

	- Neste arquivo primeiro vamos chamar a tela inicial
	- Depois criamos o evento, para identificar quando apertarmos a tecla ENTER

```python
import pygame  
from obj import Obj  
  
class Menu:  
  
    def __init__(self):  
  
        self.bg = Obj("assets/start.png", 0, 0)  
        self.change_scene = False  
  
    def draw(self, window):  
        self.bg.group.draw(window)  
  
    def events(self, event):  
        if event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_RETURN:  
                self.change_scene = True
```

- No Main realizamos as alterações:

```python
class Main:  
  
    def __init__(self, sizex, sizey, title):  
  
        self.window = pygame.display.set_mode([sizex, sizey])  
        self.title = pygame.display.set_caption(title)  
  
        self.loop = True  
  
        self.menu = Menu()  
  
    def draw(self):  
	    if not self.menu.change_scene:  
	        self.menu.draw(self.window)  
  
    def events(self):  
        for events in pygame.event.get():  
            if events.type == pygame.QUIT:  
                self.loop = False  
            self.menu.events(events)
```



### 05 - Criando a cena

- Criando um novo arquivo chamado game.py
- Criar um Background do jogo

```python
from obj import Obj  
  
class Game:  
  
    def __init__(self):  
  
        self.bg = Obj("assets/bg.png", 0, 0)  
  
        self.change_scene = False  
  
    def draw(self, window):  
        self.bg.drawing(window)  
  
    def update(self):  
        pass
```

- main

```python
import pygame  
from obj import Obj  
from menu import Menu  
from game import Game  
  
class Main:  
  
    def __init__(self, sizex, sizey, title):  
  
        self.window = pygame.display.set_mode([sizex, sizey])  
        self.title = pygame.display.set_caption(title)  
  
        self.loop = True  
  
        self.menu = Menu()  
        self.game = Game()  
  
    def draw(self):  
        if not self.menu.change_scene:  
            self.menu.draw(self.window)  
        elif not self.game.change_scene:  
            self.game.draw(self.window)  
            self.game.update()
```

- Passando a impressão de um fundo infinito

```python
from obj import Obj  
  
class Game:  
  
    def __init__(self):  
  
        self.bg = Obj("assets/bg.png", 0, 0)  
        self.bg2 = Obj("assets/bg.png", 0, -640)  
  
        self.change_scene = False  
  
    def draw(self, window):  
        self.bg.drawing(window)  
        self.bg2.drawing(window)  
  
    def update(self):  
        self.bg.sprite.rect[1] += 1  
        self.bg2.sprite.rect[1] += 1  
  
        if self.bg.sprite.rect[1] >= 640:  
            self.bg.sprite.rect[1] = 0  
  
        if self.bg2.sprite.rect[1] >= 0:  
            self.bg2.sprite.rect[1] = -640
            
```



### 06 - Adicionando aranhas a cena

- Agora o Obj vai se tornar mais inteligente.
	- Além de desenhar na tela,
	- Passar as posições
	- Armazenar uma imagem
	- E transformar o objeto num grupo
- Agora vai realizar animações quando necessário

- Primeiro será criada uma variável para controlar a taxa de frame da tela ("self.frame")

```python
import pygame   
  
class Obj:  
  
    def __init__(self, image, x, y):  
  
        self.group = pygame.sprite.Group()  
        self.sprite = pygame.sprite.Sprite(self.group)  
  
        self.sprite.image = pygame.image.load(image)  
        self.sprite.rect = self.sprite.image.get_rect()  
        self.sprite.rect[0] = x  
        self.sprite.rect[1] = y  

		#Cria o frame
        self.frame = 1  
  
    def drawing(self, window):  
        self.group.draw(window)  
  
    def anim(self):  
        self.frame += 1  
        if self.frame > 4:  
            self.frame = 1  
  
		self.sprite.image = pygame.image.load(f"assets/spider{str(self.frame)}.png")
```

- game

```python
from obj import Obj  
  
class Game:  
  
    def __init__(self):  
  
        self.bg = Obj("assets/bg.png", 0, 0)  
        self.bg2 = Obj("assets/bg.png", 0, -640)  
  
        self.spider = Obj("assets/spider1.png", 200,200)  
  
        self.change_scene = False  
  
    def draw(self, window):  
        self.bg.drawing(window)  
        self.bg2.drawing(window)  
        self.spider.drawing(window)  
  
    def update(self):  
        self.move_bg()  
        self.spider.anim()  
  
    def move_bg(self):  
        self.bg.sprite.rect[1] += 1  
        self.bg2.sprite.rect[1] += 1  
  
        if self.bg.sprite.rect[1] >= 640:  
            self.bg.sprite.rect[1] = 0  
  
        if self.bg2.sprite.rect[1] >= 0:  
            self.bg2.sprite.rect[1] = -640
```



### 07 - Controle de FPS

```python
import pygame  
from obj import Obj  
from menu import Menu  
from game import Game  
  
class Main:  
  
    def __init__(self, sizex, sizey, title):  
  
        self.window = pygame.display.set_mode([sizex, sizey])  
        self.title = pygame.display.set_caption(title)  
  
        self.loop = True  
  
        self.menu = Menu()  
        self.game = Game()  

		# CRIADA A FPS
        self.fps = pygame.time.Clock()  
  
    def draw(self):  
        if not self.menu.change_scene:  
            self.menu.draw(self.window)  
        elif not self.game.change_scene:  
            self.game.draw(self.window)  
            self.game.update()  
  
    def events(self):  
        for events in pygame.event.get():  
            if events.type == pygame.QUIT:  
                self.loop = False  
            self.menu.events(events)  
  
    def update(self):  
        while self.loop:  
	        # CADA SEGUNDO SÃO 30 FPS
            self.fps.tick(30)  
            self.draw()  
            self.events()  
            pygame.display.update()  
  
  
game = Main(360, 640, "BeeHoney")  
game.update()
```

OBJ

```PYTHON
import pygame  
  
  
class Obj:  
  
    def __init__(self, image, x, y):  
  
        self.group = pygame.sprite.Group()  
        self.sprite = pygame.sprite.Sprite(self.group)  
  
        self.sprite.image = pygame.image.load(image)  
        self.sprite.rect = self.sprite.image.get_rect()  
        self.sprite.rect[0] = x  
        self.sprite.rect[1] = y  
  
        self.frame = 1
        # PADRONIZA O VALOR DO TICK  
        self.tick = 0  
  
    def drawing(self, window):  
        self.group.draw(window)  
  
    def anim(self):
	    # INCREMENTA O FRAME A PARTIR DO TICK
	    # PODE VARIA O VALOR DO TICK CONFORME ACHAR MELHOR
        self.tick += 1  
        if self.tick >= 3:  
            self.tick = 0  
            self.frame += 1  
  
        if self.frame > 4:  
            self.frame = 1  
  
        self.sprite.image = pygame.image.load(f"assets/spider{str(self.frame)}.png")
```


### 08 - Gerando movimento das aranhas

- Cria o move_spider() no game.py

```python
def move_spiders(self):  
    self.spider.prite.rect[1] += 10
```

- Chama a função no update.

```python
def update(self):  
    self.move_bg()  
    self.spider.anim()  
    self.move_spiders()
```

- Com essa adaptação a aranha já começa a descer, porém temos que ao sair da tela eliminar a mesma

```python
def move_spiders(self):  
    self.spider.sprite.rect[1] += 10  
  
    if self.spider.sprite.rect[1] >= 700:  
        self.spider.sprite.kill()
```

- Agora vamos acrescentar outra aranha na tela, quando a outra "morrer". Faremos de maneira aleatória. Podemos alterar também a inicialização para ser aleatória. Da mesma maneira. Alterando a função __init__.

```python
import random

def __init__(self):  
  
    self.bg = Obj("assets/bg.png", 0, 0)  
    self.bg2 = Obj("assets/bg.png", 0, -640)  
  
    self.spider = Obj("assets/spider1.png", random.randrange(0,300), -50)

def move_spiders(self):  
    self.spider.sprite.rect[1] += 10  

    if self.spider.sprite.rect[1] >= 500:  
        self.spider.sprite.kill()  
        self.spider = Obj("assets/spider1.png", random.randrange(0, 300), -50)
```

### 09 - Adicionando a Flor a cena

```python
def __init__(self):  
  
	self.bg = Obj("assets/bg.png", 0, 0)  
	self.bg2 = Obj("assets/bg.png", 0, -640)  
	  
	self.spider = Obj("assets/spider1.png", random.randrange(0,300),-50)  
	self.flower = Obj("assets/florwer1.png", random.randrange(0,300),-50)

def draw(self, window):  
    self.bg.drawing(window)  
    self.bg2.drawing(window)  
    self.spider.drawing(window)  
    self.flower.drawing(window)

def update(self):  
    self.move_bg()  
    self.spider.anim()  
    self.move_spiders()  
    self.move_flower()

def move_flower(self):  
    self.flower.sprite.rect[1] += 6  
  
    if self.flower.sprite.rect[1] >= 700:  
        self.flower.sprite.kill()  
        self.flower = Obj("assets/florwer1.png", random.randrange(0, 300), -50)
```

### 10 - Sistema de animação melhorado

- No obj.py vamos alterar a animação para tornar mais personalizada

```python
def anim(self, image, tick, frames):  
    self.tick += 1  
  
    if self.tick >= tick:  
        self.tick = 0  
        self.frame += 1  
  
    if self.frame > frames:  
        self.frame = 1  
  
    self.sprite.image = pygame.image.load(f"assets/{image}{str(self.frame)}.png")
```

- Definir essas ações no game.py

```python
def update(self):  
    self.move_bg()  
    self.spider.anim("spider", 8, 4)  
    self.flower.anim("florwer", 8, 2)  
    self.move_spiders()  
    self.move_flower()
```

### 11 - Adicionando a abelha a cena

- Criaremos uma nova classe que herda a outra classe. No obj.py
- Nesta classe, iremos associar o movimento da abelha ao movimento do mouse
- Os ajustes de -35 e -30, são para centralizar o mouse. Fazem parte apenas do final. Quando mexemos no main.py, abaixo. Inseri aqui para facilitar.

```python
class Bee(Obj):  
  
    def __init__(self, image, x, y):  
        super().__init__(image, x, y)  
  
    def move_bee(self, event):  
        if event.type == pygame.MOUSEMOTION:  
            self.sprite.rect[0] = pygame.mouse.get_pos()[0] - 35
            self.sprite.rect[1] = pygame.mouse.get_pos()[1] - 30
```

- agora vamos inserir no game.py

```python
from obj import Obj, Bee

class Game:  
  
    def __init__(self):  
  
        self.bg = Obj("assets/bg.png", 0, 0)  
        self.bg2 = Obj("assets/bg.png", 0, -640)  
  
        self.spider = Obj("assets/spider1.png", random.randrange(0,300),-50)  
        self.flower = Obj("assets/florwer1.png", random.randrange(0,300),-50)  
        self.bee = Bee("assets/bee1.png", 150, 600)

	def draw(self, window):  
	    self.bg.drawing(window)  
	    self.bg2.drawing(window)  
	    self.bee.drawing(window)  
	    self.spider.drawing(window)  
	    self.flower.drawing(window)

	def update(self):  
	    self.move_bg()  
	    self.spider.anim("spider", 8, 4)  
	    self.flower.anim("florwer", 8, 2)  
	    self.bee.anim("bee", 8, 4)  
	    self.move_spiders()  
	    self.move_flower()


```

- Para ela seguir o mouse, vamos no main.py.
- Neste momento foram inseridos os ajustes de -35 e -30 na parte inicial.

```python
def events(self):  
    for events in pygame.event.get():  
        if events.type == pygame.QUIT:  
            self.loop = False  
        self.menu.events(events)  
        self.game.bee.move_bee(events)
```

### 12 - Adicionando colisões

- Ajustando movimento das asas

```python
def update(self):  
    self.move_bg()  
    self.spider.anim("spider", 8, 4)  
    self.flower.anim("florwer", 8, 2)  
    self.bee.anim("bee", 2, 4)  
    self.move_spiders()  
    self.move_flower()
```

- Agora a colisão da Bee. 
- Para fins de teste criamos primeiro uma versão que printa quando batemos

```python
class Bee(Obj):  
  
    def __init__(self, image, x, y):  
        super().__init__(image, x, y)  
  
    def move_bee(self, event):  
        if event.type == pygame.MOUSEMOTION:  
            self.sprite.rect[0] = pygame.mouse.get_pos()[0] - 35  
            self.sprite.rect[1] = pygame.mouse.get_pos()[1] - 30  
  
    def colision(self, group, name):  
  
        name = name  
        colison = pygame.sprite.spritecollide(self.sprite, group, True)  
  
        if name == "Flower" and colison:  
            print("Flower")  
        elif name == "Spider" and colison:  
            print("Spider")
```

- No Game alteramos o update

```python
def update(self):  
    self.move_bg()  
    self.spider.anim("spider", 8, 4)  
    self.flower.anim("florwer", 8, 2)  
    self.bee.anim("bee", 2, 4)  
    self.move_spiders()  
    self.move_flower()  
    self.bee.colision(self.spider.group, "Spider")  
    self.bee.colision(self.flower.group, "Flower")
```

### 13 - Sistema de GameOver

- Agora vamos criar um sistema de pontos e registrar a quantidade de vidas iniciais.

```python
class Bee(Obj):  
  
    def __init__(self, image, x, y):  
        super().__init__(image, x, y)  
  
        self.life = 3  
        self.pts = 0  
  
    def move_bee(self, event):  
        if event.type == pygame.MOUSEMOTION:  
            self.sprite.rect[0] = pygame.mouse.get_pos()[0] - 35  
            self.sprite.rect[1] = pygame.mouse.get_pos()[1] - 30  
  
    def colision(self, group, name):  
  
        name = name  
        colison = pygame.sprite.spritecollide(self.sprite, group, True)  
  
        if name == "Flower" and colison:  
            self.pts += 1  
        elif name == "Spider" and colison:  
            self.life -= 1
```

- No Game.py, vamos definir o fim do jogo

```python
def gameover(self):  
    if self.life <= 0:  
        self.change_scene = True

def update(self):  
    self.move_bg()  
    self.spider.anim("spider", 8, 4)  
    self.flower.anim("florwer", 8, 2)  
    self.bee.anim("bee", 2, 4)  
    self.move_spiders()  
    self.move_flower()  
    self.bee.colision(self.spider.group, "Spider")  
    self.bee.colision(self.flower.group, "Flower")  
    self.gameover()
```

- No Main.py

```python
def draw(self):  
    if not self.menu.change_scene:  
        self.menu.draw(self.window)  
    elif not self.game.change_scene:  
        self.game.draw(self.window)  
        self.game.update()  
  
def events(self):  
    for events in pygame.event.get():  
        if events.type == pygame.QUIT:  
            self.loop = False  
        if not self.menu.change_scene:  
            self.menu.events(events)  
        elif not self.game.change_scene:  
            self.game.bee.move_bee(events)
```

### 14 - Criando a cena de game over

- No Menu, vamos criar a classe gameover

```python
class Menu:  
  
    def __init__(self, image):  
  
        self.bg = Obj(image, 0, 0)  
        self.change_scene = False  
  
    def draw(self, window):  
        self.bg.group.draw(window)  
  
    def events(self, event):  
        if event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_RETURN:  
                self.change_scene = True  
  
class GameOver(Menu):  
  
    def __init__(self, image):  
        super().__init__(image)
```

- Agora vamos alterar o menu principal (Main)

```python
from menu import Menu, GameOver

def __init__(self, sizex, sizey, title):  
  
    self.window = pygame.display.set_mode([sizex, sizey])  
    self.title = pygame.display.set_caption(title)  
  
    self.loop = True  
  
    self.menu = Menu("assets/start.png")  
    self.game = Game()  
    self.gameover = GameOver("assets/gameover.png")  
  
    self.fps = pygame.time.Clock()

ef draw(self):  
    if not self.menu.change_scene:  
        self.menu.draw(self.window)  
    elif not self.game.change_scene:  
        self.game.draw(self.window)  
        self.game.update()  
    elif not self.gameover.change_scene:  
        self.gameover.draw(self.window)  
    else:
	    # Retornando todos os Status para False  
        self.menu.change_scene = False  
        self.game.change_scene = False  
        self.gameover.change_scene = False
        self.game.bee.life = 3  
		self.game.bee.pts = 0

def events(self):  
    for events in pygame.event.get():  
        if events.type == pygame.QUIT:  
            self.loop = False  
        if not self.menu.change_scene:  
            self.menu.events(events)  
        elif not self.game.change_scene:  
            self.game.bee.move_bee(events)  
        else:  
            self.gameover.event(events)
```

### 15  - Adicionando textos a cena

- No Obj.py, vamos criar a classe de texto

```python
class Text:  
  
    def __init__(self, size, text):  
  
        self.font = pygame.font.SysFont("Arial bold", size)  
        self.render = self.font.render(text, True, (255,255,255))  
  
    def draw(self, window, x, y):  
        window.blit(self.render, (x,y))
```

- Agora vamos chamar no Game

```python
from obj import Obj, Bee, Text

def __init__(self):  
  
    self.bg = Obj("assets/bg.png", 0, 0)  
    self.bg2 = Obj("assets/bg.png", 0, -640)  
  
    self.spider = Obj("assets/spider1.png", random.randrange(0,300),-50)  
    self.flower = Obj("assets/florwer1.png", random.randrange(0,300),-50)  
    self.bee = Bee("assets/bee1.png", 150, 600)  
  
    self.change_scene = False  
  
    self.score = Text(120, "0")  
    self.lifes = Text(60, "3")  
  
def draw(self, window):  
    self.bg.drawing(window)  
    self.bg2.drawing(window)  
    self.bee.drawing(window)  
    self.spider.drawing(window)  
    self.flower.drawing(window)  
    self.score.drawing(window, 160, 50)  
    self.lifes.drawing(window, 50, 50)


```

### 16 - Atualizando Textos

- Atualiza o Obj

```python
class Text:  
  
    def __init__(self, size, text):  
  
        self.font = pygame.font.SysFont("Arial bold", size)  
        self.render = self.font.render(text, True, (255,255,255))  
  
    def draw(self, window, x, y):  
        window.blit(self.render, (x,y))  
  
    def update_text(self, text_update):  
        self.render = self.font.render(text_update, True, (255, 255, 255))
```

- Atualiza o Game

```python
def update(self):  
    self.move_bg()  
    self.spider.anim("spider", 4, 4)  
    self.flower.anim("florwer", 7, 2)  
    self.bee.anim("bee", 2, 4)  
    self.move_spiders()  
    self.move_flower()  
    self.bee.colision(self.spider.group, "Spider")  
    self.bee.colision(self.flower.group, "Flower")  
    self.gameover()
    
```

### 17 - Adicionando Som

- Inicializar no Main

- Som de fundo

```python
class Main:  
  
    def __init__(self, sizex, sizey, title):  
  
        pygame.init()  
        pygame.font.init()  
  
        pygame.mixer.init()  
        pygame.mixer.music.load("assets/sounds/bg.ogg")  
        pygame.mixer.music.play(-1)
```

- Som das colisões

```python
class Bee(Obj):  
  
    def __init__(self, image, x, y):  
        super().__init__(image, x, y)  
  
        pygame.mixer.init()  
        self.sound_pts = pygame.mixer.Sound("assets/sounds/score.ogg")  
        self.sound_block = pygame.mixer.Sound("assets/sounds/bateu.ogg")  
  
        self.life = 3  
        self.pts = 0  
  
    def move_bee(self, event):  
        if event.type == pygame.MOUSEMOTION:  
            self.sprite.rect[0] = pygame.mouse.get_pos()[0] - 35  
            self.sprite.rect[1] = pygame.mouse.get_pos()[1] - 30  
  
    def colision(self, group, name):  
  
        name = name  
        colison = pygame.sprite.spritecollide(self.sprite, group, True)  
  
        if name == "Flower" and colison:  
            self.pts += 1  
            self.sound_pts.play()  
        elif name == "Spider" and colison:  
            self.life -= 1  
            self.sound_block.play()
```
