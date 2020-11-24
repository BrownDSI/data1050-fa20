const express = require('express');
const path = require('path');
const http = require('http');
const request = require('request');
const Joi = require('@hapi/joi');
const bodyParser = require('body-parser');
const session = require('express-session');
require ('dotenv').config('../.env');

const USERNAME = process.env.USERNAME;
const PASSWORD = process.env.PASSWORD;
const isValidUsernameAndPassword = (username, password) => username === USERNAME && password === PASSWORD;
const SECOND = 1000;

//instantiate server
const app = express();
const port = process.env.PORT || 8080;
app.set('port', port);
const server = http.createServer(app);

// middleware
app.use(express.static(__dirname + '/public'));
app.use(bodyParser.urlencoded({
    extended: true
}));
app.use(bodyParser.json());

// if deployed on heroku server, use https instead of http
if (process.env.NODE_ENV === 'production') {
    app.use((req, res, next) => {
        if (req.header('x-forwarded-proto') !== 'https')
            res.redirect(`https://${req.header('host')}${req.url}`);
        else
            next();
    });
}

// set ejs as view engine
app.set('views', path.join(__dirname, '/views'));
app.set('view engine', 'ejs');

// for session
app.use(session({
    secret: process.env.APP_SECRET,
    resave: true,
    saveUninitialized: true
}));

// Starts the server.
server.listen(port, function () {
    console.log(`Starting server on port ${port}`);
});

// Redirect base page to login page
app.get('/', (req, res) => {
    res.redirect('/login');
});

// render Login page on get request
app.get('/login', (req, res) => {
    res.render('pages/login');
});

// validate login information on post request
app.post('/login', (req, res) => {
    // ensure nothing weird being sent to server from client
    const schema = Joi.object({
        username: Joi.string().max(100),
        password: Joi.string().max(100)
    });
    const { error, value } = schema.validate({ username: req.body.username, password: req.body.password });

    if (error || !isValidUsernameAndPassword(req.body.username, req.body.password)) {
        res.json({
            isValid: false,
            message: 'invalid arguments'
        });
    } else {
        // user inputted proper username & password, create session that timesout after 30 seconds
        req.session.loggedin = true;
        req.session.cookie.maxAge = 30 * SECOND;
        res.json({
            isValid: true,
            message: 'valid arguments'
        });
    }
});

// handle get request for hidden page
app.get('/hidden-page', (req, res) => {
    // provide access if user has active session, deny otherwise
    if (req.session.loggedin){
        res.render('pages/hidden');
    } else {
        res.redirect('/')
    }
});

// generates js-based word
app.get('/genword', (req, res) => {
    let keywords = 'projector pokemon beats fitbit apples nintendo pillow phone tv t-rex bus crayons water bottle pens pencils dog cornflakes alexa earbuds monitor socks sandals xylophone kindle ssd tablet chromebook backpack'.split(' ');
    word = keywords[Math.floor(Math.random() * keywords.length)];
    // if we wanted infinite words we could do so using this, but some of the words aren't particularly searchable
    // request('https://random-word-api.herokuapp.com/word?number=1', (err, resp, body) => console.log(body));
    res.json({
        keyword: word
    });
})
