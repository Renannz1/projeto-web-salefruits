const http = require('http');
const WebSocket = require('ws');
const fs = require('fs');
const path = require('path');

// Cria um servidor HTTP para servir o arquivo HTML
const server = http.createServer((req, res) => {
    if (req.url === '/') {
        fs.readFile(path.join(__dirname, 'index.html'), (err, data) => {
            if (err) {
                res.writeHead(500);
                res.end('Erro ao carregar o arquivo');
            } else {
                res.writeHead(200, { 'Content-Type': 'text/html' });
                res.end(data);
            }
        });
    } else {
        res.writeHead(404);
        res.end('Página não encontrada');
    }
});

// Cria o servidor WebSocket
const wss = new WebSocket.Server({ server });

wss.on('connection', (ws) => {
    console.log('Cliente conectado');

    ws.on('message', (message) => {
        console.log(`Mensagem recebida: ${message}`);
        // Envia a mensagem para todos os clientes, exceto o que enviou
        wss.clients.forEach(client => {
            if (client !== ws && client.readyState === WebSocket.OPEN) {
                client.send(message);
            }
        });
    });

    ws.on('close', () => {
        console.log('Cliente desconectado');
    });

    ws.on('error', (error) => {
        console.error('Erro WebSocket:', error);
    });
});

// Inicia o servidor HTTP e WebSocket
const port = 5500; // Porta usada pelo servidor
server.listen(port, () => {
    console.log(`Servidor rodando em http://localhost:${port}`);
});
