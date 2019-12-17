// Express Router
const express = require('express');
const router = express.Router();

router.get('/', (req, res) => res.send('User Route'));

//@route: GET
//@description: User route
//@access Public (No Token Needed)

module.exports = router;