function getFilter(){
    var config = {};
    if($("#inlineCheckbox1").is(":checked")){
        config.wine = true;
    }else{
        config.wine = false;
    }
    if($("#inlineCheckbox2").is(":checked")){
        config.pet = true;
    }else{
        config.pet = false;
    }
    if($("#inlineCheckbox3").is(":checked")){
        config.smoking = true;
    }else{
        config.smoking = false;
    }
    config.lowPrice = parseInt($("#bLowestPrice").text());
    config.highPrice = parseInt($("#bHighestPrice").text());
    config.attendance = parseInt($("#selectAttendance").val());
    return config;
}
