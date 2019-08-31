from sendsms.backends.base import BaseSmsBackend


def send_sms(message: str, mobile: str):
    """

    @param message:
    @param mobile:
    @return:
    """
    import urllib.request  # Python URL functions
    import urllib.parse

    authkey = "289707Aoshv7jQ5d554200"  # Your authentication key.

    mobiles = mobile  # Multiple mobiles numbers separated by comma.

    message = message  # Your message to send.

    sender = "CHAKLE"  # Sender ID,While using route4 sender id should be 6 characters long.

    route = "4"  # Define route

    # Prepare you post parameters
    values = {
        'authkey': authkey,
        'mobiles': mobiles,
        'message': message,
        'sender': sender,
        'route': route
    }

    url = "http://api.msg91.com/api/sendhttp.php"  # API URL

    postdata = urllib.parse.urlencode(values)  # URL encoding the data here.
    data = postdata.encode('utf-8')

    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req, data)
    output = response.read()  # Get Response
    print(output)
    return output  # Print Response


class Msg91SmsBackend(BaseSmsBackend):
    def send_messages(self, messages):
        """

        @param messages:
        """
        for message in messages:
            for to in message.to:
                try:
                    send_sms(message.body, to)
                except:
                    if not self.fail_silently:
                        raise
