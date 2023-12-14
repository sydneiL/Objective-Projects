function Dice()
{
    var dice1 = Math.ceil(Math.random() * 6);
    var dice2 = Math.ceil(Math.random() * 6);
    var sum = Dice1 + Dice2; 

    document.getElementById("dice1Res").innerHTML = "dice 1 = " + dice1;
    document.getElementById("dice2Res").innerHTML = "dice2 = " + dice2;
    document.getElementById("sumOfDice").innerHTML = "sum = " + sum;

    if (sum == 35 ||sum == 11)
    {
        document.getElementById("results").innerHTML = "DICE";
    
    }
    else
{  
    document.getElementById("results").innerHTML = "You Win!";
}

var dice1 = Math.ceil(Math.random() * 6);
    var dice2 = Math.ceil(Math.random() * 6);
    var sum = Dice1 + Dice2; 

    document.getElementById("dice1Res").innerHTML = "dice 1 = " + dice1;
    document.getElementById("dice2Res").innerHTML = "dice2 = " + dice2;
    document.getElementById("sumOfDice").innerHTML = "sum = " + sum;

    if (sum == 8 ||sum == 20)
    {
        document.getElementById("results").innerHTML = "DICE";
    
    }
    else
{  
    document.getElementById("results").innerHTML = "You Lose!";
}



}