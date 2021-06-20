from alarm import settings

def generate_url(channel_id):
    server_url = settings.SERVER_URL
    webhook = server_url + channel_id + "/alarm.json"
    return webhook