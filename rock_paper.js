var a=require("readline-sync")
function win(){
    console.log ('You win!')
}

function lose(){
    console.log('You lose!')
}

while (true){
    player_choice = a.question('What do you pick? (rock, paper, scissors)')
    player_choice.trim()
    // random_moves=Math.random(0, 2)
    // const computer_choice = Math.floor(Math.random()*3);
    moves = ['rock', 'paper', 'scissors']
    var computer_choice = moves[Math.floor(Math.random()*moves.length)];
    // computer_choice =moves[random_moves]
    console.log("computer_choice",computer_choice)

    if (player_choice ==computer_choice){
        console.log('Draw!')
    }else if  (player_choice== 'rock' ||  computer_choice == 'scissors'){
        win()
    }else if  (player_choice== 'paper' || computer_choice == 'scissors'){
        lose()
    }else if (player_choice == 'scissors' || computer_choice == 'paper'){
        win()
    }else if (player_choice == 'scissors' || computer_choice == 'rock'){
        lose()
    }else if (player_choice == 'paper'   || computer_choice == 'rock'){
        win()
    }else if (player_choice == 'rock' || computer_choice == 'paper' ){
        lose()
    }
    again =a.question('Do you want to play again? (y or n)').trim()
    if (again == 'n')
        break 
}
