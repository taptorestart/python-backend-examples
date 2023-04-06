function main()
{
    (function() {
        var httpRequest = new XMLHttpRequest();
        httpRequest.onreadystatechange = logContents;
        httpRequest.open('GET', 'https://api.taptorestart.com/v1/test/');
        httpRequest.setRequestHeader('Authorization', 'Bearer yourtoken');
        httpRequest.send();
        function logContents() {
            if (httpRequest.readyState === XMLHttpRequest.DONE) {
                console.log(httpRequest.status);
                console.log(httpRequest.responseText);
            }
        }
    })();
}
