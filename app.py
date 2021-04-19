from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from twilio.twiml.voice_response import VoiceResponse, Say

app = Flask(__name__)

@app.route("/whatsapp", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)

    # Start our TwiML response
    resp = MessagingResponse()

    # Add a message
    # resp.message("The Robots are coming! Head for the hills!")


    # Determine the right reply for this message
    if body == 'hello':
        msg = resp.message("Hi!")
        msg.media("https://images.pexels.com/photos/4126695/pexels-photo-4126695.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500")
    elif body == 'bye':
        msg = resp.message("Goodbye")
        # Add a picture message
        msg.media("https://images.pexels.com/photos/246804/pexels-photo-246804.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500")
    elif body == 'when':
        #resp = VoiceResponse()
        #resp.say('The Robots are coming! Head for the hills!')
        msg = resp.message("The Robots are coming! Head for the hills!")
        msg.media("https://images.pexels.com/photos/2085831/pexels-photo-2085831.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500")
    elif body == 'hi bangboy!':
        msg = resp.message("hi!")
        msg.media("https://scontent.fsin10-1.fna.fbcdn.net/v/t1.6435-9/134744884_2836624303292522_2481575298273072520_n.jpg?_nc_cat=110&ccb=1-3&_nc_sid=09cbfe&_nc_ohc=Kcglr8XTHt4AX-mM1_q&_nc_ht=scontent.fsin10-1.fna&oh=97e1c7f6118d75d94d6392435aabb5c9&oe=60A38F87")
    else:
        msg = resp.message("Indeed.")


    return str(resp)

@app.route("/")
def hello():
  return "(x_-)___ ..|.."

if __name__ == "__main__":
    app.run()