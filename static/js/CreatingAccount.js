function ShowLeadForm(element){
    document.getElementById('Form').style.display = "flex";
    document.getElementById('LeadGroup').style.display = "flex";
    document.getElementById('StudentGroup').style.display = "none";
}
function ShowStudentForm(element){
    document.getElementById('Form').style.display = "flex";
    document.getElementById('StudentGroup').style.display = "flex";
    document.getElementById('LeadGroup').style.display = "none";
}
function CheckRegistrationForm(element){
    var form = document.getElementById('Form');
    var error = document.getElementById('error');

    if (form.firstName.value == "" ||
        form.name.value == "" ||
        form.email.value == "" ||
        form.pass.value == "" ||
        form.repass.value == "")
        {
        PrintError("Все поля должны быть заполнены");
        return false;
    }
    else if(document.getElementById('Lead').checked && form.Lgroup.value == "")
    {
        PrintError("Все поля должны быть заполнены");
        return false;
    }
     else if(document.getElementById('Student').checked && form.Sgroup.value == "0")
    {
        PrintError("Все поля должны быть заполнены");
        return false;
    }
    if (CheckLenght(form.firstName.value, 20, 2))
    {
        PrintError("Ваше имя слишком короткое или слишком длинное");
        return false;
    }
    if (CheckLenght(form.name.value, 20, 2)) {
        PrintError("Ваша фамилия слишком короткая или слишком длинная");
        return false;
    }
    if (CheckLenght(form.Lgroup.value, 10, 2) && document.getElementById('Lead').checked) {
        PrintError("Название группы слишком короткое или слишком длинное");
        return false;
    }
    if (CheckLenght(form.pass.value, 30, 4)) {
        PrintError("Длинна пароля должна быть от 4 до 30 символов");
        return false;
    }
    if (form.pass.value != form.repass.value) {
        PrintError("Пороли не совпадают");
        return false;
    }

    if(document.getElementById('Lead').checked)
    {
        form.userType.value=1;
    }
    else
    {
        form.userType.value=0;
    }
    return true;
}

function CheckLenght(string, Mlenght, mlenght) {
    if (string.length < mlenght || string.length > Mlenght) {
        return true;
    }
    else {
        return false;
    }
}

function PrintError(string) {
    var error = document.getElementById('error');
    error.style.display = "flex";
    error.innerHTML = string;
}
