// Express Router
const express = require('express');
const router = express.Router();

router.get('/', (req, res) => res.send('Auth Route'));

//@route: GET
//@description: Auth route
//@access Public (No Token Needed)

module.exports = router;