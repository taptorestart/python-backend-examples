function main()
{
    (function() {
        const httpRequest = new XMLHttpRequest();
        const data = "{ }";
        httpRequest.onreadystatechange = logContents;
        httpRequest.open('POST', 'https://api.taptorestart.com/v1/test/');
        httpRequest.setRequestHeader('Authorization', 'Bearer yourtoken');
        httpRequest.setRequestHeader('Content-Type', 'application/json');
        httpRequest.send(data);
        function logContents() {
            if (httpRequest.readyState === XMLHttpRequest.DONE) {
                console.log(httpRequest.status);
                console.log(httpRequest.responseText);
            }
        }
    })();
}