let name = "sort";
a = new Array(3); 
a[0] = [];
a[0].push("4 13 92 42 11 7 12");
a[0].push("4 7 92 42 11 13 12");
a[0].push("4 7 11 42 92 13 12");

a[1] = [];    
a[1].push("2 14 22 1 13 9 25");
a[1].push("2 14 1 13 9 22 25");
a[1].push("2 1 13 9 14 22 25");

a[2] = [];
a[2].push("6");
a[2].push("13");
a[2].push("4 17");
a[2].push("4 17 24");
a[2].push("42 88");
a[2].push("7 12");
a[2].push("7 12 42 88");
a[2].push("4 7 12 17 24 42 88");

a[3] = [];
a[3].push("10 5 67 18 3 22 7")
a[3].push("0 6 18")
a[3].push("10 5 7 3 18 22 67")
a[3].push("0 3 5")
a[3].push("3 5 7 10 18 22 67")
a[3].push("2 3 7")

a[4] = [];
a[4].push("22 41 43 7 42 19")
a[4].push("0 5 43")
a[4].push("22 41 19 7 42 43")
a[4].push("0 4 19")
a[4].push("7 19 41 22 42 43")
a[4].push("0 1 7")

a[5] = [];
a[5].push("15 8 9 16 18 28 22 38 26")
a[5].push("0 3 8")
a[5].push("8 15 9 16 18 28 22 38 26")
a[5].push("1 3 9")


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

