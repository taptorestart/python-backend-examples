function main()
{
    (function() {
        const httpRequest = new XMLHttpRequest();
        httpRequest.onreadystatechange = logContents;
        httpRequest.open('GET', 'https://google.com');
        httpRequest.send();
        function logContents() {
            if (httpRequest.readyState === XMLHttpRequest.DONE) {
                console.log(httpRequest.status);
                console.log(httpRequest.responseText);
            }
        }
    })();
}