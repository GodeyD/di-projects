import game

def get_user_menu_choice():
    selction = input('Select choice number:\n1.-Play a new game\n2.-Show scores\n3.-Quit\nchouse 1, 2 or 3: ')
    print(selction)

def print_results(results= dict):
    print(f'The results are:\nWins: {results[list(results)[0]]} \nLoses: {results[list(results)[1]]}\nDraws: {results[list(results)[2]]}\nTks for playing')

def main():
    None


Game.play()
win = 0
loss = 0
draw = 0
if yo.play() == 'win':
    win += 1
result_dict = {'win': 0,'loss': 0,'draw': 0}
result_dict_keys = result_dict.keys()
get_user_menu_choice()
print_results(result_dict)
print(result_dict[list(result_dict)[2]])
