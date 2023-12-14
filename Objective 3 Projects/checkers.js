//Array will help us build the board//
var board = [
   [null,'i',null,'i', null, 'i',null, 'i'],
   [null,'i',null,'i', null, 'i',null, 'i'],
   [null,'i',null,'i', null, 'i',null, 'i'],
   [null, null,null,null,null,null,null,null],
   [null, null,null,null,null,null,null,null],
   ['b',null,'b',null,'b',null,'b',null],
   [null,'b',null,'b',null,'b',null,'b'],
   ['b',null,'b',null,'b',null,'b',null]
]

var selValueElem = document.querySelector('#selectedSquare');

function createBoard(){
      var theBoard = document.createElement('section');
     theBoard.id='checkersBoard';
     document.body.appendChil(theBoard);

    for(var i=0; i < board.length; i++){
      for (var j=0; j<board.length; j++){
        var square = document.createElement('div');
        square.classList.add('square');
        square.setAttribute("id","div" + i + j);
      
    if((i+j)% 2 ==1){
        square.classList.add('bg');
        square.addEventListener("click", movePiece);
    }   
    
    theBoard.appendChild(square);
    
     if(board[i][j]){
        createPiece("piece" + i + j, 'checker-'+ board[i][j], square);
      }
    }     
  }
}

function createPiece(id, pieceClass, theSquare){

}

function movePiece(event){

}