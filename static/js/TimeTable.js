function hide_message(element){
    document.getElementById('message_box').style.display = "none";
    }

function show_today(){
    document.getElementById('daily_timetable').style.display = "block";
    document.getElementById('tomorrow_timetable').style.display = "none";
    document.getElementById('timetable_for_this_week').style.display = "none";
    document.getElementById('timetable_for_next_week').style.display = "none";
    }

function show_tomorrow(){
    document.getElementById('daily_timetable').style.display = "none";
    document.getElementById('tomorrow_timetable').style.display = "block";
    document.getElementById('timetable_for_this_week').style.display = "none";
    document.getElementById('timetable_for_next_week').style.display = "none";
    }

function show_this_week(){
    document.getElementById('daily_timetable').style.display = "none";
    document.getElementById('tomorrow_timetable').style.display = "none";
    document.getElementById('timetable_for_this_week').style.display = "block";
    document.getElementById('timetable_for_next_week').style.display = "none";
    }

function show_next_week(){
    document.getElementById('daily_timetable').style.display = "none";
    document.getElementById('tomorrow_timetable').style.display = "none";
    document.getElementById('timetable_for_this_week').style.display = "none";
    document.getElementById('timetable_for_next_week').style.display = "block";
    }