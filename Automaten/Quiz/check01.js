function check1() {
  let x1, x2;
  let text = "";

  x1 = document.getElementById("q1").value;
  x2 = document.getElementById("q2").value;

  // If x is Not a Number or less than one or greater than 10
  if (x1 === "5") {
    text += "1";
  } else {
    text += "0";
  }
  if (x2 === "10") {
    text += "1";
  } else {
    text += "0";
  }

  if (text === "11") {
    text = "OK"
  } else {
    text = "not OK : " + text;
  }

  document.getElementById("a1").innerHTML = text;
}