from dotenv import load_dotenv
from IPython import embed
import os
from fbchat.models import *
load_dotenv()

from fbchat import Client,log


class EchoBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)

        log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))
        if message_object.text == "polska":
            reply = Message(text="Husaria")
            self.send(reply, thread_id=thread_id, thread_type=thread_type)
            self.changeThreadEmoji("🥵", thread_id=thread_id)
        if message_object.text == "raczej":
            self.changeThreadColor(thread_id=thread_id, color= ThreadColor.VIKING)
        if message_object.text == "debug":
            embed()
        # If you're not the author, echo
        if author_id != self.uid:
            self.send(message_object, thread_id=thread_id, thread_type=thread_type)

client = EchoBot(os.getenv("FB_LOGIN"), os.getenv("FB_PASS"))
client.listen()