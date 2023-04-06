function main()
{
    (function() {
        const httpRequest = new XMLHttpRequest();
        const data = "{ }";
        httpRequest.onreadystatechange = logContents;
        httpRequest.withCredentials = true;
        httpRequest.open('POST', 'https://api.taptorestart.com/v1/test/');
        httpRequest.setRequestHeader('Cookie', 'sessionid=yoursessionid;');
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