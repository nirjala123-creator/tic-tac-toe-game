import tkinter as tk
from tkinter import messagebox

def check_winner():
    for combo in [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]:
        if buttons[combo[0]]["text"]==buttons[combo[1]]["text"]==buttons[combo[2]]["text"] !="":
            buttons[combo[0]].config(bg="green")
            buttons[combo[1]].config(bg="green")
            buttons[combo[2]].config(bg="green")
            messagebox.showinfo("tic-tac-toe",f"player{buttons[combo[0]]["text"]}wins!")
            root.quit()
def button_click(index):
    if buttons[index]["text"]=="" and not winner:
       buttons[index]["text"] = current_player
       check_winner()
       toggle_player()
def toggle_player ():
    global current_player
    current_player="X" if current_player =="O" else "O"
    label.config(text=f"Player{current_player}'s turn")
root=tk.Tk()
root.title("Tic-Tac-Toe")
buttons=  [tk.Button(root, text="", font=("normal", 25), width=6, height=2, command=lambda i=i: button_click(i)) for i in range(9)]
for i,button in enumerate(buttons):
    button.grid(row=i //3,column=i%3)
current_player="X"
winner=False
label=tk.Label(root,text=f"Player{current_player}'s turn",font=("normal",16))    
label.grid(row=3,column=0,columnspan=3)
root.mainloop()




import tkinter as tk
from tkinter import messagebox
import random

# Initialize window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Game variables
buttons = []
current_player = "X"
winner = False

# Check for a winner
def check_winner():
    global winner
    for combo in [[0,1,2],[3,4,5],[6,7,8],
                  [0,3,6],[1,4,7],[2,5,8],
                  [0,4,8],[2,4,6]]:
        if (buttons[combo[0]]["text"] == 
            buttons[combo[1]]["text"] == 
            buttons[combo[2]]["text"] != ""):
            for i in combo:
                buttons[i].config(bg="green")
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} wins!")
            winner = True
            return

    # Check for draw
    if all(button["text"] != "" for button in buttons) and not winner:
        messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
        winner = True

# Switch turns
def toggle_player():
    global current_player
    current_player = "X" if current_player == "O" else "O"
    label.config(text=f"Player {current_player}'s turn")

# Player clicks a button
def button_click(index):
    global current_player, winner

    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        check_winner()
        toggle_player()

        if not winner and current_player == "O":
            root.after(500, computer_move)  # delay for computer's move

# Computer's move (random)
def computer_move():
    global current_player, winner

    empty_indices = [i for i, btn in enumerate(buttons) if btn["text"] == ""]
    if empty_indices and not winner:
        move = random.choice(empty_indices)
        buttons[move]["text"] = "O"
        check_winner()
        toggle_player()

# Create buttons
for i in range(9):
    btn = tk.Button(root, text="", width=6, height=3, font=("Arial", 24),
                    command=lambda i=i: button_click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

# Label to show turn
label = tk.Label(root, text="Player X's turn", font=("Arial", 16))
label.grid(row=3, column=0, columnspan=3)

# Start GUI
root.mainloop()