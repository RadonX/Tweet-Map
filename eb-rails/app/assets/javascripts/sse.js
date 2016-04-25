

var stage = $('#flying-tweet');

var Tweet = function(text){
    this.appearance =  $('<div style="min-width:400px;font-size:larger;color: #eeeeee;">'+text+'</div>');
    this.appearance.hide().appendTo(stage);
}


Tweet.prototype.animate = function() {
    var that = this;
    var appearance = that.appearance;
    appearance.animate({
        left:-700
    }, 12000,'swing',function(){
        appearance.hide();
    });
}

Tweet.prototype.perform = function() {
    this.appearance.css({
        position:'absolute',
        left: stage.width()+'px',
        top:240||0,
        zIndex:10,
        display:'block'
    });
    this.animate();
}

var source = new EventSource('/tweets/stream?id='+sseid);
//source.onmessage = function(e) {};

source.addEventListener('message', function(event) {
    console.log(event.data);
    var tweet = new Tweet(event.data);
    tweet.perform();
}, false);
source.addEventListener('open', function(event) {
}, false);
source.addEventListener('error', function(event) {
    if (event.eventPhase == 2) { //EventSource.CLOSED
        console.log('> Connection was closed');
    }
}, false);
