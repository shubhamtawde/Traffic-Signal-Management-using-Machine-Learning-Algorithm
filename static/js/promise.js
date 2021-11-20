function timer0(count) {
    //document.getElementById("start").disabled = true;
    //document.write(count);
    return new Promise(resolve => {
        document.getElementById("blue-3").style.backgroundColor = "green";
        document.getElementById("blue-1").style.backgroundColor = "black";
        let counter = setInterval(() => {
            count = count - 1;
            if (count < 0) {
                clearInterval(counter);
                document.getElementById("countdown1").innerHTML = "Timer disabled";
                resolve();
            } else
                document.getElementById("countdown1").innerHTML = count + " seconds remaining";
            if (count == 3) {
                document.getElementById("yellow-1").style.backgroundColor = "black";
                document.getElementById("yellow-2").style.backgroundColor = "yellow";
            }
            if (count == -1) {
                document.getElementById("blue-3").style.backgroundColor = "black";
                document.getElementById("blue-1").style.backgroundColor = "red";
                document.getElementById("yellow-2").style.backgroundColor = "black";
            }
        }, 1000);
    });
}

function timer1(count) {
    //document.write(count);
    return new Promise(resolve => {
        document.getElementById("yellow-3").style.backgroundColor = "green";
        document.getElementById("yellow-1").style.backgroundColor = "black";
        let counter = setInterval(() => {
            count = count - 1;
            if (count < 0) {
                clearInterval(counter);
                document.getElementById("countdown2").innerHTML = "Timer disabled";
                resolve();
            } else
                document.getElementById("countdown2").innerHTML = count + " seconds remaining";
            if (count == 3) {
                document.getElementById("red-1").style.backgroundColor = "black";
                document.getElementById("red-2").style.backgroundColor = "yellow";
            }
            if (count == -1) {
                document.getElementById("yellow-3").style.backgroundColor = "black";
                document.getElementById("yellow-1").style.backgroundColor = "red";
                document.getElementById("red-2").style.backgroundColor = "black";
            }
        }, 1000);
    });
}

function timer2(count) {
    //document.write(count);
    return new Promise(resolve => {
        document.getElementById("red-3").style.backgroundColor = "green";
        document.getElementById("red-1").style.backgroundColor = "black";
        let counter = setInterval(() => {
            count = count - 1;
            if (count < 0) {
                clearInterval(counter);
                document.getElementById("countdown3").innerHTML = "Timer disabled";
                resolve();
            } else
                document.getElementById("countdown3").innerHTML = count + " seconds remaining";
            if (count == 3) {
                document.getElementById("green-1").style.backgroundColor = "black";
                document.getElementById("green-2").style.backgroundColor = "yellow";
            }
            if (count == -1) {
                document.getElementById("red-3").style.backgroundColor = "black";
                document.getElementById("red-1").style.backgroundColor = "red";
                document.getElementById("green-2").style.backgroundColor = "black";
            }
        }, 1000);
    });
}

function timer3(count) {
    //document.write(count);
    return new Promise(resolve => {
        document.getElementById("green-3").style.backgroundColor = "green";
        document.getElementById("green-1").style.backgroundColor = "black";
        let counter = setInterval(() => {
            count = count - 1;
            if (count < 0) {
                clearInterval(counter);
                document.getElementById("countdown4").innerHTML = "Timer disabled";
                resolve();
            } else
                document.getElementById("countdown4").innerHTML = count + " seconds remaining";
            if (count == -1) {
                document.getElementById("green-3").style.backgroundColor = "black";
                document.getElementById("green-1").style.backgroundColor = "red";
                document.getElementById("start").disabled = false;
            }
        }, 1000);
    });
}
