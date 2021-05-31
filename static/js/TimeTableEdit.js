function show_week(week_num){
    if(week_num == 'week1'){
        document.getElementById('week2').style.display = "none";
        document.getElementById('week1').style.display = "block";
    }
    else{
        document.getElementById('week1').style.display = "none";
        document.getElementById('week2').style.display = "block";
    }
    document.getElementById('SubmitButton').style.display = "inline-block"
}

function show_pair(element){
    var pair = document.getElementById('p' + element.id[2] + '_d' + element.id[4] + '_week' + element.id[10] )
    if(element.id[0] == 'Y'){
        pair.style.display = "block";
    }
    else{
        pair.style.display = "none";
    }
}