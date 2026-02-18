// Install dependencies first: npm install express twilio cors body-parser
const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const { Twilio } = require('twilio');

const app = express();
app.use(cors());
app.use(bodyParser.json());

const accountSid = 'ACa694ad9769b86b1821f213a707934434';   // Twilio Account SID
const authToken = 'dbba63d4ea88e9ad11ed2b60be9c90bf';     // Twilio Auth Token
const client = new Twilio(accountSid, authToken);

const TWILIO_WHATSAPP_NUMBER = 'whatsapp:+14155238886'; // Sandbox number

app.post('/send-message', async (req, res) => {
    const { to, message } = req.body;
    if (!to || !message) return res.status(400).send({ error: 'Missing fields' });

    try {
        const msg = await client.messages.create({
            from: TWILIO_WHATSAPP_NUMBER,
            to: `whatsapp:${to}`,   // e.g. whatsapp:+91XXXXXXXXXX
            body: message
        });
        res.send({ success: true, sid: msg.sid });
    } catch (err) {
        console.error(err);
        res.status(500).send({ success: false, error: err.message });
    }
});

app.listen(3000, () => console.log('Server running on port 3000'));
