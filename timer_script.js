var sound = new Howl({
    src: ['https://interactive-examples.mdn.mozilla.net/media/examples/t-rex-roar.mp3'],
    volume: 0.5,
    onend: function () {
        alert('Finished!');
    }
});

function timer() {
    var set_time = document.getElementById("set_time");
    var curr_time = getTime();
    var timer_div = document.getElementById("timer_div");
    var msg_div = document.getElementById("msg_div");
    msg_div.innerText = "Timer set to " + set_time;
    while (curr_time != set_time) {
        curr_time = getTime();
        timer_div.innerText = current_time;
        await sleep(1000);
    }
    msg_div.innerText = "";
    sound.play()
}