let name = "liste";
a = []; 
a[0] = [];
a[0].push("6 2 3 4");
a[0].push("0");

a[1] = [];    
a[1].push("3 4 5 2");
a[1].push("2");

a[2] = [];
a[2].push("None b b d d")

a[3] = [];
a[3].push("e d e")

a[4] = [];
a[4].push("4 5 3 6 2 7 1 8 0 9")

a[5] = [];
a[5].push("Keller")
a[5].push("4 3 8 7 6 2 1 0")

a[6] = [];
a[6].push("Schlange")
a[6].push("0 1 2 3 4 6 7 8")

 


function checkanswer(nr) {
  let anz = a[nr].length;
  let q = new Array(anz).fill("");
  let x = new Array(anz).fill("");
  let text = "";
  let x0;
  for (let i=0; i<anz; i++) {

    q[i] = "q"+nr+i.toString();
    x[i] = document.getElementById(q[i]).value;
    x0 =  x[i].replace(/\s+/g, " ").trim();
    text = (x0 === a[nr][i]) ? text + "1" : text + "0";
    localStorage.setItem(name+q[i],x[i]);
   
  }

  let good = "1";
  while (good.length < anz) good += "1";

  text = (text === good ? "OK" : "not OK : " + text)
  document.getElementById("a"+nr).innerHTML = text;
 
}
 
function getStoredResults(nr) {
  let anz = a[nr].length;
  let q = new Array(anz).fill("");
  let k = 0;
  for (let i=0; i<anz; i++) {
    q[i] = "q"+nr+i.toString();
    k +=  getVariable(name+q[i],q[i]);
  }

  if (k>0) checkanswer(nr);

}

function getVariable(name,id) {
  let x = localStorage.getItem(name);
  document.getElementById(id).value = (x !== null) ? x : "" ;
  if (x !== null) return 1
}

for (let i=0; i<a.length; i++) {
  getStoredResults(i);
}

