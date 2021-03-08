// Update Time
const updateTime = setInterval(() => {
    const currentTime = new Date();
    let hours = currentTime.getHours();
    let minutes = currentTime.getMinutes();
    let seconds = currentTime.getSeconds();

    document.getElementById("time").innerHTML = `${hours > 9 ? hours : '0' + hours}:${minutes> 9 ? minutes : '0' + minutes}:${seconds> 9 ? seconds : '0' + seconds}`;

}, 1000)