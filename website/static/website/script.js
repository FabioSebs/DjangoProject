//GSAP Portion (Animations)
let tlForm = new TimelineLite;

tlForm.to("#awanForm",.5, {opacity:.8 , ease: Power4})
.to("#formLogo",1.5, {scaleX: 1.5, scaleY: 1.5, ease: Back.easeOut.config(8)});

//Form Validation
const userName = document.getElementById("name");
const password = document.getElementById("pwd");
const gender = document.getElementById("gender");
const form = document.getElementById("awanForm");
const submit = document.getElementsByClassName("sub");
let userError = document.getElementById("errorUser");
let userPwd = document.getElementById("errorPwd");
let errorCount = 0;

console.log(userName);
console.log(password);
console.log(form);
console.log(userError);
console.log(userPwd);


function validate(){
    if(user() || pwd()){
        return false;
    }
    else {
        return true;
    }
}

function user(){
    let userInput = userName.value.trim()

    if (userInput==='' || userInput== null){
        errorMessage(userName, userError, "Username cannot be blank" );
        return true;
    }

    if (specialCharacter(userInput)){
        errorMessage(userName, userError, "Username cannot have special characters");
        return true;
    }

}

function pwd(){
    if (password.value.trim()==='' || password.value.trim()== null){
        errorMessage(password, userPwd, "Password cannot be blank");
        return true;
    }
}

function errorMessage(input, feildText, msg){
    input.style.outline = "1px solid red";
    feildText.innerHTML = msg;
}

function specialCharacter(string){
    confirmation = false;
    string.includes(')') ? confirmation = true 
    : string.includes('(') ? confirmation = true
    : string.includes('*') ? confirmation = true
    : string.includes('&') ? confirmation = true
    : string.includes('^') ? confirmation = true
    : string.includes('%') ? confirmation = true
    : string.includes('$') ? confirmation = true
    : string.includes('#') ? confirmation = true
    : string.includes('@') ? confirmation = true
    : string.includes('!') ? confirmation = true
    : string.includes('`') ? confirmation = true
    : string.includes('~') ? confirmation = true
    : string.includes('}') ? confirmation = true
    : string.includes('{') ? confirmation = true
    : string.includes(']') ? confirmation = true
    : string.includes('[') ? confirmation = true
    : string.includes('"') ? confirmation = true
    : string.includes('/') ? confirmation = true
    : string.includes('\'') ? confirmation = true
    : confirmation = false;

    return confirmation;

}
