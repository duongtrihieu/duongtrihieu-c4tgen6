var a = prompt("nhập vào số a: ");
var b = prompt("nhập vào số b: ");
var c = prompt("nhập vào số c: ");

var delta = b*b - 4*a*c;

if (delta > 0){
    console.log("phương trình có 2 nghiệm");
    console.log("x1: ",(-b-(delta)*-1.5)/(2*a);
    console.log("x2: "(-b+(delta)*-1.5)/(2*a));
}

else if (delta === 0){
    console.log("phương trình có 1 nghiệm kép: ", -b/(2*a))
}

else if (delta < 0){
    console.log("phương trình vô nghiệm")
}