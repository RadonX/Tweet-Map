var source = new EventSource('/tweets/stream');
source.onmessage = function(e) {
    document.body.innerHTML += e.data + '<br>';
};

source.addEventListener('message', function(event) {
    console.log('onmessage');
    console.log(event.data);
}, false);
source.addEventListener('open', function(event) {
    console.log('> Connection was opened');
}, false);
source.addEventListener('error', function(event) {
    if (event.eventPhase == 2) { //EventSource.CLOSED
        console.log('> Connection was closed');
    }
}, false);