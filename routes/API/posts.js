// Express Router
const express = require('express');
const router = express.Router();

router.get('/', (req, res) => res.send('Posts Route'));

//@route: GET
//@description: Posts route
//@access Public (No Token Needed)

module.exports = router;