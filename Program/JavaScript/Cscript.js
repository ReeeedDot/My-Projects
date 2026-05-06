//calculte the remaining time until the christmas

function calculateTimeUntilChristmas(){
    const now = new Date();
    const christmas = new Date(now.getFullYear(),11,25);
    const timeDiff= christmas-now;

    //Convert the time difference to days,hours,minutes, and seconds
    
    const days= Math.floor(timeDiff/(1000*60*60*24));
    const hours=Math.floor((timeDiff%(1000*60*60*24))/(1000*60*60));
    const minutes=Math.floor((timeDiff%(1000*60))/(1000*60));
    const seconds=Math.floor((timeDiff%(1000*60))/1000);

    //Display the countdown on the page

    document.grtElementById("countdown").innerHTML='${days}d ${hours}h ${minutes}m ${seconds}s';

    //update the countdown every second

    setTimeout(calculateTimeUntilChristmas,1000);
}
calculateTimeUntilChristmas();
