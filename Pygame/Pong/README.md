# Step by Step

![image](https://github.com/alexandre-ferreira-1986/Python_learning/blob/main/Pygame/Pong/assets/final_program.png)

## <span style="color:#0070c0">Introduction to  pygame - Pong</span>


1. Creating a Window

```python
window = pygame.display.set_mode(1280,720)
title = pygame.display.set_caption("Pong")
```

2. Keeping the window open

```python
loop = True  
while loop:  
	# Check all events
    for events in pygame.event.get():  
	    # if you call close window
        if events.type == pygame.QUIT:  
            loop = False  
	pygame.display.update()
```

3. Add an image

```python
# Load the image
field = pygame.image.load("assets/field.png")
# Call the image and positioning it
window.blit(field, (0,0))
```

4. Adding Players

```python
# Add Player 1
player1 = pygame.image.load("assets/player1.png")  
window.blit(player1, (50, 310))  

# Add Player 2
player2 = pygame.image.load("assets/player2.png")  
window.blit(player2, (1150, 310))  

# Add Ball
ball = pygame.image.load("assets/ball.png")  
window.blit(ball, (617,337))

```

5. Moving the Ball

- <span style="color:#9c9c9c">Foi criada uma função move_ball, para mover a bolinha, que ainda não está realizando a tarefa completamente</span>
- <span style="color:#9c9c9c">Foi criada uma função draw()  para inserir os elementos (anteriormente estavamos desenhando logo depois de criar)</span>
- <span style="color:#9c9c9c">Chamamos as 2 funções dentro do While.</span>
- <span style="color:#9c9c9c">Criamos as variáveis ball_x e ball_y, assim conseguimos iterar nessas posições.</span>

```python
ball_x = 617  
ball_y = 337  
  
def move_ball():  
    global ball_x  
    global ball_y  
  
    ball_x += 1  
  
def draw():  
    window.blit(field, (0, 0))  
    window.blit(player1, (50, 310))  
    window.blit(player2, (1150, 310))  
    window.blit(ball, (ball_x, ball_y))  
  
loop = True  
while loop:  
    for events in pygame.event.get():  
        if events.type == pygame.QUIT:  
            loop = False  
  
    draw()  
    move_ball()  
    pygame.display.update()
```

6. Movements to  Player 01

```python
player1_y = 310

loop = True  
while loop:  
    for events in pygame.event.get():  
        if events.type == pygame.QUIT:  
            loop = False
        # Up - press W, Down - press S  
        if events.type == pygame.KEYDOWN:  
            if events.key == pygame.K_w:  
                player1_y -= 10  
            if events.key == pygame.K_s:  
                player1_y += 10  
    draw()  
    move_ball()  
    pygame.display.update()

```

7. Improving movements from Player 01

- Criou-se a função move_player() para mover o player para cima ou para baixo dependendo da condição de verdadeiro ou falso
- A condição vai ser alterada dentro do While.
	- Sendo que se pressionar a tecla, a condição se torna verdadeira (KEYDOWN)
	- Se soltar a tecla, a variável se torna falsa (KEYUP)

```python
player1_moveup = False  
player1_movedown = False

def move_player():  
    global player1_y  
  
    if player1_moveup:  
        player1_y -= 5  
    else:  
        player1_y += 0  
  
    if player1_movedown:  
        player1_y += 5  
    else:  
        player1_y += 0

loop = True  
while loop:  
    for events in pygame.event.get():  
        if events.type == pygame.QUIT:  
            loop = False  
        if events.type == pygame.KEYDOWN:  
            if events.key == pygame.K_w:  
                player1_moveup = True  
            if events.key == pygame.K_s:  
                player1_movedown = True  
        if events.type == pygame.KEYUP:  
            if events.key == pygame.K_w:  
                player1_moveup = False  
            if events.key == pygame.K_s:  
                player1_movedown = False  
    draw()  
    move_ball()  
    move_player()  
    pygame.display.update()
```

8. Defining limits to the Player

- Tem que checar os limites da tela certinho, pode colocar para imprimir se for o caso a posição. No caso deste programa, os limites foram 0 e 575

```python
def move_player():  
    global player1_y  
  
    if player1_moveup:  
        player1_y -= 5  
    else:  
        player1_y += 0  
  
    if player1_movedown:  
        player1_y += 5  
    else:  
        player1_y += 0  
  
    if player1_y <= 0:  
        player1_y = 0  
    elif player1_y >= 575:  
        player1_y = 575
```

9. Defining Ball limits

```python
ball_dir = -2
# Mudando a velocidade da boinha
def move_ball():  
    global ball_x  
    global ball_y  
    global ball_dir  
  
    ball_x += ball_dir  
	# Primeiro marca o ponto que a bola tem que voltar
    if ball_x < 120:  
	    # Se o jogador estiver abaixo vai sempre voltar
        if player1_y < ball_y + 23:  
	        # Agora delimita o limite de em quanto pode estar
            if player1_y + 146 > ball_y:  
	            # Agora muda a direção da bolinha
                ball_dir *= -1
```

10. Player 2 and ball moves

```python
player2_y = 310

# Faz o player 2 acompanhar a bolinha, apenas para checar
def move_player2():  
    global player2_y  
    player2_y = ball_y  
  
def move_ball():  
    global ball_x  
    global ball_y  
    global ball_dir  
    global ball_dir_y  
  
    ball_x += ball_dir  
    ball_y += ball_dir_y  
  
    if ball_x < 120:  
        if player1_y < ball_y + 23:  
            if player1_y + 146 > ball_y:  
                ball_dir *= -1  
	# Faz a bola retornar
    if ball_x > 1100:  
        if player2_y < ball_y + 23:  
            if player2_y + 146 > ball_y:  
                ball_dir *= -1  
	# Faz a bolinha se mover quando pate nas bordas
    if ball_y > 685:  
        ball_dir_y *= -1  
    elif ball_y <= 0:  
        ball_dir *= -1
```

11. Restarting ball position

```python
def move_ball():  
    global ball_x  
    global ball_y  
    global ball_dir  
    global ball_dir_y  
  
    ball_x += ball_dir  
    ball_y += ball_dir_y  
  
    if ball_x < 120:  
        if player1_y < ball_y + 23:  
            if player1_y + 146 > ball_y:  
                ball_dir *= -1  
  
    if ball_x > 1100:  
        if player2_y < ball_y + 23:  
            if player2_y + 146 > ball_y:  
                ball_dir *= -1  
  
    if ball_y > 685:  
        ball_dir_y *= -1  
    elif ball_y <= 0:  
        ball_dir *= -1  

	# Checa se a bolinha vai extrapolar os limites
    if ball_x < -50:  
        ball_x = 617  
        ball_y = 337  
        ball_dir_y *= -1  
        ball_dir *= 1  
  
    elif ball_x > 1320:  
        ball_x = 617  
        ball_y = 337  
        ball_dir_y *= -1  
        ball_dir *= 1

```

12. Add score

```python
score1 = 0  
score1_img = pygame.image.load("assets/score/0.png")  
score2 = 0  
score2_img = pygame.image.load("assets/score/0.png")

def draw():  
    window.blit(field, (0, 0))  
    window.blit(player1, (50, player1_y))  
    window.blit(player2, (1150, player2_y))  
    window.blit(ball, (ball_x, ball_y))  
    window.blit(score1_img, (500,50))  
    window.blit(score2_img, (710,50))

def move_ball():  
    global ball_x  
    global ball_y  
    global ball_dir  
    global ball_dir_y  
    global score1  
    global score2  
    global score1_img  
    global score2_img  
  
    ball_x += ball_dir  
    ball_y += ball_dir_y  
  
    if ball_x < 120:  
        if player1_y < ball_y + 23:  
            if player1_y + 146 > ball_y:  
                ball_dir *= -1  
  
    if ball_x > 1100:  
        if player2_y < ball_y + 23:  
            if player2_y + 146 > ball_y:  
                ball_dir *= -1  
  
    if ball_y > 685:  
        ball_dir_y *= -1  
    elif ball_y <= 0:  
        ball_dir *= -1  
  
    if ball_x < -50:  
        ball_x = 617  
        ball_y = 337  
        ball_dir_y *= -1  
        ball_dir *= 1  
        score2 += 1  
        score2_img = pygame.image.load(f"assets/score/{str(score2)}.png")  
  
    elif ball_x > 1320:  
        ball_x = 617  
        ball_y = 337  
        ball_dir_y *= -1  
        ball_dir *= 1  
        score1 += 1  
        score1_img = pygame.image.load(f"assets/score/{str(score1)}.png")

```

13. Finalize the project

```python
win = pygame.image.load("assets/win.png")

def draw():  
    if score1 or score2 < 9:  
        window.blit(field, (0, 0))  
        window.blit(player1, (50, player1_y))  
        window.blit(player2, (1150, player2_y))  
        window.blit(ball, (ball_x, ball_y))  
        window.blit(score1_img, (500,50))  
        window.blit(score2_img, (710,50))  
        move_ball()  
        move_player()  
        move_player2()  
    else:  
        window.blit(win, (300,330))
```
