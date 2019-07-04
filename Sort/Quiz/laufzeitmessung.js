 
let name = 'laufzeit';
let anz = 18;
function saveAnswer() {
 
    for (let i=0; i<anz; i++) {
        x = document.getElementById('q'+i.toString()).value;
        localStorage.setItem(name+i.toString(),x);
    }

}

function getStoredResults() {
    let q = new Array(anz).fill("");
    for (let i=0; i<anz; i++) {
      let x = localStorage.getItem(name+i.toString());
      document.getElementById("q"+i.toString()).value = x;
    }
 }
 getStoredResults();