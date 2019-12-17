const express = require('express');
const router = express.Router();
const gravatar = require('gravatar');


//  Documentation: https://express-validator.github.io/docs/  //
// ====================================================== //
//  express-validator: requires to express-validator/check are deprecated.
// You  should just use require("express-validator") instead.  //
// ====================================================== //
const {
    check,
    validationResult
} = require('express-validator');

const User = require('../../models/User');

router.post('/', [
        check('name', 'Name is required')
        .not()
        .isEmpty(), //  << Important!  
        check('email', 'Please include a valid email address').isEmail(),
        check('password', 'Please enter a password with 6 or more characters').isLength({
            min: 6
        }),
    ],
    async (req, res) => {
        // Data sent to this route & handles the response
        const errors = validationResult(req);
        if (!errors.isEmpty()) {
            return res.status(400).json({
                errors: errors.array()
            });
        }

        // Destructure: parsing request.body
        const {
            name,
            email,
            password
        } = req.body;

        try {
            //  👀 See if user exists
            let user = await User.findOne({ email });
                if(user) {
                    res.status(400).json({ errors: [ { msg: 'User already sxists' }] });
                }
            // 😬 Get users Gravatar
            const avatar = gravatar.url(email, {
                s: '200',
                r: 'pg',
                d: 'mm'
            })

            user = new User ({
                name,
                email,
                avatar,
                password
            });

            // 🔐 Encrypt password (bcrypt)

            // ✅ Return jsonwebtoken
            res.send('User Route');
        } catch(err) {
            console.error(err.message);
            res.status(500).send('Server Error');
        }
    });

//@route: POST api/users
//@description: Register user
//@access Public (No Token Needed)

module.exports = router;