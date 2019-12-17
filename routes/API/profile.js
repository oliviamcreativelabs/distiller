// Express Router
const express = require('express');
const router = express.Router();

router.get('/', (req, res) => res.send('Profile Route'));

//@route: GET
//@description: Profile route
//@access Public (No Token Needed)

module.exports = router;