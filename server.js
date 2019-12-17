const express = require('express');
const connectDB = require('./config/db');

const app = express();

// Connect Database
connectDB();

// Initialize Middleware
app.use(express.json({ extended: false }));

app.get('/', (req, res) => res.send('API Running...'));

// --------- Define Routes --------- //

// Users
app.use('/api/users', require('./routes/api/users'));
// Auth
app.use('/api/auth', require('./routes/api/auth'));
// Profile
app.use('/api/profile', require('./routes/api/profile'));
// Posts
app.use('/api/posts', require('./routes/api/posts'));

const PORT = process.env.PORT || 5000;

app.listen(PORT, () => console.log(`Server started on port ${PORT}`));

