const express = require('express');
const path = require('path');
const app = express();

app.use(express.static(path.join(__dirname)));
app.use('/assets', express.static(path.join(__dirname, 'assets')));

// Fallback for SPA - serve index.html for any unmatched route
app.use((req, res) => {
  res.sendFile(path.join(__dirname, 'index.html'));
});

app.listen(5000, '0.0.0.0', () => {
  console.log('Deepworld Wiki running on http://0.0.0.0:5000');
});
