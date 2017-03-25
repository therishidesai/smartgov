const express = require('express');
const morgan = require('morgan');
const path = require('path');

const app = express();

// Setup logger
app.use(morgan(':remote-addr - :remote-user [:date[clf]] ":method :url HTTP/:http-version" :status :res[content-length] :response-time ms'));

// Serve static assets
app.use(express.static(path.resolve(__dirname, 'js')));

app.get('*', function (req, res) {
  res.sendFile(path.join(__dirname, 'views', 'index.html'))
})
const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
  console.log(`App listening on port ${PORT}!`);
});
