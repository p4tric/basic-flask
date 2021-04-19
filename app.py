from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

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
    elif body == 'bye':
        msg = resp.message("Goodbye")
        # Add a picture message
        msg.media("https://farm8.staticflickr.com/7090/6941316406_80b4d6d50e_z_d.jpg")
    elif body == 'when':
        msg = resp.message("The Robots are coming! Head for the hills!")
    elif body == 'hi':
        msg = resp.message("hi salva!")
        msg.media("https://scontent.fsin10-1.fna.fbcdn.net/v/t1.6435-9/134744884_2836624303292522_2481575298273072520_n.jpg?_nc_cat=110&ccb=1-3&_nc_sid=09cbfe&_nc_ohc=Kcglr8XTHt4AX-mM1_q&_nc_ht=scontent.fsin10-1.fna&oh=97e1c7f6118d75d94d6392435aabb5c9&oe=60A38F87")



    return str(resp)

@app.route("/")
def hello():
  return "(x_-)___ ..|.."

if __name__ == "__main__":
    app.run()